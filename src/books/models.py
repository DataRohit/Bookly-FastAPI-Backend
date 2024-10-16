import uuid
from datetime import datetime

import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, SQLModel


class BookCategory(SQLModel, table=True):
    __tablename__ = "book_categories"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    category: str = Field(sa_column=Column(pg.VARCHAR, nullable=False, unique=True))
    description: str = Field(sa_column=Column(pg.TEXT, nullable=False))
    created_by: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, default=uuid.uuid4)
    )
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now
        )
    )


class BookGenre(SQLModel, table=True):
    __tablename__ = "book_genres"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    genre: str = Field(sa_column=Column(pg.VARCHAR, nullable=False, unique=True))
    description: str = Field(sa_column=Column(pg.TEXT, nullable=False))
    created_by: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, default=uuid.uuid4)
    )
    created_at: datetime = Field(
        sa_column=Column(pg.TIMESTAMP, nullable=False, default=datetime.now)
    )
    updated_at: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP, nullable=False, default=datetime.now, onupdate=datetime.now
        )
    )


class Book(SQLModel, table=True):
    __tablename__ = "books"

    uid: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False, primary_key=True, default=uuid.uuid4)
    )
    title: str = Field(sa_column=Column(pg.VARCHAR, nullable=False))
    description: str = Field(sa_column=Column(pg.TEXT, nullable=False))
    isbn: str = Field(sa_column=Column(pg.VARCHAR, nullable=False, unique=True))
    published_date: datetime = Field(sa_column=Column(pg.DATE, nullable=False))
    page_count: int = Field(sa_column=Column(pg.INTEGER, nullable=False))
    authors: list[uuid.UUID] = Field(
        sa_column=Column(pg.ARRAY(pg.UUID), nullable=False)
    )
    categories: list[uuid.UUID] = Field(
        sa_column=Column(pg.ARRAY(pg.UUID), nullable=False)
    )
    genres: list[uuid.UUID] = Field(sa_column=Column(pg.ARRAY(pg.UUID), nullable=False))
    images: list[uuid.UUID] = Field(sa_column=Column(pg.ARRAY(pg.UUID), nullable=False))
