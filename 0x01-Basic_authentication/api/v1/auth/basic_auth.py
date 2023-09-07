#!/usr/bin/env python3
"""The Basic Auth class"""

from api.v1.auth.auth import Auth
import base64


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
