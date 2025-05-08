from sqlalchemy import create_engine, String
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from config import settings

engine = create_engine(
    url=settings.database_url,
    echo = True
)

session_factory = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
