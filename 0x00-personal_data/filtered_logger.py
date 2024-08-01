#!/usr/bin/env python3

"""
Log formatter
"""

import logging
import os
import re
from typing import List

import mysql.connector

PII_FIELDS = (
    "name", "email", "phone", "ssn", "password"
    )


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """format record"""
        return filter_datum(
            self.fields,
            self.REDACTION,
            super(RedactingFormatter, self).format(record),
            self.SEPARATOR,
        )


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Function that returns the log message obfuscated

    Parameters
        fields: list of fields to redact
        redaction: string representing redacted message
        message: string representing message
        separator: string representing

    Return
        User data filtered message
    """

    for field in fields:
        pattern = f"{field}=[^{separator}]*"
        message = re.sub(pattern, f"{field}={redaction}", message)
    return message


def get_logger() -> logging.Logger:
    """
    Function that returns a logging object
    """

    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))  # type: ignore
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Function that returns a connector to the database
    """

    host = os.getenv("PERSONAL_DATA_DB_HOST", "localhost")
    user = os.getenv("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.getenv("PERSONAL_DATA_DB_PASSWORD", "")
    database = os.getenv("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=database
    )

    return connection  # type: ignore



def main():
    """
    Main function
    """

    connection = get_db()
    users = connection.cursor()
    users.execute(
        "SELECT CONCAT('name=', name, ';ssn=', ssn, ';ip=', ip, \
        ';user_agent', user_agent, ';') AS message FROM users;"
    )
    formatter = RedactingFormatter(fields=PII_FIELDS)  # type: ignore
    logger = get_logger()

    for user in users:
        logger.log(logging.INFO, user[0])


if __name__ == "__main__":
    main()
