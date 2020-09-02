from decimal import Decimal

from src.database.helper import get_session
from src.external_apis.open_exchange_rates import OpenExchangeRates
from src.models.currency_transaction import CurrencyTransactions
from src.utils.apm import apm
from src.utils.exceptions import InvalidCurrencyInput
from src.utils.helper_functions import round_value_up, calculate_final_amount


def process(currency_symbol: str, transact_amount: Decimal):
    try:
        currency_rate = OpenExchangeRates.get_current_rate(currency_symbol)

        currency_conversion = CurrencyTransactions()
        currency_conversion.base_currency_symbol = "USD"
        currency_conversion.transaction_currency_symbol = currency_symbol
        currency_conversion.transaction_amount = round_value_up(transact_amount, 12)
        currency_conversion.currency_rate = round_value_up(currency_rate, 12)
        currency_conversion.final_amount = calculate_final_amount(currency_rate, transact_amount, 8)

        response = currency_conversion.as_dict()
        with get_session() as session:
            session.add(currency_conversion)
            session.commit()

        return response

    except InvalidCurrencyInput:
        apm.capture_exception()
        raise InvalidCurrencyInput

    except Exception:
        apm.capture_exception()


