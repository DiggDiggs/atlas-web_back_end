#!/usr/bin/env python
"""
This is one alternative implementation of a FIFO cache 
that inherits from BaseCaching.
"""

from base_caching import BaseCaching

class FIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        if key is None or item is None:
            return
        
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded = self.keys.pop(0)
            print(f"DISCARD: {discarded}")
            del self.cache_data[discarded]

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
