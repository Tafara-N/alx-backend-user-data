#!/usr/bin/env python3

"""
Function expects one string argument name `password` and returns a salted,
hashed password, which is a byte string

The other expects two args to validate that the provided password matches the
hashed password and returns a boolean value
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function to hash the input password and return the hashed bytes

    Parameter
        password (str): Input password to be hashed

    Return
        bytes: Hashed password in bytes
    """

    if password:
        return bcrypt.hashpw(str.encode(password), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Checks if the provided password matches the hashed password by using bcrypt

    Parameters
        hashed_password: A bytes object representing the hashed password
        password: A string representing the plain text password

    Return
        A boolean indicating whether the password matches the hashed password
    """

    if hashed_password and password:
        return bcrypt.checkpw(str.encode(password), hashed_password)
