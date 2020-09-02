import os
import unittest
from decimal import Decimal
from http import HTTPStatus
from random import uniform, randint
from unittest.mock import patch

from src.database.helper import db
from src.utils.settings import BASE_DIR
from tests import mocked_api_response
from tests.integration_test import build_testing_flask_app

""" 
    ############################                      DISCLAIMER                      ############################
    DUE TO THE FACT THAT SQLITE DON'T HAVE DECIMAL TYPE IT IS IMPOSSIBLE TO TEST VALUE ROUNDING HERE UNFORTUNATELY
    ##############################################################################################################
"""


class UserTest(unittest.TestCase):

    def setUp(self):
        self.db_uri = f'{BASE_DIR}/database/app.db'
        self.app = build_testing_flask_app(self.db_uri)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        try:
            '''PYTHON PHILOSOPHY BETTER SAY SORRY THAN ASK FOR PERMISSION....'''
            os.remove(self.db_uri)
        except Exception:
            pass

    @patch("src.external_apis.open_exchange_rates.OpenExchangeRates._get_rates")
    def test_general_endpoints(self, mocked_get_rates):
        mocked_get_rates.return_value = mocked_api_response
        payload = {
            "amount": uniform(0, 999999),
            "currency": "EUR"
        }

        response = self.app.post(
            '/api/currency-transaction',
            json=payload
        )

        assert response.status_code == HTTPStatus.OK.value
        response = self.app.get(
            '/api/currency-transactions/last'
        )

        assert response.status_code == HTTPStatus.OK.value

    @patch("src.external_apis.open_exchange_rates.OpenExchangeRates._get_rates")
    def test_last_endpoint_ordering(self, mocked_get_rates):
        mocked_get_rates.return_value = mocked_api_response
        currency_list = list(mocked_api_response['rates'].keys())
        test_mapping = {}
        for i in range(50):
            payload = {
                "amount": uniform(0.1, 9999),
                "currency": currency_list[randint(0, len(currency_list))-1]
            }
            if payload['currency'] not in test_mapping:
                test_mapping[payload['currency']] = []

            test_mapping[payload['currency']].append(payload['amount'])

            response = self.app.post(
                '/api/currency-transaction',
                json=payload
            )

            assert response.status_code == HTTPStatus.OK.value

            response = self.app.get(
                '/api/currency-transactions/last',
                json=payload
            )

            assert response.status_code == HTTPStatus.OK.value

            assert response.json['data'][0]['transactionCurrencySymbol'] == payload['currency']

        response = self.app.get(
            '/api/currency-transactions/last?limit=50',
            json=payload
        )
        assert response.status_code == HTTPStatus.OK.value

        assert response.json['total'] == 50

        for currency in test_mapping.keys():
            response = self.app.get(
                f'/api/currency-transactions/last?currency={currency}'
            )
            assert response.status_code == HTTPStatus.OK.value

            assert int(Decimal(response.json['data'][0]['transactionAmount'])) == int(test_mapping[currency][-1])

        for currency in test_mapping.keys():
            response = self.app.get(
                f'/api/currency-transactions/last?currency={currency}&limit={len(test_mapping[currency])}'
            )
            assert response.status_code == HTTPStatus.OK.value

            assert response.json['total'] == len(test_mapping[currency])

            for index, values in enumerate(test_mapping[currency]):
                assert int(Decimal(response.json['data'][index]['transactionAmount'])) == int(test_mapping[currency][(index * -1) -1])

        for currency in test_mapping.keys():
            page = 1
            currency_sum = Decimal(0)
            while True:
                response = self.app.get(
                    f'/api/currency-transactions/last?currency={currency}&limit=50&page={page}'
                )
                assert response.status_code == HTTPStatus.OK.value

                pages = response.json['pages']
                for data in response.json['data']:
                    currency_sum += Decimal(data['transactionAmount'])

                page =+ 1
                if pages == pages:
                    break

            assert int(currency_sum) == int(sum(test_mapping[currency]))
