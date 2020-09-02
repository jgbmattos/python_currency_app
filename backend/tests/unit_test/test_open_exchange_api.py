from typing import Dict
from unittest import TestCase
from unittest.mock import patch

from src.external_apis.open_exchange_rates import OpenExchangeRates
from src.utils.exceptions import InvalidCurrencyInput
from tests import mocked_api_response


@patch("src.external_apis.open_exchange_rates.OpenExchangeRates._get_rates")
def test_get_current_rate(mocked_get_rates):
    mocked_get_rates.return_value = mocked_api_response
    CURRENCY_RATE = OpenExchangeRates.get_current_rate("BRL")
    assert CURRENCY_RATE == 5.6088

    CURRENCY_RATE = OpenExchangeRates.get_current_rate("ZAR")
    assert CURRENCY_RATE == 16.91655

    with TestCase().assertRaises(InvalidCurrencyInput):
        OpenExchangeRates.get_current_rate("ABC")


@patch("src.external_apis.open_exchange_rates.OpenExchangeRates._get_rates")
def test_get_current_forecast(mocked_get_rates):
    mocked_get_rates.return_value = mocked_api_response
    forecast = OpenExchangeRates.get_forecast()
    assert 'rates' in forecast
    assert 'timestamp' in forecast
    assert 'base' in forecast
    assert isinstance(forecast['rates'], Dict)
