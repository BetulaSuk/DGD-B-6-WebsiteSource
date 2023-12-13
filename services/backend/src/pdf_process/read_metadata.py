import json

from asyncmy import connect
from asyncmy.cursors import DictCursor


async def readin_pdf_metadata():
    conn = await connect(host='127.0.0.1',
                         port=3306,
                         user='root',
                         passwd='23825',
                         db='dgd_db',
                         charset='utf8')
    with open("./data/100_PDF_MetaData.json", encoding='utf8') as metadata_file:
        data = json.load(metadata_file)
        data_lst = []
        for key in data.keys():
            sub_lst = []
            sub_data = data[key]
            sub_lst.append(sub_data['date'])
            sub_lst.append(sub_data['conference'])
            sub_lst.append(sub_data['year'])
            sub_lst.append(json.dumps(sub_data['author']))
            sub_lst.append(sub_data['last_page'])
            sub_lst.append(sub_data['link'])
            sub_lst.append(sub_data['abstract'])
            sub_lst.append(sub_data['title'])
            sub_lst.append(sub_data['paper_id'])
            sub_lst.append(sub_data['update_time'])
            sub_lst.append(sub_data['journal'])
            sub_lst.append(sub_data['issn'])
            sub_lst.append(sub_data['first_page'])
            sub_lst.append(sub_data['publisher'])
            sub_lst.append(sub_data['doi'])
            sub_lst.append(str(sub_data['keywords']))
            data_lst.append(sub_lst)
    async with conn.cursor(cursor=DictCursor) as cs:
        await cs.execute("""CREATE TABLE IF NOT EXISTS `PdfData`(
                         `date`datetime NOT NULL,
                         `conference`varchar(255) DEFAULT NULL,
                         `year`int(11) DEFAULT NULL,
                         `author` text DEFAULT NULL,
                         `last_page`int(11) DEFAULT NULL,
                         `link`varchar(255) DEFAULT NULL,
                         `abstract`longtext DEFAULT NULL,
                         `title`text DEFAULT NULL,
                         `paper_id`varchar(255) NOT NULL,
                         `update_time`datetime DEFAULT NULL,
                         `journal`varchar(255) DEFAULT NULL,
                         `issn`varchar(255) DEFAULT NULL,
                         `first_page`int(11) DEFAULT NULL,
                         `publisher`varchar(255) DEFAULT NULL,
                         `doi`varchar(255) DEFAULT NULL,
                         `keywords`varchar(255) DEFAULT NULL,
                         UNIQUE KEY`paper_id`(`paper_id`)USING BTREE,
                         KEY`journal`(`journal`)USING BTREE
                         )
                         ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 collate utf8mb4_general_ci""")
        cs.executemany("""REPLACE INTO PdfData (
                       date,
                       conference,
                       year,
                       author,
                       last_page,
                       link,
                       abstract,
                       title,
                       paper_id,
                       update_time,
                       journal,
                       issn,
                       first_page,
                       publisher,
                       doi,
                       keywords) 
                       VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                       """, data_lst)
    conn.commit()
        

