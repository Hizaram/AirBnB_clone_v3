#!/usr/bin/python3
"""Module that houses the routing function for status"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def hello_status():
    """Function that returns the jsonfied version of status"""
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def hello_stats():
    """Function that retrieves the number of each object in JSON format
    Returns:
        Jsonified format of the count method of all objects
    """
    stats_dict = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(stats_dict)
