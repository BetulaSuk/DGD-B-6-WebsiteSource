from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from elasticsearch import NotFoundError

from src.pdf.searcher.searcher import Searcher

from pydantic import BaseModel

router = APIRouter()


class Item(BaseModel):
    keyword: str
    data_type: str
    method: str


@router.post("/search/", response_class=JSONResponse)
async def es_search(item: Item):
    try:
        if item.data_type == "pdf_data":
            es_searcher = Searcher()
            result = es_searcher.get_info_pdfdata(item.method, item.keyword)
            return JSONResponse(content=result)
        elif item.data_type == "arxiv_data":
            es_searcher = Searcher()
            result = es_searcher.get_info_arxivdata(item.method, item.keyword)
            return JSONResponse(content=result)
    except NotFoundError:
        raise HTTPException(status_code=404,
                            detail=f"No result in {item.data_type}")
