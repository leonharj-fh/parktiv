# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.task import Task
from swagger_server import util
import re


class AnimalWithTask(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, title: str=None, image: str=None, task: Task=None):  # noqa: E501
        """AnimalWithTask - a model defined in Swagger

        :param id: The id of this AnimalWithTask.  # noqa: E501
        :type id: str
        :param title: The title of this AnimalWithTask.  # noqa: E501
        :type title: str
        :param image: The image of this AnimalWithTask.  # noqa: E501
        :type image: str
        :param task: The task of this AnimalWithTask.  # noqa: E501
        :type task: Task
        """
        self.swagger_types = {
            'id': str,
            'title': str,
            'image': str,
            'task': Task
        }

        self.attribute_map = {
            'id': 'id',
            'title': 'title',
            'image': 'image',
            'task': 'task'
        }

        self._id = id
        self._title = title
        self._image = image
        self._task = task

    @classmethod
    def from_dict(cls, dikt) -> 'AnimalWithTask':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The AnimalWithTask of this AnimalWithTask.  # noqa: E501
        :rtype: AnimalWithTask
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this AnimalWithTask.


        :return: The id of this AnimalWithTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this AnimalWithTask.


        :param id: The id of this AnimalWithTask.
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
        """Gets the title of this AnimalWithTask.


        :return: The title of this AnimalWithTask.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this AnimalWithTask.


        :param title: The title of this AnimalWithTask.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501
        if title is not None and len(title) < 1:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `1`")  # noqa: E501

        self._title = title

    @property
    def image(self) -> str:
        """Gets the image of this AnimalWithTask.

        Url to the image  # noqa: E501

        :return: The image of this AnimalWithTask.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image: str):
        """Sets the image of this AnimalWithTask.

        Url to the image  # noqa: E501

        :param image: The image of this AnimalWithTask.
        :type image: str
        """

        self._image = image

    @property
    def task(self) -> Task:
        """Gets the task of this AnimalWithTask.


        :return: The task of this AnimalWithTask.
        :rtype: Task
        """
        return self._task

    @task.setter
    def task(self, task: Task):
        """Sets the task of this AnimalWithTask.


        :param task: The task of this AnimalWithTask.
        :type task: Task
        """
        if task is None:
            raise ValueError("Invalid value for `task`, must not be `None`")  # noqa: E501

        self._task = task
