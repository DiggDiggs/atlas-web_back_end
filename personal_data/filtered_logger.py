""" takes arguments to have tghem return nothing the function will obtain an display each row under a filtered format"""
from typing import List
import logging 
import re 
import os
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "address", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Redact sensitive fields in log message"""
    for field in PII_FIELDS:
        message = re.sub(rf"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
0