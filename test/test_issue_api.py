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
from comicvine_client.api.issue_api import IssueApi  # noqa: E501
from comicvine_client.rest import ApiException


class TestIssueApi(unittest.TestCase):
    """IssueApi unit test stubs"""

    def setUp(self):
        self.api = comicvine_client.api.issue_api.IssueApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_issue(self):
        """Test case for get_issue

        Get a particular issue  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
