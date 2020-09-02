from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, String, DECIMAL

from src.models.base_model import BaseModel


def get_uuid():
    return str(uuid4())


class CurrencyTransactions(BaseModel):
    __tablename__ = 'currency_transaction'

    id = Column(String(36), nullable=False, default=get_uuid, primary_key=True)
    base_currency_symbol = Column(String(10), nullable=False, default='USD')
    transaction_currency_symbol = Column(String(10), nullable=False)
    final_amount = Column(DECIMAL(28, 8), nullable=False)
    transaction_amount = Column(DECIMAL(28, 12), nullable=False)
    currency_rate = Column(DECIMAL(28, 12), nullable=False)

    def as_dict(self):
        return {
            c.name: datetime.fromtimestamp(getattr(self, c.name) / 1000000)
            if c.name == 'created_at_utc' and getattr(self, c.name) else getattr(self, c.name)
            for c in self.__table__.columns
        }
