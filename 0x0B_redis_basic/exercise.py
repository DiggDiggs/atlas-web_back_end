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
    def wrapper(self, *args, **kwargs):
        """
       Uses rpush to append input parameters to the list of inputs.
        """
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(output))
        return output
    return wrapper