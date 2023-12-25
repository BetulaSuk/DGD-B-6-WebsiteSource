from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from fastapi.staticfiles import StaticFiles

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users, notes, pdf_data, search

app = FastAPI()

app.mount("/static", StaticFiles(directory="data/static"), name="static")

#Changed!!!
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(notes.router)
app.include_router(pdf_data.router)
app.include_router(search.router)

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)


@app.get("/")
def home():
    return "Hello, World!"
