#!/usr/bin/env python3
"""
Password encrypting module
"""
from xmlrpc.client import Boolean
import bcrypt


def hash_password(password: str) -> bytes:
    """apply bcrypt encoding on plaintext password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed


def is_valid(hashed_password: bytes, password: str) -> Boolean:
    """Validate provided password against hashed record"""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
