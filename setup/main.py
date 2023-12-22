import asyncio
from asyncmy import connect
from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import BadRequestError

from download.arxivpdf import download_arxiv
from db.arxivdata import readin_arxivdata
from db.pdfdata import readin_pdfdata
from es.config import ES_HOSTS, ES_AUTH
from es.index import setup_pdfdata_index, setup_arxivdata_index


async def setup_db():
    for retry_times in range(1, 4):
        try:
            conn = await connect(host='localhost',
                                 port=3306,
                                 user='dgd',
                                 password='dgd23825',
                                 db='dgd_db',
                                 charset='utf8')
            break
        except ConnectionError:
            print(
                f">>> WARN: connect to mysql failed, retrying...({retry_times})"
            )
            if retry_times >= 3:
                raise ConnectionError(
                    ">>> ERROR: give up connecting to mysql server, check your settings."
                )

    print(">>> reading pdfdata...")
    await readin_pdfdata(conn)

    print(">>> getting arxivdata...")
    await readin_arxivdata(conn)

    print(">>> db setup successfully!")

    return conn


async def setup_es(db):
    async with AsyncElasticsearch(hosts=ES_HOSTS,
                                  basic_auth=ES_AUTH,
                                  verify_certs=False,
                                  max_retries=3) as aes:
        if not await aes.ping():
            print(
                ">>> ERROR: connection to ES server failed, check your settings."
            )
            return
        await setup_pdfdata_index(aes, db)
        await setup_arxivdata_index(aes, db)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    db_task = loop.create_task(setup_db())
    loop.run_until_complete(db_task)
    db_conn = db_task.result()

    loop.run_until_complete(
        asyncio.gather(setup_es(db_conn), download_arxiv(db_conn)))

    loop.close()
