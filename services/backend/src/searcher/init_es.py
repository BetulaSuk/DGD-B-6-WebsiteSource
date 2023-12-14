from elasticsearch import Elasticsearch

from asyncmy import connect
from asyncmy.cursors import DictCursor

# es url
es_config = [{
    "scheme":"http",
    "host":"elasticsearch",
    "port": 9200
}]
static_paper_index = 'static_paper'

# 分词器和mapping的配置
pdfdata_body = {
    "settings":{
        "analysis":{
            "analyzer":{
                "name_analyzer":{
                    "tokenizer" : "whitespace",
                    "filter" : "lowercase"
                },
                "key_analyzer":{
                    "tokenizer" : "keyword",
                    "filter" : "lowercase"
                }
            }
        }
    },
    "mappings" : {
      "properties" : {
        "title" : {
            "type" : "text",
            "analyzer":"english",
        },
        "paper_id" : {
            "type" : "keyword",
        },
        "web" : {
            "type" : "keyword",
        },
        # "time":{
        #     "type" : "date",
        # },
        # "update_time":{
        #     "type" : "date",
        # },
        "year":{
            "type" : "long",
        },
        "abstract" : {
            "type" : "text",
            "analyzer" : "english"
        },
        # "affiliation" : {
        #     "type" : "text",
        #     "analyzer" : "name_analyzer"
        # },
        "author_name" : {
            "type" : "text",
            "analyzer" : "name_analyzer"
        },
        "keywords" : {
            "type" : "text",
            "analyzer" : "key_analyzer"
        },
        "venue" : {
            "type" : "text",
            "analyzer" : "key_analyzer"
        }
      }
    }
}


# 拆分数据
def create_body(data):
    dct = {}
    dct["title"] = data[0]
    dct["paper_id"] = data[1]
    # dct["page"] = [data[12], data[4]]
    dct["web"] = data[2]
    # dct["time"] = data[0]
    # dct["update_time"] = data[9]
    dct["year"] = data[3]
    dct["abstract"] = data[4]
    
    authorList = data[5][1:-3].split("\"], ")
    # dct["affiliation"] = authorList[0][17:].split("\", \"")
    dct["author_name"] = authorList[1][10:].split("\", \"")
    
    if data[6] == "[]":
        dct["keywords"] = []
    else:
        dct["keywords"] = data[6][2:-2].split("\', \'")
    
    dct["venue"] = data[7]
    return dct

def setup_es(app):
    @app.on_event("startup")
    async def init_es():
        # 连接es, 如果静态索引以及建好就跳过
        es = Elasticsearch(es_config, verify_certs=False)
        print(es.ping())
        if es.indices.exists(index=static_paper_index):
            return
        # 连接数据库, 获取表单数据
        conn = await connect(host='db',
                             port=3306,
                             user='dgd',
                             password='dgd23825',
                             db='dgd_db',
                             charset='utf8')
        async with conn.cursor(cursor=DictCursor) as cs:
            await cs.execute('SELECT title, paper_id, link, year, abstract, author, keywords, venue FROM pdfdata')
            data_from_db = await cs.fetchall()
        # 创建索引
        es.indices.create(index=static_paper_index, body=pdfdata_body)

        i = 0
        for data in data_from_db:
            temp_body = create_body(data)
            es.index(index=static_paper_index, id=i, body=temp_body)
            i+=1

