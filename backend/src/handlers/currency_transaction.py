from flask_restful import Resource, request

from src.processor.currency_transaction import process
from src.schemas.currency_transaction import CurrencyTransactionInput, CurrencyTransactionOutput
from src.utils.apm import apm
from src.utils.decorators import validate_schema
from src.utils.exceptions import InvalidCurrencyInput
from src.utils.helper_functions import json_parser


class CurrencyTransaction(Resource):

    @validate_schema(CurrencyTransactionInput)
    def post(self):
        parsed_request_data = json_parser(request.data)
        try:
            process_result = process(parsed_request_data['currency'], parsed_request_data['amount'])
            if not process_result:
                return {"message": "Failed request please try again latter"}, 500

        except InvalidCurrencyInput:
            apm.capture_exception()
            return {"message": "Invalid currency input"}, 400

        return {
            "message": "Request processed",
            "data": CurrencyTransactionOutput(process_result, strict=False).to_primitive()
        }
