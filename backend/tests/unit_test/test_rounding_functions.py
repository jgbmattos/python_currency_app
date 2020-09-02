from src.utils.helper_functions import round_value_up, truncate_value, calculate_final_amount
from decimal import Decimal

value = Decimal('0.000021899')
transaction_value = Decimal('10.5')


def test_round_value_up():
    rounded_value = round_value_up(value, 8)
    assert rounded_value == Decimal('0.00002190')


def test_truncate_value():
    truncated_value = truncate_value(value, 9)
    assert truncated_value == 21899


def test_calculate_final_amount():
    final_value = calculate_final_amount(value, transaction_value, 8)
    assert final_value == Decimal('0.00022994')
