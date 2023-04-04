from flask import Blueprint
from flask import request
from models.rates_format import RatesSchema

average_prices = Blueprint("average_prices", __name__)


@average_prices.route('/rates', methods=['GET'])
def GET_average_prices():  # route handler function
    # check for any errors in any values when taking them in
    #  we can do that with a class

    # with our schema we can validate the requests arguments.
    if (RatesSchema.validate(request.args)):
        return "error in arguments"

    # returning a response
    return "Rates"
