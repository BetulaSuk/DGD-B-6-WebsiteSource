import requests
from lxml import etree

TARGET_URL = "https://arxiv.org/abs/2312.14144"
HEADERS = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
TEMPLATE_DICT = {
    'paper_id': '',
    'title': '',
    'author': [],
    'link': '',
    'abstract': '',
    'keywords': '',
    'last_submit_time': ''
}

respon = requests.get(TARGET_URL, headers=HEADERS)

print(respon)

tree = etree.HTML(respon.text.encode('utf-8'))

temp = tree.xpath('//a[@title="Abstract"]/@href')

print(temp)
