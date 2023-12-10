from elasticsearch import Elasticsearch
import json

# json格式化显示函数
def json_print(string):
    print(json.dumps(string, sort_keys=True, indent=4, separators=(',', ':')))
    return

class Searcher:
    def __init__(self) -> None:
        self.es = Elasticsearch()

    def search(self, method, key):
        #若输入的关键词中有空格则自动进行短语查询
        if " " in key:
            match = "match_phrase"
        else:
            match = "match"
    
        q = {
            "_source": [
            "title",
            "paper_id",
            "web",
            "year",
            "abstract",
            "author_name",
            "keywords",
            "venue"
            ],
            "query": {
                "script_score": {
                "query": {
                    match: {method: key}
                },
                "script": {
                    "source": "_score * 100 + (doc['year'].value/100)"
                }
                }
            }
        }
        result = self.es.search(index="paper", body=q)
        if result['hits']['hits'] == []:
            print("Sorry, no match result.")
            return None
        # json_print(result['hits']['hits'])
        return result['hits']['hits']
    
    # 以list(dict)格式得到method:key搜索结果中的信息
    # list[i]包含"title","paper_id","web","year","abstracct","author_name","keywords","venue"等信息
    def get_info(self, method, key):
        lst = []
        
        for i in self.search(method, key):
            lst.append(i["_source"])
        
        return lst



# 尝试搜索并输出结果
if __name__ == '__main__':
    se = Searcher()
    # result = se.search('keywords','brazil')
    l = se.get_info('keywords','brazil')
    for i in l:
        print(i)