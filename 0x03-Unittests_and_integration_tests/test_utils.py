#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map
from parameterized import parameterized, parameterized_class


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for utils.access_nested_map function

    >>> nested_map = {"a": {"b": {"c": 1}}}
    >>> access_nested_map(nested_map, ["a", "b", "c"])
    1
    """
    @parameterized.expand([
        ({"a": {"b": {"c": 1}}}, ["a", "b", "c"], 1),
        ({"x": {"y": {"z": 5}}}, ["x", "y", "z"], 5),
        ({"key": {"inner_key": "value"}}, ["key", "inner_key"], "value"),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        A method to test that access_nested_map returns
        what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
