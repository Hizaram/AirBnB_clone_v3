#!/usr/bin/python3
"""Module that gets our app running for the project"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """Function that stops the current session
    Arguments:
        error [str]: Error message or exception
    """
    storage.close()


@app.errorhandler(404)
def not_found(message):
    """Handles the error 404 status code
    Arguments:
        message (str): The string to display in place of an error
    Returns:
        The HTTP response for the request
    """
    response = jsonify({"error": "Not found"})
    response.status_code = 404
    return response


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', default=5000)),
            threaded=True
            )
