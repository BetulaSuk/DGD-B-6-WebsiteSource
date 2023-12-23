from asyncmy.cursors import DictCursor

from asyncio import sleep
from random import randint

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


def get_datetime(lst):
    for i in lst:
        if i[-1] == ')':
            time = i[14:-12]
            return time


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


async def readin_arxivdata(connection) -> None:
    for retry_times in range(1, 4):
        try:
            response = requests.get(TARGET_URL, headers=HEADERS)
            tree = etree.HTML(response.text.encode('utf-8'))
            temp = tree.xpath('//a[@title="Abstract"]/@href')
            break
        except requests.exceptions.RequestException:
            print(
                f">>> WARN: request sent to {TARGET_URL} failed, retrying...({retry_times})"
            )
            if retry_times >= 3:
                raise ConnectionError(
                    ">>> ERROR: give up getting arxivdata, check your settings."
                )

    print(f">>> successfully get from {TARGET_URL}: {response}")

    total = len(temp)
    result = []
    for i in range(total):
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
        time_temp = tree.xpath('//div[@class="submission-history"]/text()')
        dic['last_submit_time'] = get_datetime(time_temp)
        result.append(dic)
        print(f">>> GET[{i+1}/{total}]: {link}")
        await sleep(float(randint(50, 100)) / 100.0)

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
    print(">>> arxiv PDF metadata from arxiv reading complete!")
