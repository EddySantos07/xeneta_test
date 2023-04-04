from flask import Blueprint
from flask import request

from models.rates_format import RatesSchema;

average_prices = Blueprint("average_prices", __name__)

@average_prices.route('/rates',  methods=['GET'])
def GET_average_prices():  # route handler function

    # grabbing all the parameters
    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    # returning a response
    return "Hello World!"
