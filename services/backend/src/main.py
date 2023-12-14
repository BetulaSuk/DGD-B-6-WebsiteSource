from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise

from src.database.register import register_tortoise
from src.database.config import TORTOISE_ORM

from src.pdf_process.read_metadata import readin_pdf_metadata
from src.creeper.initArxiv50 import setup_creeper

# import searcher.searcher


# enable schemas to read relationship between models
Tortoise.init_models(["src.database.models"], "models")

"""
import 'from src.routes import users, notes' must be after 'Tortoise.init_models'
why?
https://stackoverflow.com/questions/65531387/tortoise-orm-for-python-no-returns-relations-of-entities-pyndantic-fastapi
"""
from src.routes import users, notes, pdf_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8080"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(users.router)
app.include_router(notes.router)
app.include_router(pdf_data.router)

register_tortoise(app, config=TORTOISE_ORM, generate_schemas=False)

readin_pdf_metadata(app)
setup_creeper(app)

@app.get("/")
def home():
    return "Hello, World!"
