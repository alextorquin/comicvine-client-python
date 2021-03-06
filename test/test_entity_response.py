# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import comicvine_client
from comicvine_client.models.entity_response import EntityResponse  # noqa: E501
from comicvine_client.rest import ApiException

class TestEntityResponse(unittest.TestCase):
    """EntityResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test EntityResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.entity_response.EntityResponse()  # noqa: E501
        if include_optional :
            return EntityResponse(
                status_code = 102, 
                error = 'Error in URL Format', 
                number_of_total_results = 0, 
                number_of_page_results = 0, 
                results = null
            )
        else :
            return EntityResponse(
        )

    def testEntityResponse(self):
        """Test EntityResponse"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
