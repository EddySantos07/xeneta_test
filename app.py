#app.py
from flask import Flask;
from flask import request;

# name for the Flask app (refer to output)
app = Flask(__name__) 

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return "Hello World!"

@app.route("/GET_average_prices", methods=['GET']) # decorator
def GET_average_prices(): # route handler function

    date_from = request.args.get('date_from')
    date_to = request.args.get('date_to')
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    # returning a response
    return "Hello World!"

# running the server
# app.run(debug=True)