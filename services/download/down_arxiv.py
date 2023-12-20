import requests

from asyncmy import connect
from asyncmy.cursors import DictCursor

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'
}


async def download_arxiv():
    mysql_conn = await connect(host='localhost',
                               port=3306,
                               user='dgd',
                               password='dgd23825',
                               db='dgd_db',
                               charset='utf8')
    async with mysql_conn.cursor(cursor=DictCursor) as cs:
        await cs.execute('SELECT paper_id FROM arxivdata;')
        result = await cs.fetchall()

    for i in result:
        name = '../backend/data/static/Arxiv_PDF/' + i['paper_id'] + '.pdf'
        url = 'https://arxiv.org/pdf/' + i['paper_id'] + '.pdf'
        print(name)
        print(url)
        dowlimg = requests.get(url, headers=HEADERS)
        with open(name, 'wb') as f:
            f.write(dowlimg.content)


if __name__ == '__main__':
    from asyncio import run
    run(download_arxiv())
