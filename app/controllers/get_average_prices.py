from flask import Blueprint;
from flask import request;
from models.rates_format import RatesSchema;
from utilities.rates_calculation import rates_calculation;

average_prices = Blueprint("average_prices", __name__)

@average_prices.route('/rates', methods=['GET'])
def GET_average_prices():  # route handler function
    
    # with our schema we can validate the requests arguments.
    check_args = RatesSchema().validate(request.args)
    if (check_args):
        return "error in arguments"
    
    return rates_calculation(**request.args)

