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

    def get_user_from_session_id(self, session_id: str) -> Union[str, None]:
        """
        Fetches a user using the session id

        Return
            The user associated with the session ID, or None if the session ID
            does not exist
        """

        if session_id is None:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None

    def get_reset_password_token(self, email: str) -> str:
        """
        Generates a password reset token

        Return
            The reset token
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError

        token = _generate_uuid()
        self._db.update_user(user.id, reset_token=token)

        return token

    def update_password(self, reset_token: str, password: str) -> None:
        """
        Updates a user's password

        Return
            None
        """

        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError

        self._db.update_user(user.id, hashed_password=_hash_password(password))
        self._db.update_user(user.id, reset_token=None)
