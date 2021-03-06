# coding: utf-8

"""
    ComicVine API

    OpenAPI specification for the ComicVine API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from comicvine_client.configuration import Configuration


class Person(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'int',
        'name': 'str',
        'aliases': 'str',
        'api_detail_url': 'str',
        'description': 'str',
        'deck': 'str',
        'site_detail_url': 'str',
        'date_added': 'str',
        'date_last_updated': 'str',
        'image': 'Image',
        'birth': 'str',
        'count_of_issue_appearances': 'int',
        'gender': 'int',
        'story_arc_credits': 'list[object]',
        'volume_credits': 'list[Volume]',
        'issue_credits': 'list[Issue]',
        'country': 'str',
        'created_characters': 'object',
        'death': 'date',
        'email': 'str',
        'hometown': 'str',
        'website': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'aliases': 'aliases',
        'api_detail_url': 'api_detail_url',
        'description': 'description',
        'deck': 'deck',
        'site_detail_url': 'site_detail_url',
        'date_added': 'date_added',
        'date_last_updated': 'date_last_updated',
        'image': 'image',
        'birth': 'birth',
        'count_of_issue_appearances': 'count_of_issue_appearances',
        'gender': 'gender',
        'story_arc_credits': 'story_arc_credits',
        'volume_credits': 'volume_credits',
        'issue_credits': 'issue_credits',
        'country': 'country',
        'created_characters': 'created_characters',
        'death': 'death',
        'email': 'email',
        'hometown': 'hometown',
        'website': 'website'
    }

    def __init__(self, id=None, name=None, aliases=None, api_detail_url=None, description=None, deck=None, site_detail_url=None, date_added=None, date_last_updated=None, image=None, birth=None, count_of_issue_appearances=None, gender=None, story_arc_credits=None, volume_credits=None, issue_credits=None, country=None, created_characters=None, death=None, email=None, hometown=None, website=None, local_vars_configuration=None):  # noqa: E501
        """Person - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._aliases = None
        self._api_detail_url = None
        self._description = None
        self._deck = None
        self._site_detail_url = None
        self._date_added = None
        self._date_last_updated = None
        self._image = None
        self._birth = None
        self._count_of_issue_appearances = None
        self._gender = None
        self._story_arc_credits = None
        self._volume_credits = None
        self._issue_credits = None
        self._country = None
        self._created_characters = None
        self._death = None
        self._email = None
        self._hometown = None
        self._website = None
        self.discriminator = None

        self.id = id
        if name is not None:
            self.name = name
        if aliases is not None:
            self.aliases = aliases
        if api_detail_url is not None:
            self.api_detail_url = api_detail_url
        if description is not None:
            self.description = description
        if deck is not None:
            self.deck = deck
        if site_detail_url is not None:
            self.site_detail_url = site_detail_url
        if date_added is not None:
            self.date_added = date_added
        if date_last_updated is not None:
            self.date_last_updated = date_last_updated
        if image is not None:
            self.image = image
        if birth is not None:
            self.birth = birth
        if count_of_issue_appearances is not None:
            self.count_of_issue_appearances = count_of_issue_appearances
        if gender is not None:
            self.gender = gender
        if story_arc_credits is not None:
            self.story_arc_credits = story_arc_credits
        if volume_credits is not None:
            self.volume_credits = volume_credits
        if issue_credits is not None:
            self.issue_credits = issue_credits
        if country is not None:
            self.country = country
        if created_characters is not None:
            self.created_characters = created_characters
        if death is not None:
            self.death = death
        if email is not None:
            self.email = email
        if hometown is not None:
            self.hometown = hometown
        if website is not None:
            self.website = website

    @property
    def id(self):
        """Gets the id of this Person.  # noqa: E501

        Unique ID for the entity.  # noqa: E501

        :return: The id of this Person.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Person.

        Unique ID for the entity.  # noqa: E501

        :param id: The id of this Person.  # noqa: E501
        :type id: int
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def name(self):
        """Gets the name of this Person.  # noqa: E501

        Name for the entity  # noqa: E501

        :return: The name of this Person.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Person.

        Name for the entity  # noqa: E501

        :param name: The name of this Person.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def aliases(self):
        """Gets the aliases of this Person.  # noqa: E501

        List of aliases the entity is known by. A \\n (newline) seperates each alias.  # noqa: E501

        :return: The aliases of this Person.  # noqa: E501
        :rtype: str
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        """Sets the aliases of this Person.

        List of aliases the entity is known by. A \\n (newline) seperates each alias.  # noqa: E501

        :param aliases: The aliases of this Person.  # noqa: E501
        :type aliases: str
        """

        self._aliases = aliases

    @property
    def api_detail_url(self):
        """Gets the api_detail_url of this Person.  # noqa: E501

        URL pointing to the entity detail resource.  # noqa: E501

        :return: The api_detail_url of this Person.  # noqa: E501
        :rtype: str
        """
        return self._api_detail_url

    @api_detail_url.setter
    def api_detail_url(self, api_detail_url):
        """Sets the api_detail_url of this Person.

        URL pointing to the entity detail resource.  # noqa: E501

        :param api_detail_url: The api_detail_url of this Person.  # noqa: E501
        :type api_detail_url: str
        """

        self._api_detail_url = api_detail_url

    @property
    def description(self):
        """Gets the description of this Person.  # noqa: E501

        Description of the entity.  # noqa: E501

        :return: The description of this Person.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Person.

        Description of the entity.  # noqa: E501

        :param description: The description of this Person.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def deck(self):
        """Gets the deck of this Person.  # noqa: E501

        Brief summary of the Entity.  # noqa: E501

        :return: The deck of this Person.  # noqa: E501
        :rtype: str
        """
        return self._deck

    @deck.setter
    def deck(self, deck):
        """Sets the deck of this Person.

        Brief summary of the Entity.  # noqa: E501

        :param deck: The deck of this Person.  # noqa: E501
        :type deck: str
        """

        self._deck = deck

    @property
    def site_detail_url(self):
        """Gets the site_detail_url of this Person.  # noqa: E501

        URL pointing to the concept on Giant Bomb.  # noqa: E501

        :return: The site_detail_url of this Person.  # noqa: E501
        :rtype: str
        """
        return self._site_detail_url

    @site_detail_url.setter
    def site_detail_url(self, site_detail_url):
        """Sets the site_detail_url of this Person.

        URL pointing to the concept on Giant Bomb.  # noqa: E501

        :param site_detail_url: The site_detail_url of this Person.  # noqa: E501
        :type site_detail_url: str
        """

        self._site_detail_url = site_detail_url

    @property
    def date_added(self):
        """Gets the date_added of this Person.  # noqa: E501

        Date the entity was added to Comic Vine.  # noqa: E501

        :return: The date_added of this Person.  # noqa: E501
        :rtype: str
        """
        return self._date_added

    @date_added.setter
    def date_added(self, date_added):
        """Sets the date_added of this Person.

        Date the entity was added to Comic Vine.  # noqa: E501

        :param date_added: The date_added of this Person.  # noqa: E501
        :type date_added: str
        """

        self._date_added = date_added

    @property
    def date_last_updated(self):
        """Gets the date_last_updated of this Person.  # noqa: E501

        Date the entity was last updated on Comic Vine.  # noqa: E501

        :return: The date_last_updated of this Person.  # noqa: E501
        :rtype: str
        """
        return self._date_last_updated

    @date_last_updated.setter
    def date_last_updated(self, date_last_updated):
        """Sets the date_last_updated of this Person.

        Date the entity was last updated on Comic Vine.  # noqa: E501

        :param date_last_updated: The date_last_updated of this Person.  # noqa: E501
        :type date_last_updated: str
        """

        self._date_last_updated = date_last_updated

    @property
    def image(self):
        """Gets the image of this Person.  # noqa: E501


        :return: The image of this Person.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Person.


        :param image: The image of this Person.  # noqa: E501
        :type image: Image
        """

        self._image = image

    @property
    def birth(self):
        """Gets the birth of this Person.  # noqa: E501

        A date, if one exists, that the person was born on. Not an origin date.  # noqa: E501

        :return: The birth of this Person.  # noqa: E501
        :rtype: str
        """
        return self._birth

    @birth.setter
    def birth(self, birth):
        """Sets the birth of this Person.

        A date, if one exists, that the person was born on. Not an origin date.  # noqa: E501

        :param birth: The birth of this Person.  # noqa: E501
        :type birth: str
        """

        self._birth = birth

    @property
    def count_of_issue_appearances(self):
        """Gets the count_of_issue_appearances of this Person.  # noqa: E501

        Number of issues this person appears in.  # noqa: E501

        :return: The count_of_issue_appearances of this Person.  # noqa: E501
        :rtype: int
        """
        return self._count_of_issue_appearances

    @count_of_issue_appearances.setter
    def count_of_issue_appearances(self, count_of_issue_appearances):
        """Sets the count_of_issue_appearances of this Person.

        Number of issues this person appears in.  # noqa: E501

        :param count_of_issue_appearances: The count_of_issue_appearances of this Person.  # noqa: E501
        :type count_of_issue_appearances: int
        """

        self._count_of_issue_appearances = count_of_issue_appearances

    @property
    def gender(self):
        """Gets the gender of this Person.  # noqa: E501

        Gender of the person. Available options are: Male (1), Female (2), Other (3)  # noqa: E501

        :return: The gender of this Person.  # noqa: E501
        :rtype: int
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this Person.

        Gender of the person. Available options are: Male (1), Female (2), Other (3)  # noqa: E501

        :param gender: The gender of this Person.  # noqa: E501
        :type gender: int
        """
        allowed_values = [1, 2, 3]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and gender not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def story_arc_credits(self):
        """Gets the story_arc_credits of this Person.  # noqa: E501

        List of story arcs this person appears in.  # noqa: E501

        :return: The story_arc_credits of this Person.  # noqa: E501
        :rtype: list[object]
        """
        return self._story_arc_credits

    @story_arc_credits.setter
    def story_arc_credits(self, story_arc_credits):
        """Sets the story_arc_credits of this Person.

        List of story arcs this person appears in.  # noqa: E501

        :param story_arc_credits: The story_arc_credits of this Person.  # noqa: E501
        :type story_arc_credits: list[object]
        """

        self._story_arc_credits = story_arc_credits

    @property
    def volume_credits(self):
        """Gets the volume_credits of this Person.  # noqa: E501


        :return: The volume_credits of this Person.  # noqa: E501
        :rtype: list[Volume]
        """
        return self._volume_credits

    @volume_credits.setter
    def volume_credits(self, volume_credits):
        """Sets the volume_credits of this Person.


        :param volume_credits: The volume_credits of this Person.  # noqa: E501
        :type volume_credits: list[Volume]
        """

        self._volume_credits = volume_credits

    @property
    def issue_credits(self):
        """Gets the issue_credits of this Person.  # noqa: E501


        :return: The issue_credits of this Person.  # noqa: E501
        :rtype: list[Issue]
        """
        return self._issue_credits

    @issue_credits.setter
    def issue_credits(self, issue_credits):
        """Sets the issue_credits of this Person.


        :param issue_credits: The issue_credits of this Person.  # noqa: E501
        :type issue_credits: list[Issue]
        """

        self._issue_credits = issue_credits

    @property
    def country(self):
        """Gets the country of this Person.  # noqa: E501

        Country the person resides in.  # noqa: E501

        :return: The country of this Person.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Person.

        Country the person resides in.  # noqa: E501

        :param country: The country of this Person.  # noqa: E501
        :type country: str
        """

        self._country = country

    @property
    def created_characters(self):
        """Gets the created_characters of this Person.  # noqa: E501

        Comic characters this person created.  # noqa: E501

        :return: The created_characters of this Person.  # noqa: E501
        :rtype: object
        """
        return self._created_characters

    @created_characters.setter
    def created_characters(self, created_characters):
        """Sets the created_characters of this Person.

        Comic characters this person created.  # noqa: E501

        :param created_characters: The created_characters of this Person.  # noqa: E501
        :type created_characters: object
        """

        self._created_characters = created_characters

    @property
    def death(self):
        """Gets the death of this Person.  # noqa: E501

        Date this person died on.  # noqa: E501

        :return: The death of this Person.  # noqa: E501
        :rtype: date
        """
        return self._death

    @death.setter
    def death(self, death):
        """Sets the death of this Person.

        Date this person died on.  # noqa: E501

        :param death: The death of this Person.  # noqa: E501
        :type death: date
        """

        self._death = death

    @property
    def email(self):
        """Gets the email of this Person.  # noqa: E501

        The email of this person.  # noqa: E501

        :return: The email of this Person.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Person.

        The email of this person.  # noqa: E501

        :param email: The email of this Person.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def hometown(self):
        """Gets the hometown of this Person.  # noqa: E501

        City or town the person resides in.  # noqa: E501

        :return: The hometown of this Person.  # noqa: E501
        :rtype: str
        """
        return self._hometown

    @hometown.setter
    def hometown(self, hometown):
        """Sets the hometown of this Person.

        City or town the person resides in.  # noqa: E501

        :param hometown: The hometown of this Person.  # noqa: E501
        :type hometown: str
        """

        self._hometown = hometown

    @property
    def website(self):
        """Gets the website of this Person.  # noqa: E501

        URL to the person website.  # noqa: E501

        :return: The website of this Person.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Person.

        URL to the person website.  # noqa: E501

        :param website: The website of this Person.  # noqa: E501
        :type website: str
        """

        self._website = website

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Person):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Person):
            return True

        return self.to_dict() != other.to_dict()
