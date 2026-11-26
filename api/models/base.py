
from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
    Identity,
    Integer,
    MetaData,
    func,
)
from sqlalchemy.orm import DeclarativeBase


# Standard naming conventions for database constraints
naming_convention = {
    "ix": "ix_%(table_name)s_%(column_0_name)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Base(DeclarativeBase):
    metadata = MetaData(naming_convention=naming_convention)


class IDMixin:
    id = Column(
        Integer,
        Identity(always=True),
        primary_key=True,
    )


class TimestampMixin:
    create_dt = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
