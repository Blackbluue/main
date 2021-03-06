#!/usr/bin/env python3
"""media module."""
from sqlalchemy import Column, Integer, String, Date, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Anime(Base):
    """Anime table."""

    __tablename__ = "Anime"
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    director = Column(String(32))
    release_date = Column(Date)
    synopsis = Column(Text)

    def __init__(self, title, director=None, release_date=None, synopsis=None):
        """Create a record."""
        self.title = title
        self.director = director
        self.release_date = release_date
        self.synopsis = synopsis


class Manga(Base):
    """Manga table."""

    __tablename__ = "Manga"
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    author = Column(String(32))
    release_date = Column(Date)
    synopsis = Column(Text)

    def __init__(self, title, author=None, release_date=None, synopsis=None):
        """Create a record."""
        self.title = title
        self.author = author
        self.release_date = release_date
        self.synopsis = synopsis


class Movie(Base):
    """Movie table."""

    __tablename__ = "Movie"
    id = Column(Integer, primary_key=True)
    title = Column(String(32), nullable=False)
    director = Column(String(32))
    release_date = Column(Date)
    synopsis = Column(Text)

    def __init__(self, title, director=None, release_date=None, synopsis=None):
        """Create a record."""
        self.title = title
        self.director = director
        self.release_date = release_date
        self.synopsis = synopsis
