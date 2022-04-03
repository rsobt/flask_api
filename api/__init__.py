from flask import Blueprint, jsonify, request
from flaskbook_api.api import caluculation

api = Blueprint("api", __name__)


@api.route("/")
def index():
    return jsonify({"column": "value"}), 201


@api.post("/detect")
def detection():
    return caluculation.detection(request)
