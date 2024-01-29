#!/usr/bin/env python3
"""
testing the gitclient should be a-OK
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from parameterized import parameterized_class
from client import GithubOrgClient
from urllib.error import HTTPError
from fixtures import *


class TestGithubOrgClient(unittest.TestCase):
    """
    test client
    """
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch("client.get_json", return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """
        test GithubOrgClient.org
        """