from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.pdf_data as crud
from src.schemas.pdf_data import PdfInSchema, PdfOutSchema
from src.schemas.token import Status

import os

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


@router.get(
    "/pdf/csv/{paper_id}"
)
async def get_pdf_csv(paper_id: str):
    try:
        files = os.listdir("data/static/100_PDF_results/" + paper_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Wrong paper_id")
    return files


@router.get(
    "/pdf/img/{paper_id}"
)
async def get_pdf_img(paper_id: str):
    try:
        files = os.listdir("data/static/100_PDF_images/" + paper_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Wrong paper_id")
    return files
