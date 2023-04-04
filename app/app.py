#app.py
from flask import Flask;
from controllers import get_average_prices;

# name for the Flask app (refer to output)
app = Flask(__name__) 

app.register_blueprint(get_average_prices)

# defining a route
@app.route("/", methods=['GET', 'POST', 'PUT']) # decorator
def home(): # route handler function
    # returning a response
    return "Hello World!"

# @app.route("/GET_average_prices", methods=['GET']) # decorator


# running the server
# app.run(debug=True)