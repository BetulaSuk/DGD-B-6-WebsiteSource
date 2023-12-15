from elasticsearch import Elasticsearch

from asyncmy import connect
from asyncmy.cursors import DictCursor

# es url
ES_HOSTS = [{"scheme": "http", "host": "elasticsearch", "port": 9200}]
ES_AUTH = ("elastic", "es23825")
PDFDATA_INDEX = 'pdfdata'

# 分词器和mapping的配置
PDFDATA_BODY = {
    "settings": {
        "analysis": {
            "analyzer": {
                "name_analyzer": {
                    "tokenizer": "whitespace",
                    "filter": "lowercase"
                },
                "key_analyzer": {
                    "tokenizer": "keyword",
                    "filter": "lowercase"
                }
            }
        }
    },
    "mappings": {
        "properties": {
            "title": {
                "type": "text",
                "analyzer": "english",
            },
            "paper_id": {
                "type": "keyword",
            },
            "web": {
                "type": "keyword",
            },
            "year": {
                "type": "long",
            },
            "abstract": {
                "type": "text",
                "analyzer": "english"
            },
            "author_name": {
                "type": "text",
                "analyzer": "name_analyzer"
            },
            "keywords": {
                "type": "text",
                "analyzer": "key_analyzer"
            },
            "venue": {
                "type": "text",
                "analyzer": "key_analyzer"
            }
        }
    }
}
