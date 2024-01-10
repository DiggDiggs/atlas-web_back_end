"""
Create a class LIFOCache that inherits from BaseCaching
and is a LIFO caching system implemented in a different way
"""


BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    - Uses self.cache_data dict from BaseCaching parent class

    - Overloads __init__() and calls parent init with super()
    """
    
    def __init__(self):
        """
        - Overloaded __init__()
        - Calls parent __init__()
        """
        super().__init__()

    def put(self, key, item):
        """
        - Adds item to self.cache_data dict with key
        
        - Does nothing if key or item is None

        - Removes oldest item if cache size exceeds BaseCaching.MAX_ITEMS
        - Prints discarded key
        """
        
        if key is None or item is None:
            return
        
        self.cache_data[key] = item
        
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = list(self.cache_data)[0]
            print("DISCARD:", oldest_key)
            del self.cache_data[oldest_key]

    def get(self, key):
        """
        - Returns value from self.cache_data dict for key
        
        - Returns None if key is None or doesn't exist
        """
        
        if key is None or key not in self.cache_data:
            return None
        
        return self.cache_data[key]
