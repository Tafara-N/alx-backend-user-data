#!/usr/bin/env python3

"""
A Flask app that has a single GET route ("/") and use flask.jsonify to return a
JSON payload
"""

from flask import Flask, abort, jsonify, redirect, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index() -> str:
    """
    Index endpoint

    Return
        A JSON payload: {"message": "Bienvenue"}
    """

    return jsonify({
        "message": "Bienvenue"
        })


@app.route("/users", methods=["POST"], strict_slashes=False)
def register() -> str:
    """
    Registering a new user

    Return
        A JSON payload: {"email": "<user email>", "message": "user created"}
    """

    email = request.form.get("email")
    password = request.form.get("password")

    try:
        user = AUTH.register_user(email, password)
        if user is not None:
            return jsonify({
                "email": user.email,
                "message": "user created"
                })
    except ValueError:
        return jsonify({
            "message": "email already registered"
            }), 400


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    Creating a session for the user

    Return
        A JSON payload: {"email": "<user email>", "message": "logged in"}
    """

    email = request.form.get("email")
    password = request.form.get("password")

    is_valid = AUTH.valid_login(email, password)
    if not is_valid:
        abort(401)

    session_id = AUTH.create_session(email)

    response = jsonify({
        "email": email,
        "message": "logged in"
        })

    response.set_cookie("session_id", session_id)

    return response


@app.route("/sessions", methods=["DELETE"], strict_slashes=False)
def logout():
    """
    Destroying/ Log out a user session

    Return
        A redirect to the root of the app
    """

    session_id = request.cookies.get("session_id", None)
    user = AUTH.get_user_from_session_id(session_id)

    if session_id is None or user is None:
        abort(403)

    AUTH.destroy_session(user.id)

    return redirect("/")


@app.route("/profile", methods=["GET"], strict_slashes=False)
def profile() -> str:
    """
    Showing the profile of the user

    Return
        A JSON payload: {"email": "<user email>"}
    """

    session_id = request.cookies.get("session_id", None)
    if session_id is None:
        abort(403)

    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)

    return jsonify({
        "email": user.email
        }), 200


@app.route("/reset_password", methods=["POST"], strict_slashes=False)
def get_reset_password_token() -> str:
    """
    Generating a reset passowrd token for the user
    """

    email = request.form.get("email")
    session_id = AUTH.create_session(email)

    if not session_id:
        abort(403)

    token = AUTH.get_reset_password_token(email)

    return jsonify({
        "email": email,
        "reset_token": token
        })


@app.route("/reset_password", methods=["PUT"], strict_slashes=False)
def update_password() -> str:
    """
    Updating the user's password

    Return
        A JSON payload: {
            "email": "<user email>",
            "message": "Password updated"
            }
    """

    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")

    try:
        AUTH.update_password(reset_token, new_password)
    except Exception:
        abort(403)

    return jsonify({
        "email": email,
        "message": "Password updated"
        }), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
