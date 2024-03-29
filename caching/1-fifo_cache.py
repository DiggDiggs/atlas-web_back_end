#!/usr/bin/env python
"""
We are creating class FIFOCache that inherits from BaseCaching
and is a FIFO caching system
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    -You must use <self.cache_data>: dict from the parent class BaseCaching

    -You can overload def __init__(self):
    but don’t forget to call the parent init: super().__init__()
    """

    def __init__(self):
        """
        -Overload inherited init
        """
        super().__init__()

    def put(self, key, item):
        """
        -Assigns to the dict <self.cache_data> the item value for the key

        -If key or item is None, dont do anything.

        -If the number of items in self.cache_data is higher than
        BaseCaching.MAX_ITEMS, you must get ride of the first item
        put in cache (FIFO algorithm), and you must print DISCARD:
        with the key discarded
        """

        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = list(self.cache_data.keys())[0]
            del self.cache_data[discarded_key]

            print("DISCARD: {}".format(discarded_key))

    def get(self, key):
        """
        -Returns the value in self.cache_data linked to key.

        -If key is None or if the key doesn’t exist in self.cache_data,
        return None.
        """

        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
