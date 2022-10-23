#!/usr/bin/python3
"""Module that houses the routing function for status"""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def hello_status():
    """Function that returns the jsonfied version of status"""
    return jsonify({'status': 'OK'})
