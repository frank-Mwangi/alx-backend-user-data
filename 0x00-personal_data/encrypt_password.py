#!/usr/bin/env python3
"""
Password encrypting module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """apply bcrypt encoding on plaintext password"""
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed
