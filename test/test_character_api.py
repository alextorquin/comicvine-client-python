# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import comicvine_client
from comicvine_client.api.character_api import CharacterApi  # noqa: E501
from comicvine_client.rest import ApiException


class TestCharacterApi(unittest.TestCase):
    """CharacterApi unit test stubs"""

    def setUp(self):
        self.api = comicvine_client.api.character_api.CharacterApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_character(self):
        """Test case for get_character

        Get a particular character  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()