from elasticsearch import Elasticsearch
import json

from src.pdf.searcher.config import *


# json格式化显示函数
def json_print(string):
    print(json.dumps(string, sort_keys=True, indent=4, separators=(',', ':')))
    return


# 拆分数据
def create_body(data):
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


class Searcher:
    pdfdata_index_exist = False

    def __init__(self, es_instance=None) -> None:
        if not es_instance:
            self.es = Elasticsearch(hosts=ES_HOSTS,
                                    basic_auth=ES_AUTH,
                                    verify_certs=False)
        else:
            self.es = es_instance

        if self.es.indices.exists(index=PDFDATA_INDEX):
            print("<Searcher:init> pdfdata index exist")
            Searcher.pdfdata_index_exist = True

    async def setup_pdfdata_index(self, connection):
        # 避免重复创建索引
        if Searcher.pdfdata_index_exist:
            print("<Searcher> pdfdata index exist, giveup setup pdfdata.")
            return
        # 连接数据库, 获取表单数据
        print("<Searcher> collecting data from db (pdfdata).")
        async with connection.cursor(cursor=DictCursor) as cs:
            await cs.execute(
                'SELECT title, paper_id, link, year, abstract, author, keywords, journal, id FROM pdfdata'
            )
            data_from_db = await cs.fetchall()
        # 创建索引
        print("<Searcher> start creating pdfdata index.")
        self.es.indices.create(index=PDFDATA_INDEX, body=PDFDATA_BODY)

        for data in data_from_db:
            temp_body = create_body(data)
            self.es.index(index=PDFDATA_INDEX, id=data["id"], body=temp_body)

        Searcher.pdfdata_index_exist = True
        print("<Searcher> created pdfdata index successfully.")

    def search_pdfdata(self, method, key: str):
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
        result = self.es.search(index=PDFDATA_INDEX, body=q)
        if result['hits']['hits'] == []:
            print(
                f"<Searcher> Sorry, no match result. data type: pdfdata; method: {method}; key: {key}."
            )
            return ""
        # json_print(result['hits']['hits'])
        return result['hits']['hits']

    # 以list(dict)格式得到method:key搜索结果中的信息
    # list[i]包含"title","paper_id","link","year","abstracct","author_name","keywords","journal"等信息
    def get_info_pdfdata(self, method, key):
        result = self.search_pdfdata(method, key)
        if not result:
            return []

        lst = []
        for i in self.search_pdfdata(method, key):
            lst.append(i["_source"])

        return lst
