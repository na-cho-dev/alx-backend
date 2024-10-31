#!/usr/bin/python3
"""
LFU Caching
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    A LFU caching system that inherits from BaseCaching with LFU eviction.
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.freq = {}
        self.order = []

    def put(self, key, item):
        """
        Adds an item in the cache

        Args:
            key: Key to be used as an index
            item: Item to be stored
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.freq.values())
                candidates = [k for k,
                              freq in self.freq.items() if freq == min_freq]

                if len(candidates) > 1:
                    for candidate in self.order:
                        if candidate in candidates:
                            discard = candidate
                            break
                else:
                    discard = candidates[0]

                del self.cache_data[discard]
                del self.freq[discard]
                self.order.remove(discard)
                print("DISCARD:", discard)

            self.cache_data[key] = item
            self.freq[key] = 1
            self.order.append(key)

    def get(self, key):
        """Gets an item from the cache by key, updating frequency for LFU"""
        if key in self.cache_data:
            self.freq[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None