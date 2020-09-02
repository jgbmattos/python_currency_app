from src.database.helper import read_replica_async_session
from src.models.currency_transaction import CurrencyTransactions
from sqlalchemy import desc
from src.utils.apm import apm


def get_latests_transactions(currency=None, page=1, limit=1):
    try:
        with read_replica_async_session() as session:
            query = session.query(CurrencyTransactions)
            if currency:
                query = query.filter(CurrencyTransactions.transaction_currency_symbol == currency)

            query = query.order_by(desc(CurrencyTransactions.created_at_utc)).limit(limit)

            return query.from_self().paginate(page=page, per_page=10 if limit > 10 else limit)

    except Exception:
        apm.capture_exception()
