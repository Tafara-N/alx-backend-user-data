#!/usr/bin/env python3

"""
User authentication service
"""

import bcrypt

from typing import Union
from uuid import uuid4

from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


def _hash_password(password: str) -> str:
    """
    Hash a password

    Parameters
        password - the password to be hashed

    Return
        The hashed password
    """

    return bcrypt.hashpw(
        password.encode('utf-8'), bcrypt.gensalt()
        ).decode('utf-8')


def _generate_uuid() -> str:
    """
    Generating a UUID
    """

    return str(uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """
        Registering a new user
        """

        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

        else:
            raise ValueError(f'User {email} already exists')

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validate a user login

        Return
            True if the password is valid, False otherwise
        """

        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(
                password.encode('utf-8'),
                user.hashed_password.encode('utf-8')
                )

        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """
        Creates a session and saves it in the database

        Return
            The session ID
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)

        return session_id
