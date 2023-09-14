#!/usr/bin/env python3
"""
The authentication module
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """Hash user password method"""
    encoded_pwd = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(encoded_pwd, salt)
    return hashed_pwd
