from decimal import Decimal, ROUND_UP
from json import JSONDecoder
from typing import Union


def round_value_up(value: Union[float, Decimal], decimals: int):
    if not isinstance(value, Decimal):
        value = Decimal(value)
    return value.quantize(Decimal(f'0.{"0" * (decimals-1)}1'), rounding=ROUND_UP)


def truncate_value(value: Union[float, Decimal], decimals: int):
    return int(value * (10 ** decimals))


def calculate_final_amount(currency_rate: Union[float, Decimal],
                           transaction_amount: Union[float, Decimal], decimals: int):
    return round_value_up((truncate_value(round_value_up(currency_rate, 12), 12) *
                           truncate_value(round_value_up(transaction_amount, 12), 12)) / Decimal(10 ** (12 * 2)),
                          decimals)


def json_parser(data: bytes):
    return JSONDecoder(parse_float=Decimal).decode(data.decode('utf8'))
