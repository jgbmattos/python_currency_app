
from datetime import datetime

from sqlalchemy import Column, Boolean
from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


def get_timestamp():
    return int(datetime.utcnow().timestamp() * 1000000)


class BaseModel(DeclarativeBase):
    __abstract__ = True

    created_at_utc = Column(BIGINT(unsigned=True), nullable=False, default=get_timestamp, index=True)
    deleted = Column(Boolean, default=False, nullable=False)
