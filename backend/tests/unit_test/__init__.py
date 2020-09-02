from datetime import datetime
from uuid import uuid4

serialized_mocked_json_with_decimals = b'{"message": "mocked", "value": 0.000021899}'

mocked_input = {
    "amount": 0.25567801,
    "currency": "BTC"
}

mocked_fault_db_payload = {
    "base_currency_symbol": "USD",
    "final_amount": "0.00002189",
    "transaction_amount": "0.255678010000",
    "transaction_currency_symbol": "BTC",
    "currency_rate": "0.000085581293"
}

mocked_db_payload = {
    "base_currency_symbol": "USD",
    "final_amount": "0.00002189",
    "transaction_amount": "0.255678010000",
    "transaction_currency_symbol": "BTC",
    "currency_rate": "0.000085581293",
    "created_at_utc": datetime.utcnow(),
    "id": str(uuid4())
}
