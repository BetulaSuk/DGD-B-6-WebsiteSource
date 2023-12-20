from asyncmy.cursors import DictCursor

import requests
from lxml import etree

TARGET_URL = "https://arxiv.org/list/math.NT/pastweek?show=53"
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'
}
TEMPLATE_DICT = {
    'paper_id': '',
    'title': '',
    'author': [],
    'link': '',
    'abstract': '',
    'keywords': '',
    'last_submit_time': ''
}


async def replace_arxivdata(connection, arxivdata_lst) -> None:
    async with connection.cursor(cursor=DictCursor) as cs:
        await cs.executemany(
            """REPLACE INTO arxivdata (
                author,
                link,
                abstract,
                title,
                paper_id,
                last_submit_time,
                keywords) 
                VALUES (%s,%s,%s,%s,%s,%s,%s)
                """, arxivdata_lst)
    await connection.commit()


async def check_arxivdata(connection) -> bool:
    async with connection.cursor(cursor=DictCursor) as cs:
        await cs.execute('SELECT EXISTS(SELECT 1 FROM arxivdata);')
        is_exist = await cs.fetchone()
        if (is_exist == 1):
            return True
        else:
            return False


async def readin_arxivdata(connection) -> None:
    retry_times = 0
    while True:
        try:
            response = requests.get(TARGET_URL, headers=HEADERS)
            tree = etree.HTML(response.text.encode('utf-8'))
            temp = tree.xpath('//a[@title="Abstract"]/@href')
            break
        except requests.exceptions.RequestException:
            print(f"request sent to {TARGET_URL} failed, retrying...({retry_times} times)")
            if retry_times >= 3:
                print("<WARNING> give up readin arxivdata, please check your Internet settings.")
                return
            else:
                continue

    result = []
    for i in range(0, len(temp)):
        dic = TEMPLATE_DICT.copy()
        dic['paper_id'] = temp[i][5:]
        link = 'https://arxiv.org' + temp[i]
        dic['link'] = link
        sub_response = requests.get(link, headers=HEADERS)
        tree = etree.HTML(sub_response.text.encode('utf-8'))
        sub_temp = tree.xpath('//blockquote[@class="abstract mathjax"]/text()')
        dic['abstract'] = sub_temp[1][:-6]
        au_temp = tree.xpath('//div[@class="authors"]//a/text()')
        dic['author'] = au_temp
        ti_temp = tree.xpath('//h1[@class="title mathjax"]/text()')
        dic['title'] = ti_temp[0]
        result.append(dic)

    arxivdata_lst = []

    for i in result:
        sub_lst = []
        sub_lst.append(str(i['author']))
        sub_lst.append(i['link'])
        sub_lst.append(i['abstract'])
        sub_lst.append(i['title'])
        sub_lst.append(i['paper_id'])
        sub_lst.append(i['last_submit_time'])
        sub_lst.append(str(i['keywords']))
        arxivdata_lst.append(sub_lst)

    await replace_arxivdata(connection, arxivdata_lst)
    print("arxivdata reading complete!")
