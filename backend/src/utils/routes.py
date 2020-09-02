from flask_restful import Api
from src.handlers.currency_transaction import CurrencyTransaction
from src.handlers.transaction_history import TransactionHistory
from src.handlers.get_forecast import GetForecast


def set_endpoints(app):
    api = Api()
    api.add_resource(CurrencyTransaction, f"/api/currency-transaction")
    api.add_resource(TransactionHistory, f"/api/currency-transactions/last")
    api.add_resource(GetForecast, f"/api/get-forecast")
    api.init_app(app)
