# app.py
from flask import Flask
from controllers.get_average_prices import average_prices
from utilities.db_connection import db_cursor


def create_app():
    # name for the Flask app (refer to output)
    app = Flask(__name__)

    app.register_blueprint(average_prices)
    
    db_cursor()

    # defining a route
    @app.route("/", methods=['GET'])
    def home():  # route handler function
        # returning a response
        return "Hello World!"

    return app


APP = create_app()
