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


search_history = list()


@router.post("/search/history")
async def get_search_text(term: dict):
    search_term = term.get("term", "")
    if search_term:
        # Add the search term to the history
        search_history.append(search_term)

    #非常简陋的删除历史记录，之后应该做个按钮TODO
    if search_term == "clear":
        search_history.clear()

    # Limit search history to the last 5 entries
    #在这里截取不知道为什么会使得search_history编程unbounded
    #所以改为在return中截取！！
    #search_history = search_history[-5:]

    return JSONResponse(content={"searchHistory": search_history[-5:]})
