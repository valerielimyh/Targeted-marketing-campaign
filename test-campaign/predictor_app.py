import flask
from flask import request
from predictor_api import make_prediction, feature_names

# Initialize the app

app = flask.Flask(__name__)


# An example of routing:
# If they go to the page "/" (this means a GET request
# to the page http://127.0.0.1:5000/), return a simple
# page that says the site is up!
@app.route("/")
def hello():
	return flask.render_template('index.html')
	# return "It's alive"


@app.route("/predict", methods=["POST", "GET"])
def predict():
    # request.args contains all the arguments passed by our form
    # comes built in with flask. It is a dictionary of the form
    # "form name (as set in template)" (key): "string in the textbox" (value)
    x_input, predictions = make_prediction(request.args)
    return flask.render_template('predictor_bootstrap.html', x_input=x_input,
                                 feature_names=feature_names,
                                 prediction=predictions)


# Start the server, continuously listen to requests.
# We'll have a running web app!

# For local development:

if __name__=="__main__":
    # For local development:
    #app.run(debug=True)
    # For public web serving:
    #app.run(host='0.0.0.0')
    app.run()
# app.run(port=5000,debug=True)

# For public web serving:
# app.run(host='0.0.0.0')
