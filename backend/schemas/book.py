from typing import Optional
from pydantic import BaseModel, root_validator, model_validator
from datetime import datetime


class CreateBook(BaseModel):
    title: str
    isbn: str
    author: str


class UpdateBook(CreateBook):
    pass


class DisplayBookDetails(BaseModel):
    title: str
    author: str
    isbn: str

    class Config():
        orm_mode = True
