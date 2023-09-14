#!/usr/bin/env python3
"""
The authentication module
"""

import bcrypt
from db import DB
from user import User
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """Hash user password method"""
    encoded_pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)
    return hashed_pwd


class Auth:
    """
    Auth class to interact with the authentication database
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> TypeVar('User'):
        """"The register user method"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
            return new_user
