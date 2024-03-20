from typing import List
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from db.models import Note
from api.schemas import GetNote, UpdateNote


router = APIRouter()


@router.post("/notes", response_model=GetNote, status_code=status.HTTP_201_CREATED)
def add_note(note: UpdateNote, db: Session = Depends(get_db)):
    note_record = Note(**note.dict())
    db.add(note_record)
    db.commit()
    db.refresh(note_record)
    return note_record


@router.get("/notes", response_model=List[GetNote])
def get_notes(db: Session = Depends(get_db)):
    note_records = db.query(Note).all()
    return note_records


@router.get("/notes/{note_id}", response_model=GetNote)
def get_note(note_id: int, db: Session = Depends(get_db)):
    note_record = db.query(Note).filter(Note.id == note_id).first()
    if not note_record:
        raise HTTPException(
            detail=f"Note with id {note_id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    return note_record


@router.put("/notes/{note_id}", response_model=GetNote)
def update_note(note_id: int, note: UpdateNote, db: Session = Depends(get_db)):
    note_record = db.query(Note).filter(Note.id == note_id).first()
    if not note_record:
        raise HTTPException(
            detail=f"Note with id {note_id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    note_record.text = note.text
    db.add(note_record)
    db.commit()
    return note_record


@router.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    note_record = db.query(Note).filter(Note.id == note_id).first()
    if not note_record:
        raise HTTPException(
            detail=f"Note with id {note_id} does not exist.",
            status_code=status.HTTP_404_NOT_FOUND,
        )
    db.delete(note_record)
    db.commit()
    return {"status": 0}
