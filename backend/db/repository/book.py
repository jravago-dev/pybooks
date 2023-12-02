from sqlalchemy.orm import Session
from schemas.book import CreateBook
from db.models.book import Book


def create_new_book(book: CreateBook, db: Session):
    book = Book(
        title=book.title,
        isbn=book.isbn,
        author=book.author,
        is_active=True
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book
