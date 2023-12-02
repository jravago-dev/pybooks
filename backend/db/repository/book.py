from sqlalchemy.orm import Session
from schemas.book import CreateBook, UpdateBook
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


def get_single_book(isbn: str, db: Session):
    book = db.query(Book).filter(Book.isbn == isbn).first()
    return book


def get_active_books(db: Session):
    active_books = db.query(Book).filter(Book.is_active).all()
    return active_books


def get_all_books(db: Session):
    books = db.query(Book).filter().all()
    print(books)
    return books


def update_book_details(isbn: str, book: UpdateBook, db: Session):
    existing_book = db.query(Book).filter(Book.isbn == isbn).first()
    if not existing_book:
        return

    existing_book.title = book.title
    existing_book.author = book.author
    existing_book.is_active = book.is_active

    db.add(existing_book)
    db.commit()
    return existing_book


def set_book_as_inactive(isbn: str, db: Session):
    existing_book = db.query(Book).filter(Book.isbn == isbn).first()
    if not existing_book:
        return

    existing_book.is_active = False
    db.add(existing_book)
    db.commit()
    return {"msg": f"ISBN {isbn} has been deleted."}
