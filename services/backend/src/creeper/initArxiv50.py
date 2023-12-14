from asyncmy import connect
from asyncmy.cursors import DictCursor

import requests
from lxml import etree

target_url = "https://arxiv.org/list/math.NT/pastweek?show=53"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'}
template_dic = {
    'date':'0000-01-01T00:00:00',
    'conference':'',
    'year':-1,
    'author':[],
    'last_page':-1,
    'link':'',
    'abstract':'',
    'title':'',
    'paper_id':'',
    'update_time':'0000-01-01T00:00:00',
    'journal':'',
    'issn':'',
    'first_page':-1,
    'publisher':'',
    'doi':'',
    'keywords':''
}

def setup_creeper(app):
    @app.on_event("startup")
    async def run_creeper():
        conn = await connect(host='db',
                             port=3306,
                             user='dgd',
                             password='dgd23825',
                             db='dgd_db',
                             charset='utf8')
        title = []
        result = []
        response = requests.get(target_url, headers=headers)
        tree = etree.HTML(response.text.encode('utf-8'))
        temp = tree.xpath('//a[@title="Abstract"]/@href')

        for i in range(0, len(temp)):
            dic = template_dic.copy()
            dic['paper_id']=temp[i][5:]
            url = 'https://arxiv.org'+temp[i]
            dic['link']=url
            sub_response = requests.get(url,headers=headers)
            tree = etree.HTML(sub_response.text.encode('utf-8'))
            sub_temp = tree.xpath('//blockquote[@class="abstract mathjax"]/text()')
            dic['abstract'] = sub_temp[1][:-6]
            au_temp = tree.xpath('//div[@class="authors"]//a/text()')
            dic['author'] = au_temp
            ti_temp = tree.xpath('//h1[@class="title mathjax"]/text()')
            dic['title']=ti_temp[0]
            result.append(dic)
        
        lst = []

        for i in result:
            sub_lst = []
            sub_lst.append(i['date'])
            sub_lst.append(i['conference'])
            sub_lst.append(i['year'])
            sub_lst.append(str(i['author']))
            sub_lst.append(i['last_page'])
            sub_lst.append(i['link'])
            sub_lst.append(i['abstract'])
            sub_lst.append(i['title'])
            sub_lst.append(i['paper_id'])
            sub_lst.append(i['update_time'])
            sub_lst.append(i['journal'])
            sub_lst.append(i['issn'])
            sub_lst.append(i['first_page'])
            sub_lst.append(i['publisher'])
            sub_lst.append(i['doi'])
            sub_lst.append(str(i['keywords']))
            lst.append(sub_lst)

        async with conn.cursor(cursor=DictCursor) as cs:
            await cs.executemany("""
                                 REPLACE INTO pdfdata (
                                 date,
                                 conference,
                                 year,
                                 author,
                                 last_page,
                                 link,
                                 abstract,
                                 title,
                                 paper_id,
                                 update_time,
                                 journal,
                                 issn,
                                 first_page,
                                 publisher,
                                 doi,
                                 keywords)
                                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                 ,lst)
        await conn.commit()

