#!/usr/bin/env python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system:
    """
    def __inti__(self):
        """Initialize BasicCache Class"""
        super().__init__()

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key
        """
        if (key is None) or (item is None):
            return

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
