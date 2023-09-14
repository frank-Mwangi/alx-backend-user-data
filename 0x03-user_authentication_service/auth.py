#!/usr/bin/env python3
"""
The authentication module
"""

from xmlrpc.client import Boolean
import bcrypt
from db import DB
from user import User
from typing import TypeVar
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _hash_password(password: str) -> bytes:
    """Hash user password method"""
    encoded_pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)
    return hashed_pwd


def _generate_uuid() -> str:
    """Method to generate random uuid"""
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> Boolean:
        """Validate credentials method"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False
