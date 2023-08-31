#!/usr/bin/env python3
"""
The filtered logger module
"""
from os import environ
from mysql.connector import connection
import re
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def get_db() -> connection.MySQLConnection:
    """Return a connector to the database"""
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    pwd = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    db_host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")
    connector = connection.MySQLConnection(
        user=username,
        password=pwd,
        host=db_host,
        database=db_name
    )
    return connector


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Return log message obfuscated"""
    for field in fields:
        message = re.sub(f'{field}=(.*?){separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Filters values in incoming log records"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Logs while obfuscating PII fields"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    logger.addHandler(handler)
    handler.setFormatter(RedactingFormatter(PII_FIELDS))

    return logger
