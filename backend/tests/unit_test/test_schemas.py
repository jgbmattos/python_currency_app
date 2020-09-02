from src.schemas.currency_transaction import CurrencyTransactionOutput, CurrencyTransactionInput
from tests.unit_test import mocked_db_payload, mocked_fault_db_payload, mocked_input
from schematics.exceptions import DataError
from unittest import TestCase


def test_output_schema():
    CurrencyTransactionOutput(CurrencyTransactionOutput(mocked_db_payload).to_primitive()).validate()

    with TestCase().assertRaises(DataError):
        CurrencyTransactionOutput(CurrencyTransactionOutput(mocked_fault_db_payload).to_primitive()).validate()


def test_input_schema():
    CurrencyTransactionInput(mocked_input).validate()
