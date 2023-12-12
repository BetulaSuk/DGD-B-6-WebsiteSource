from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from tortoise.contrib.fastapi import HTTPNotFoundError


router = APIRouter()

search_history = list()

@router.post("/api/search")
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