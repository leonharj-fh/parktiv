# coding: utf-8


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


        :return: The url of this Image.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Image.


        :param url: The url of this Image.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")  # noqa: E501

        self._url = url

    @property
    def copyright(self) -> str:
        """Gets the copyright of this Image.


        :return: The copyright of this Image.
        :rtype: str
        """
        return self._copyright

    @copyright.setter
    def copyright(self, copyright: str):
        """Sets the copyright of this Image.


        :param copyright: The copyright of this Image.
        :type copyright: str
        """
        if copyright is not None and len(copyright) < 1:
            raise ValueError("Invalid value for `copyright`, length must be greater than or equal to `1`")  # noqa: E501

        self._copyright = copyright
