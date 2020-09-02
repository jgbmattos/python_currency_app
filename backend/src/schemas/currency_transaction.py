from schematics import Model
from schematics.types import StringType, DateTimeType, DecimalType


class CurrencyTransactionInput(Model):
    currency = StringType(required=True, min_length=3, max_length=10)
    amount = DecimalType(required=True)


class CurrencyTransactionOutput(Model):
        base_currency_symbol = StringType(required=True, min_length=3, max_length=10, serialized_name="baseCurrencySymbol")
        final_amount = DecimalType(required=True, serialized_name='finalAmount')
        transaction_amount = DecimalType(required=True, serialized_name='transactionAmount')
        transaction_currency_symbol = StringType(required=True, min_length=3, max_length=10, serialized_name="transactionCurrencySymbol")
        currency_rate = DecimalType(required=True, serialized_name='currencyRate')
        created_at_utc = DateTimeType(required=True, serialized_name="transactionDateTime")
        id = StringType(required=True)
