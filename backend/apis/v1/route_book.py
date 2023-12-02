from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.book import CreateBook, DisplayBookDetails, UpdateBook
from db.repository.book import (create_new_book, get_single_book, get_active_books,
                                get_all_books, update_book_details, set_book_as_inactive)
from typing import List

router = APIRouter()


@router.post("/", response_model=DisplayBookDetails, status_code=status.HTTP_201_CREATED)
async def create_book(book: CreateBook, db: Session = Depends(get_db)):
    book = create_new_book(book=book, db=db)
    return book


@router.put("/{isbn}", response_model=DisplayBookDetails)
async def update_book_details(isbn: str, book: UpdateBook, db: Session = Depends(get_db)):
    updated_book = update_book_details(isbn=isbn, book=book, db=db)
    if not updated_book:
        raise HTTPException(detail=f"ISBN {isbn} does not exist.", status_code=status.HTTP_400_BAD_REQUEST)
    return updated_book


@router.get("/{isbn}", response_model=DisplayBookDetails)
async def get_book(isbn: str, db: Session = Depends(get_db)):
    book = get_single_book(isbn=isbn, db=db)
    if not book:
        raise HTTPException(detail=f"ISBN {isbn} does not exist.", status_code=status.HTTP_400_BAD_REQUEST)
    return book


@router.get("/active", response_model=List[DisplayBookDetails], status_code=status.HTTP_200_OK)
async def get_active_books(db: Session = Depends(get_db)):
    active_books = get_active_books(db)
    return active_books


@router.get("/", response_model=List[DisplayBookDetails], status_code=status.HTTP_200_OK)
async def get_all_books(db: Session = Depends(get_db)):
    books = get_all_books(db)
    return books


@router.delete("/{isbn}")
async def set_book_as_inactive(isbn: str, db: Session = Depends(get_db), status_code=status.HTTP_200_OK):
    message = set_book_as_inactive(isbn, db)
    if message.get("error"):
        raise HTTPException(detail=message.get("error"), status_code=status.HTTP_400_BAD_REQUEST)
    return {"msg": message.get("msg")}
