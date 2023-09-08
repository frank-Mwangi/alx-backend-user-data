#!/usr/bin/env python3

"""
Module to handle all routes for session auth
"""
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """The login method"""
    email = request.form.get('email', None)
    password = request.form.get('password', None)
    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400
    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404
    for user in users:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401
        from api.v1.app import auth
        session_id = auth.create_session(user.id)
        session_name = os.getenv("SESSION_NAME")
        resp = jsonify(user.to_json())
        resp.set_cookie(session_name, session_id)
        return resp


@app_views.route('/auth_session/logout',
                 methods=['DELETE'],
                 strict_slashes=False)
def logout():
    """The logout method"""
    from api.v1.app import auth
    logout = auth.destroy_session(request)
    if logout:
        return jsonify({}), 200
    abort(404)
