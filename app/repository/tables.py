from typing import TypeAlias

from sqlalchemy import Column, Integer, Unicode

from app.repository.database import db

DeclarativeBase: TypeAlias = db.Model


class AccountModel(DeclarativeBase):
    __tablename__ = "accounts"
    id = Column(Integer(), primary_key=True)
    nickname = Column(Unicode(), default="anonymous")
