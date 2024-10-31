#!/usr/bin/env python3
"""LRU caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    A caching system that inherits from BaseCaching
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []  # To track order of key accesses for LRU removal algo

    def put(self, key, item):
        """
        Adds an item in the cache

        Args:
            key: Key to be used as an index
            item: Item to be stored
        Returns:
            nothing if the key and item is none
        """
        if key is not None and item is not None:
            # If key exists, remove it from order to update its position
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
        """Gets an item from the cache by key, updating order for LRU"""
        if key in self.cache_data:
            # Move accessed key to the end of the order list
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
