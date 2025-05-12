from typing import Optional
from database import Base, engine, session_factory
from models import BooksModel

def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def insert_data(books_list: list):
    with session_factory() as session:
        session.add_all(books_list)
        session.commit()

def create_book(title: str,
                author: str,
                year: int,
                is_taken: Optional[bool]) -> BooksModel:
    return BooksModel(title, author, year, is_taken)