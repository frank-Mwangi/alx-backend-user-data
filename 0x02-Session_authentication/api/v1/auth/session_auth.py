#!/usr/bin/env python3
"""Session Authentication module"""

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """The Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a session"""
        if user_id is None:
            return None
        if type(user_id) != str:
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
