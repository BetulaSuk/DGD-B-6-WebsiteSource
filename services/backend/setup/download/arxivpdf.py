import requests

from asyncmy import connect
from asyncmy.cursors import DictCursor

HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36 HBPC/11.0.8.301'
}


async def download_arxiv(mysql_conn):
    async with mysql_conn.cursor(cursor=DictCursor) as cs:
        await cs.execute('SELECT paper_id FROM arxivdata;')
        result = await cs.fetchall()

    result = [i['paper_id'] for i in result]

    total = len(result)
    for i in range(total):
        name = './data/static/Arxiv_PDF/' + result[i] + '.pdf'
        url = 'https://arxiv.org/pdf/' + result[i] + '.pdf'
        print(f">>> GET[{i+1}/{total}]: {url}")
        print(f"    TO: {name}")
        data = requests.get(url, headers=HEADERS)
        with open(name, 'wb') as f:
            f.write(data.content)

    print(">>> Download PDF from arxiv complete!")
