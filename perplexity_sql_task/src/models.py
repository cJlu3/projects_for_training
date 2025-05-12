from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class BooksModel(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    year: Mapped[int]
    is_taken: Mapped[bool] = mapped_column(default=False)