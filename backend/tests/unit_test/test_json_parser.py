from tests.unit_test import serialized_mocked_json_with_decimals
from src.utils.helper_functions import json_parser, round_value_up
from decimal import Decimal


def test_json_parser():
    parsed_json = json_parser(serialized_mocked_json_with_decimals)

    assert round_value_up(parsed_json['value'], 8) == round_value_up(Decimal('0.000021899'), 8)
