#!/usr/bin/env python3

"""
User authentication service
"""

import bcrypt
from uuid import uuid4
from typing import Union
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
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()
