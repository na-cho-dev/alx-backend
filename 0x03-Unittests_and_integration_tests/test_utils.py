#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from unittest.mock import Mock, patch
from utils import access_nested_map
from parameterized import parameterized, parameterized_class
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: Dict,
        path: Tuple[str],
        expected: Union[Dict, int]
    ) -> None:
        """
        A method to test that access_nested_map returns
        what it is supposed to.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
