from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.book import CreateBook, DisplayBookDetails
from db.repository.book import create_new_book

router = APIRouter()


@router.post("/", response_model=DisplayBookDetails, status_code=status.HTTP_201_CREATED)
async def create_book(book: CreateBook, db: Session = Depends(get_db)):
    book = create_new_book(book=book, db=db)
    return book
