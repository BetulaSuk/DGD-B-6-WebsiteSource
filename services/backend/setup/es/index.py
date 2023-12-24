from asyncmy.cursors import DictCursor
from elasticsearch.exceptions import BadRequestError

from es.config import *


# 拆分数据
async def create_pdfbody(data):
    dct = {}
    dct["title"] = data["title"]
    dct["paper_id"] = data["paper_id"]
    dct["link"] = data["link"]
    dct["year"] = data["year"]
    dct["abstract"] = data["abstract"]
    authorList = data["author"][1:-3].split("\"], ")
    dct["author_name"] = authorList[1][10:].split("\", \"")

    if data["keywords"] == "[]":
        dct["keywords"] = []
    else:
        dct["keywords"] = data["keywords"][2:-2].split("\', \'")

    dct["journal"] = data["journal"]
    return dct


def create_arxivbody(data):
    dct = {}
    dct["title"] = data["title"]
    dct["paper_id"] = data["paper_id"]
    dct["link"] = data["link"]
    dct["abstract"] = data["abstract"]
    #修改
    authorList = data["author"][2:-2].split('\', \'')
    dct["author_name"] = authorList

    if data["keywords"] == "[]":
        dct["keywords"] = []
    else:
        dct["keywords"] = data["keywords"][2:-2].split("\', \'")
    return dct


async def setup_pdfdata_index(es, connection):
    # 连接数据库, 获取表单数据
    print("<Searcher> collecting data from db (pdfdata).")
    async with connection.cursor(cursor=DictCursor) as cs:
        await cs.execute(
            'SELECT title, paper_id, link, year, abstract, author, keywords, journal FROM pdfdata'
        )
        data_from_db = await cs.fetchall()
    # 创建索引
    print("<Searcher> start creating pdfdata index.")
    try:
        await es.indices.create(index=PDFDATA_INDEX, body=PDFDATA_BODY)
    except BadRequestError:
        print("<Searcher> pdfdata indices existed")

    for data in data_from_db:
        temp_body = await create_pdfbody(data)
        await es.index(index=PDFDATA_INDEX,
                       id=data["paper_id"],
                       body=temp_body)

    print("<Searcher> created pdfdata index successfully.")


async def setup_arxivdata_index(es, connection):
    # 连接数据库, 获取表单数据
    print("<Searcher> collecting data from db (arxivdata).")
    async with connection.cursor(cursor=DictCursor) as cs:
        await cs.execute(
            'SELECT title, paper_id, link, abstract, author, keywords FROM arxivdata'
        )
        data_from_db = await cs.fetchall()
    # 创建索引
    print("<Searcher> start creating arxivdata index.")
    try:
        await es.indices.create(index=ARXIVDATA_INDEX, body=ARXIVDATA_BODY)
    except BadRequestError:
        print("<Searcher> arxivdata indices existed")

    for data in data_from_db:
        temp_body = create_arxivbody(data)
        await es.index(index=ARXIVDATA_INDEX,
                       id=data["paper_id"],
                       body=temp_body)

    print("<Searcher> created arxivdata index successfully.")
