from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import PdfData
from src.schemas.pdf_data import PdfOutSchema
from src.schemas.token import Status

async def get_by_id(pdf_id) -> PdfOutSchema:
    return await PdfOutSchema.from_queryset_single(PdfData.get(id=pdf_id))

