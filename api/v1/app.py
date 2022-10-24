#!/usr/bin/python3
"""Module that gets our app running for the project"""
from os import getenv
from models import storage
from api.v1.views import app_views
from flask import Flask, Blueprint


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(error):
    """Function that stops the current session
    Arguments:
        error [str]: Error message or exception
    """
    storage.close()


if __name__ == "__main__":
    app.run(host=getenv('HBNB_API_HOST', default='0.0.0.0'),
            port=int(getenv('HBNB_API_PORT', default=5000)),
            threaded=True
            )
