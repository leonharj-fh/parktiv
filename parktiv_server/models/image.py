# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from parktiv_server.models.base_model_ import Model
from parktiv_server import util


class Image(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, url: str=None, copyright: str=None):  # noqa: E501
        """Image - a model defined in Swagger

        :param url: The url of this Image.  # noqa: E501
        :type url: str
        :param copyright: The copyright of this Image.  # noqa: E501
        :type copyright: str
        """
        self.swagger_types = {
            'url': str,
            'copyright': str
        }

        self.attribute_map = {
            'url': 'url',
            'copyright': 'copyright'
        }
        self._url = url
        self._copyright = copyright

    @classmethod
    def from_dict(cls, dikt) -> 'Image':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Image of this Image.  # noqa: E501
        :rtype: Image
        """
        return util.deserialize_model(dikt, cls)

    @property
    def url(self) -> str:
        """Gets the url of this Image.

        Server path to an image  # noqa: E501

        :return: The url of this Image.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Image.

        Server path to an image  # noqa: E501

        :param url: The url of this Image.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def copyright(self) -> str:
        """Gets the copyright of this Image.

        Copyright information for the image which must be set when displaying  # noqa: E501

        :return: The copyright of this Image.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright: str):
        """Sets the copyright of this Image.

        Copyright information for the image which must be set when displaying  # noqa: E501

        :param copyright: The copyright of this Image.
        :type copyright: str
        """

        self._copyright = copyright
