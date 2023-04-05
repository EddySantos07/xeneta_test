from flask import Blueprint;
from flask import request;
from models.rates_format import RatesSchema;
from utilities.rates_calculation import rates_calculation;

average_prices = Blueprint("average_prices", __name__)

@average_prices.route('/rates', methods=['GET'])
def GET_average_prices():  # route handler function
    # check for any errors in any values when taking them in
    #  we can do that with a class

    print(request.args, "request arguments???")

    # with our schema we can validate the requests arguments.
    check_args = RatesSchema().validate(request.args)
    if (check_args):
        return "error in arguments"
    
    return rates_calculation(**request.args)

