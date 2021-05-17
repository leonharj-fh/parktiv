# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util
import re


class Role(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, title: str=None, description: str=None):  # noqa: E501
        """Role - a model defined in Swagger

        :param id: The id of this Role.  # noqa: E501
        :type id: str
        :param title: The title of this Role.  # noqa: E501
        :type title: str
        :param description: The description of this Role.  # noqa: E501
        :type description: str
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'description': str
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'description': 'description'
        }

        self._id = id
        self._title = title
        self._description = description

    @classmethod
    def from_dict(cls, dikt) -> 'Role':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Role of this Role.  # noqa: E501
        :rtype: Role
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Role.


        :return: The id of this Role.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Role.


        :param id: The id of this Role.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501
        if id is not None and len(id) < 1:
            raise ValueError("Invalid value for `id`, length must be greater than or equal to `1`")  # noqa: E501
        if id is not None and not re.search(r'^[a-zA-Z0-9_-]{1,30}$', id):  # noqa: E501
            raise ValueError("Invalid value for `id`, must be a follow pattern or equal to `/^[a-zA-Z0-9_-]{1,30}$/`")  # noqa: E501

        self._id = id

    @property
    def title(self) -> str:
        """Gets the title of this Role.

        Title  # noqa: E501

        :return: The title of this Role.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this Role.

        Title  # noqa: E501

        :param title: The title of this Role.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def description(self) -> str:
        """Gets the description of this Role.

        Short description of the character  # noqa: E501

        :return: The description of this Role.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this Role.

        Short description of the character  # noqa: E501

        :param description: The description of this Role.
        :type description: str
        """

        self._description = description
