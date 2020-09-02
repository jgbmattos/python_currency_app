from flask import jsonify
from flask_restful import Resource, request

from src.models.queries import get_latests_transactions
from src.schemas.currency_transaction import CurrencyTransactionOutput


class TransactionHistory(Resource):

    def get(self):
        currency = request.args.get('currency')
        limit = request.args.get('limit', 1, type=int)
        page = request.args.get('page', 1, type=int)
        print(page)
        query_result = get_latests_transactions(currency, page, limit)
        if not query_result:
            return {}, 204

        return jsonify(
            {
                'page': query_result.page,
                'pages': query_result.pages,
                'total': query_result.total,
                'total_per_page': query_result.per_page,
                'data': [CurrencyTransactionOutput(item.as_dict(), strict=False).to_native()
                         for item in query_result.items]
            }
        )
