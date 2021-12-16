# coding: utf-8


from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from parktiv_server.models.base_model_ import Model
from parktiv_server import util
import re


class Task(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, role_id: str=None, exercise: str=None, audio: str=None):  # noqa: E501
        """Task - a model defined in Swagger

        :param role_id: The role_id of this Task.  # noqa: E501
        :type role_id: str
        :param exercise: The exercise of this Task.  # noqa: E501
        :type exercise: str
        :param audio: The audio of this Task.  # noqa: E501
        :type audio: str
        """
        self.swagger_types = {
            'role_id': str,
            'exercise': str,
            'audio': str
        }

        self.attribute_map = {
            'role_id': 'roleId',
            'exercise': 'exercise',
            'audio': 'audio'
        }
        self._role_id = role_id
        self._exercise = exercise
        self._audio = audio

    @classmethod
    def from_dict(cls, dikt) -> 'Task':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Task of this Task.  # noqa: E501
        :rtype: Task
        """
        return util.deserialize_model(dikt, cls)

    @property
    def role_id(self) -> str:
        """Gets the role_id of this Task.

        Task related role identifier  # noqa: E501

        :return: The role_id of this Task.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id: str):
        """Sets the role_id of this Task.

        Task related role identifier  # noqa: E501

        :param role_id: The role_id of this Task.
        :type role_id: str
        """
        if role_id is None:
            raise ValueError("Invalid value for `role_id`, must not be `None`")  # noqa: E501

        self._role_id = role_id

    @property
    def exercise(self) -> str:
        """Gets the exercise of this Task.

        Human readable description of an exercise which should be performed  # noqa: E501

        :return: The exercise of this Task.
        :rtype: str
        """
        return self._exercise

    @exercise.setter
    def exercise(self, exercise: str):
        """Sets the exercise of this Task.

        Human readable description of an exercise which should be performed  # noqa: E501

        :param exercise: The exercise of this Task.
        :type exercise: str
        """
        if exercise is None:
            raise ValueError("Invalid value for `exercise`, must not be `None`")  # noqa: E501

        self._exercise = exercise

    @property
    def audio(self) -> str:
        """Gets the audio of this Task.

        Url to an audio file which explains the exercise acoustically.  # noqa: E501

        :return: The audio of this Task.
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio: str):
        """Sets the audio of this Task.

        Url to an audio file which explains the exercise acoustically.  # noqa: E501

        :param audio: The audio of this Task.
        :type audio: str
        """

        self._audio = audio
