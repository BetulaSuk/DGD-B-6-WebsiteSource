from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist, IntegrityError

from src.database.models import Notes
from src.schemas.notes import NoteOutSchema
from src.schemas.token import Status  # NEW


async def get_notes(current_user):
    usr_notes = Notes.filter(author_id=current_user.id)
    return await NoteOutSchema.from_queryset(usr_notes)


async def get_note(note_id) -> NoteOutSchema:
    return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))


async def create_note(note, current_user) -> NoteOutSchema:
    note_dict = note.dict(exclude_unset=True)
    note_dict["author_id"] = current_user.id
    try:
        note_obj = await Notes.create(**note_dict)
    except IntegrityError:
        raise HTTPException(status_code=400, detail="Wrong pdf_id")
    return await NoteOutSchema.from_tortoise_orm(note_obj)


async def update_note(note_id, note, current_user) -> NoteOutSchema:
    try:
        db_note = await NoteOutSchema.from_queryset_single(
            Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404,
                            detail=f"Note {note_id} not found")

    if db_note.author.id == current_user.id:
        await Notes.filter(id=note_id).update(**note.dict(exclude_unset=True))
        return await NoteOutSchema.from_queryset_single(Notes.get(id=note_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_note(note_id, current_user) -> Status:  # UPDATED
    try:
        db_note = await NoteOutSchema.from_queryset_single(
            Notes.get(id=note_id))
    except DoesNotExist:
        raise HTTPException(status_code=404,
                            detail=f"Note {note_id} not found")

    if db_note.author.id == current_user.id:
        deleted_count = await Notes.filter(id=note_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404,
                                detail=f"Note {note_id} not found")
        return Status(message=f"Deleted note {note_id}")  # UPDATED

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")
