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
from comicvine_client.models.person import Person  # noqa: E501
from comicvine_client.rest import ApiException

class TestPerson(unittest.TestCase):
    """Person unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Person
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = comicvine_client.models.person.Person()  # noqa: E501
        if include_optional :
            return Person(
                id = None, 
                name = None, 
                aliases = None, 
                api_detail_url = None, 
                site_detail_url = None, 
                date_added = None, 
                date_last_updated = None, 
                birth = None, 
                count_of_issue_appearances = None, 
                country = None, 
                created_characters = None, 
                death = None, 
                deck = None, 
                description = None, 
                email = None, 
                gender = None, 
                hometown = None, 
                image = None, 
                issue_credits = None, 
                story_arc_credits = None, 
                volume_credits = None, 
                website = None
            )
        else :
            return Person(
                id = None,
        )

    def testPerson(self):
        """Test Person"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
