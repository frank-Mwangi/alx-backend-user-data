#!/usr/bin/env python3
"""The Basic Auth class"""

from api.v1.auth.auth import Auth


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
