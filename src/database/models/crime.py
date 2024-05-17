from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    Numeric,
    String,
    Table,
    Text,
    text,
)
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from src.root.database import DeclarativeBase


class AbstractBase(DeclarativeBase):
    __abstract__ = True
    date_created_utc = Column(DateTime(), default=datetime.now)
    date_updated_utc = Column(DateTime(), onupdate=datetime.now)

    def as_dict(self):
        return {field.name: getattr(self, field.name) for field in self.__table__.c}