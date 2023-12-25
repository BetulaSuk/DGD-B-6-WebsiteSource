from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.pdf_data as crud
from src.schemas.pdf_data import PdfInSchema, PdfOutSchema
from src.schemas.token import Status

router = APIRouter()


@router.get(
    "/pdf/id",
    response_model=PdfOutSchema,
)
async def get_pdf(pdf_id: str) -> PdfOutSchema:
    try:
        return await crud.get_by_id(pdf_id)
    except DoesNotExist:
        raise HTTPException(status_code=404, detail="Pdf does not exist")
