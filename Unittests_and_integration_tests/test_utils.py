#!/usr/bin/env python3
"""
Unittests for utils.py
"""
import unittest
from unittest import TestCase
from unittest.mock import patch
from unittest import mock
from parameterized import parameterized
from utils import memoize

class TestAccessNestedMap(TestCase):
    """
        Test access to nested map method
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, map, path, expected):
        """
        Test access to nested map method
        """
        from utils import access_nested_map
        self.assertEqual(access_nested_map(map, path), expected)

        @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b")),
    ])