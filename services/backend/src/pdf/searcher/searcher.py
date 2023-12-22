<<<<<<< HEAD
from elasticsearch import Elasticsearch, BadRequestError
=======
from elasticsearch import AsyncElasticsearch
import asyncio
>>>>>>> 2b5be08 (split setup part, reconstructed)
import json

from src.pdf.searcher.config import *


class Searcher:
    pdfdata_index_exist = False
    arxivdata_index_exist = False

    def __init__(self, es_instance: AsyncElasticsearch = None):
        if not es_instance:
            for retry_times in range(1, 4):
                try:
                    self.es = AsyncElasticsearch(hosts=ES_HOSTS,
                                                 basic_auth=ES_AUTH,
                                                 verify_certs=False)
                except ConnectionError:
                    print(
                        f"<Searcher:init> Client init failed, retrying...({retry_times})"
                    )
                    continue
                else:
                    print("<Searcher:init> Client init successfully")
                    break
            raise ConnectionError("<Searcher:init> retried 3 times, give up!")
        else:
            self.es = es_instance

    async def __aenter__(self, es_instance: AsyncElasticsearch = None):
        if await self.es.indices.exists(index=PDFDATA_INDEX):
            print("<Searcher:init> pdfdata index exist")
            Searcher.pdfdata_index_exist = True
        if await self.es.indices.exists(index=ARXIVDATA_INDEX):
            print("<Searcher:init> arxivdata index exist")
            Searcher.arxivdata_index_exist = True
        return self

    async def __aexit__(self, *_):
        await self.es.close()

<<<<<<< HEAD
        for data in data_from_db:
            temp_body = create_pdfbody(data)
            self.es.index(index=PDFDATA_INDEX, id=data["id"], body=temp_body)

        Searcher.pdfdata_index_exist = True
        print("<Searcher> created pdfdata index successfully.")

    async def setup_arxivdata_index(self, connection):
        # 避免重复创建索引
        if Searcher.arxivdata_index_exist:
            print("<Searcher> arxivdata index exist, giveup setup arxivdata.")
            return
        # 连接数据库, 获取表单数据
        print("<Searcher> collecting data from db (arxivdata).")
        async with connection.cursor(cursor=DictCursor) as cs:
            await cs.execute(
                'SELECT title, paper_id, link, abstract, author, keywords, id FROM arxivdata'
            )
            data_from_db = await cs.fetchall()
        # 创建索引
        print("<Searcher> start creating arxivdata index.")
        # try:
        self.es.indices.create(index=ARXIVDATA_INDEX, body=ARXIVDATA_BODY)
        # except BadRequestError:
        # pass

        for data in data_from_db:
            temp_body = create_arxivbody(data)
            self.es.index(index=ARXIVDATA_INDEX, id=data["id"], body=temp_body)

        Searcher.arxivdata_index_exist = True
        print("<Searcher> created arxivdata index successfully.")

    def search_pdfdata(self, method, key: str):
=======
    async def search_pdfdata(self, method, key: str):
>>>>>>> 2b5be08 (split setup part, reconstructed)
        #若输入的关键词中有空格则自动进行短语查询
        if " " in key:
            match = "match_phrase"
        else:
            match = "match"

        q = {
            "_source": [
                "title", "paper_id", "link", "year", "abstract", "author_name",
                "keywords", "journal"
            ],
            "query": {
                "script_score": {
                    "query": {
                        match: {
                            method: key
                        }
                    },
                    "script": {
                        "source": "_score * 100 + (doc['year'].value/100)"
                    }
                }
            }
        }
        result = await self.es.search(index=PDFDATA_INDEX, body=q)
        if result['hits']['hits'] == []:
            print(
                f"<Searcher> Sorry, no match result. data type: pdfdata; method: {method}; key: {key}."
            )
            return ""
        # json_print(result['hits']['hits'])
        return result['hits']['hits']

    # 以list(dict)格式得到method:key搜索结果中的信息
    # list[i]包含"title","paper_id","link","year","abstracct","author_name","keywords","journal"等信息
    async def get_info_pdfdata(self, method, key):
        print(f"<Searcher> pdfdata method: {method}; key: {key}")
        lst = []
        result = await self.search_pdfdata(method, key)
        for i in result:
            lst.append(i["_source"])
            print(f"    - {i['_source']['paper_id']}")

        return lst

    async def search_arxivdata(self, method, key: str):
        #若输入的关键词中有空格则自动进行短语查询
        if " " in key:
            match = "match_phrase"
        else:
            match = "match"

        q = {
            "_source": [
                "author_name", "link", "abstract", "title", "paper_id",
                "keywords"
            ],
            "query": {
                match: {
                    method: key
                }
            }
        }
        result = await self.es.search(index=ARXIVDATA_INDEX, body=q)
        if result['hits']['hits'] == []:
            print(
                f"<Searcher> Sorry, no match result. data type: arxivdata; method: {method}; key: {key}."
            )
            return ""
        # json_print(result['hits']['hits'])
        return result['hits']['hits']

    # 以list(dict)格式得到method:key搜索结果中的信息
    # list[i]包含"title","paper_id","link","year","abstracct","author_name","keywords","journal"等信息
    async def get_info_arxivdata(self, method, key):
        print(f"<Searcher> arxivdata method: {method}; key: {key}")
        lst = []
        result = await self.search_arxivdata(method, key)
        for i in result:
            lst.append(i["_source"])
            print(f"    - {i['_source']['paper_id']}")

        return lst
