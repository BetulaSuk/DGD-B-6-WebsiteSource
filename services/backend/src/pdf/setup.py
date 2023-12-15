from asyncmy import connect

from src.pdf.metadata.pdfdata import check_pdfdata, readin_pdfdata
from src.pdf.metadata.arxivdata import check_arxivdata, readin_arxivdata
from src.pdf.searcher.searcher import Searcher


def setup_pdfdata(app):

    @app.on_event("startup")
    async def init_pdfdata():
        mysql_conn = await connect(host='db',
                                   port=3306,
                                   user='dgd',
                                   password='dgd23825',
                                   db='dgd_db',
                                   charset='utf8')
        exist_pdfdata = await check_pdfdata(mysql_conn)
        exist_arxivdata = await check_arxivdata(mysql_conn)

        if not exist_pdfdata:
            await readin_pdfdata(mysql_conn)
        if not exist_arxivdata:
            await readin_arxivdata(mysql_conn)

        if not Searcher.pdfdata_index_exist:
            seacher = Searcher()
            await seacher.setup_pdfdata_index(mysql_conn)
