import requests
from lxml import etree

from asyncmy import connect
from asyncmy.cursors import DictCursor


async def run_creeper():
    conn = await connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='23825',
                         db='dgd_db',
                         charset='utf8')
    async with conn.cursor(cursor=DictCursor) as cs:
        await cs.execute()

