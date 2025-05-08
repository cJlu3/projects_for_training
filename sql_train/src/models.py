from datetime import datetime, timezone
from typing import Annotated
from sqlalchemy import MetaData, Table, Column, Integer, String, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm.attributes import create_proxied_attribute
from database import Base
import enum

intpk = Annotated[int, mapped_column(primary_key=True)]
created_at = Annotated[datetime, mapped_column(server_default=text("TIMEZONE('utc', now())"))]
updated_at = Annotated[datetime, mapped_column(
        server_default=text("TIMEZONE('utc', now())"), 
        onupdate=datetime.now(timezone.utc)
    )]


class WorkersOrm(Base):
    __tablename__: str = "workers"
    id: Mapped[intpk]
    username: Mapped[str]


class Workload(enum.Enum):
    parttime = "parttime"
    fulltime = "fulltime"

class ResumesOrm(Base):
    __tablename__: str = "resumes"
    id: Mapped[intpk]
    title: Mapped[str]
    compensation: Mapped[int | None]
    workload: Mapped[Workload]
    worker_id: Mapped[int] = mapped_column(ForeignKey("workers.id", ondelete="CASCADE"))
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
