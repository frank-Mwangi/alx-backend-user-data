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
        path = path + '/' if path[len(path) - 1] != '/' else path
        if path in excluded_paths:
            return False      
        return True

    def authorization_header(self, request=None) -> str:
        """Auth headers"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """handles the Flask request object"""
        return None
