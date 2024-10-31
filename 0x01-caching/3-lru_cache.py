#!/usr/bin/env python3
"""LRU caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    LRUCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        """Initializes the LRUCache Class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Assign to the dictionary self.cache_data the
        item value for the key key
        """
        if (key is None) or (item is None):
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the least recently used item
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        # Add the new key and item, then update order list
        self.cache_data[key] = item
        self.order.append(key)

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
