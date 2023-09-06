#!/usr/bin/env python3
"""
API authentication class
"""

from typing import List, TypeVar
from flask import request


class Auth:
    """The authentication class"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Self explanatory"""
        if path is None:
            return True
        if excluded_paths is None:
            return True
        if len(excluded_paths) == 0:
            return True
        if path is None or excluded_paths is None:
            return True
        path = path + '/' if path[-1] != '/' else path
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Auth headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """handles the Flask request object"""
        return None
