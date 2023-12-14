from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import PdfData

PdfInSchema = pydantic_model_creator(
    PdfData, name="PdfIn", exclude_readonly=True
)

PdfOutSchema = pydantic_model_creator(
    PdfData, name="PdfOut", exclude=[]
)


