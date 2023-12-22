from asyncmy.cursors import DictCursor

import json

PDF_METADATA_PATH = "./services/backend/data/100_PDF_MetaData.json"


async def replace_pdfdata(connection, pdfdata_lst) -> None:
    async with connection.cursor(cursor=DictCursor) as cs:
        await cs.executemany(
            """REPLACE INTO pdfdata (
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
                """, pdfdata_lst)
    await connection.commit()


async def readin_pdfdata(connection) -> None:
    with open(PDF_METADATA_PATH, encoding='utf8') as metadata_file:
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
    await replace_pdfdata(connection, data_lst)
    print(">>> 100 PDF metadata reading complete!")
