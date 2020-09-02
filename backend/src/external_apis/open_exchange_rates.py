from http import HTTPStatus

import requests

from src.utils.decorators import cache
from src.utils.exceptions import InvalidCurrencyInput
from src.utils.helper_functions import json_parser
from src.utils.settings import OPEN_EXCHANGE_HOST, OPEN_EXCHANGE_API_KEY

"""
    DISCLAIMER:
    
    Reading their doc (https://openexchangerates.org/faq) this API is updated every hour. So I decided to use Redis 
    as a cache (@cache decorator) to not make unnecessary requests to their API 

"""


class OpenExchangeRates:

    @staticmethod
    @cache
    def _get_rates():
        response = requests.get(
            f"{OPEN_EXCHANGE_HOST}/latest.json?show_alternative=true&app_id={OPEN_EXCHANGE_API_KEY}",
            verify=False
        )
        response.raise_for_status()

        if response.status_code != HTTPStatus.OK.value:
            raise Exception(f"integration error. OpenExchange. server response status code: {response.status_code}")

        return json_parser(response.content)

    @staticmethod
    def get_current_rate(currency_symbol: str = None):
        api_response = OpenExchangeRates._get_rates()

        if currency_symbol not in api_response['rates']:
            raise InvalidCurrencyInput

        return api_response['rates'][currency_symbol]

    @staticmethod
    def get_forecast():
        return OpenExchangeRates._get_rates()
