#!/usr/bin/env python3
"""
Redis cache , retreives data,stores data. A lot of data is stored in cache.
"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps
def call_history(method: Callable) -> Callable:
    """
    looks at and writes the input and output of a Cache() method.
    """
    @wraps(method)