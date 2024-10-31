#!/usr/bin/env python3
"""FIFO caching"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initializes the FIFOCache Class"""
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key
        """
        if (key is None) or (item is None):
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_item = list(self.cache_data)[0]
            print(f'DISCARD: {first_item}')
            first_item = self.cache_data.pop(first_item)

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
