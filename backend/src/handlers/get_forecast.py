from flask_restful import Resource
from src.external_apis.open_exchange_rates import OpenExchangeRates
from flask import jsonify


class GetForecast(Resource):
    
    def get(self):
        response = OpenExchangeRates.get_forecast()

        return jsonify(response['rates'])


