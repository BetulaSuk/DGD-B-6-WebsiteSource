from elasticsearch import Elasticsearch
import pymysql

# 连接数据库
conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       db='DGD_web',
                       charset='utf8')
cursor = conn.cursor()
cursor.execute('SELECT * FROM pdf_data')
result = cursor.fetchall()

# 拆分数据
def create_body(data):
    dct = {}
    dct["title"] = data[7]
    dct["paper_id"] = data[8]
    # dct["page"] = [data[12], data[4]]
    dct["web"] = data[5]
    # dct["time"] = data[0]
    # dct["update_time"] = data[9]
    dct["year"] = data[2]
    dct["abstract"] = data[6]
    
    authorList = data[3][1:-3].split("\"], ")
    # dct["affiliation"] = authorList[0][17:].split("\", \"")
    dct["author_name"] = authorList[1][10:].split("\", \"")
    
    if data[15] == "[]":
        dct["keywords"] = []
    else:
        dct["keywords"] = data[15][2:-2].split("\', \'")
    
    dct["venue"] = data[10]
    return dct

# 分词器和mapping的配置
my_body = {
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

# 创建索引
es = Elasticsearch(["http://localhost:9200"])
print(es.ping())
es.indices.create(index='paper', body=my_body)

i = 0
for data in result:
    temp = create_body(data)
    es.index(index="paper", id=i, body=temp)
    i+=1

# es.indices.delete("paper")