from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

from src.pdf.pdfdata.read_metadata import readin_pdf_metadata
from src.pdf.pdfdata.creeper.initArxiv50 import setup_creeper

from src.searcher.init_es import setup_es

# import searcher.searcher

# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

from src.routes import users, notes, pdf_data, search

app = FastAPI()

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

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)
readin_pdf_metadata(app)
setup_creeper(app)
setup_es(app)


@app.get("/")
def home():
    return "Hello, World!"
