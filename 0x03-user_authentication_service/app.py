#!/usr/bin/env python3

"""
A Flask app that has a single GET route ("/") and use flask.jsonify to return a
JSON payload
"""

from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Index endpoint

    Return
        A JSON payload: {"message": "Bienvenue"}
    """

    return jsonify(
        {"message": "Bienvenue"}
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
