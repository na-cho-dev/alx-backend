#!/usr/bin/env python3
"""LIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initializes the LIFOCache Class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key
        """
        if (key is None) or (item is None):
            return

        if key in self.cache_data:
            self.queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.queue.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        Returns the value in self.cache_data linked to key
        """
        if key is None:
            return None

        for ky, val in self.cache_data.items():
            if ky is None:
                return None
            elif ky == key:
                return val
