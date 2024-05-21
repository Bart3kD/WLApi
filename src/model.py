from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer)
    name = Column(String, primary_key=True)


class Kind(Base):
    __tablename__ = 'kinds'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.name'), nullable=False)
    kind_id = Column(Integer, ForeignKey('kinds.id'), nullable=False)

    author = relationship("Author")
    kind = relationship("Kind")