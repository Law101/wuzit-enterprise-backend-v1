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
    
class User(AbstractBase):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    email = Column(String(200), unique=True, nullable=False)
    email_is_verified = Column(Boolean, nullable=False)
    password = Column(String(200), nullable=False)
    status = Column(String(20), nullable=False)
    level = Column(ForeignKey("user_levels.id"), nullable=False)
    date_deleted_utc = Column(DateTime(), onupdate=datetime.now, nullable=True)

    user_level = relationship("UserLevel")

class UserProfile(AbstractBase):
    __tablename__ = "user_profiles"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(ForeignKey("users.id"), nullable=False, unique=True)
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    phone_number = Column(String(20), nullable=True, unique=True)
    company = Column(String(50), nullable=True)
    user = relationship("User")


class UserLevel(AbstractBase):
    __tablename__ = "user_levels"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(50), nullable=False)
    description = Column(String(200), nullable=False)
    requirements = Column(JSONB(astext_type=Text()), nullable=False)


class UserAccess(AbstractBase):
    __tablename__ = "users_access"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    user_id = Column(ForeignKey("users.id"), nullable=False, unique=True)
    access_token = Column(String(200), nullable=False)
    access_key = Column(String(20), nullable=False)
    user = relationship("User")