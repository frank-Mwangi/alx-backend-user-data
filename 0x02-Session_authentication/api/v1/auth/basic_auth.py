#!/usr/bin/env python3
"""The Basic Auth class"""

from api.v1.auth.auth import Auth
import base64
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Defining the BasicAuth class"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Encode auth header"""
        if authorization_header is None:
            return None
        if type(authorization_header) != str:
            return None
        if authorization_header.startswith("Basic "):
            return "".join(authorization_header.split(" ")[1:])

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """Decodes a base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) != str:
            return None
        try:
            bytes = base64_authorization_header.encode("utf-8")
            encoded = base64.b64decode(bytes)
            return encoded.decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> (str, str):
        """Extract credentials from auth header"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) != str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        header = decoded_base64_authorization_header
        email = header.split(":")[0]
        password = header.split(":")[1]
        return (email, password)

    def user_object_from_credentials(self,
                                     user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """Return an user instance"""
        if user_email is None or type(user_email) != str:
            return None
        if user_pwd is None or type(user_pwd) != str:
            return None
        try:
            users = User.search({"email": user_email})
            if not users:
                return None
            for user in users:
                if user and user.is_valid_password(user_pwd):
                    return user
                return None
        except Exception:
            return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieve User instance for a request"""
        if request:
            auth_head = self.authorization_header(request)
            extract = self.extract_base64_authorization_header(auth_head)
            decode = self.decode_base64_authorization_header(extract)
            (email, password) = self.extract_user_credentials(decode)
            return self.user_object_from_credentials(email, password)
