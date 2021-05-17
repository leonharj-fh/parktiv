import connexion
import six

from swagger_server.models.animal_response import AnimalResponse  # noqa: E501
from swagger_server.models.animal_with_task import AnimalWithTask  # noqa: E501
from swagger_server.models.parks_response import ParksResponse  # noqa: E501
from swagger_server.models.role_response import RoleResponse  # noqa: E501
from swagger_server import util
from flask import abort
from flask_parameter_validation import ValidateParameters, Route, Form, Query
from typing import List, Optional


@ValidateParameters()
def animals_memory_random_get(size: int = Query(min_int=0, max_int=100, default=5),  Accept_Language: Optional[str] = Form("de")):  # noqa: E501
    """Retrieve a random list of animal ids

    Retrieve a random list of animals. Each animal id is returned twice. # noqa: E501

    :param size: 
    :type size: int
    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: List[str]
    """
    return 'do some magic!'

@ValidateParameters()
def get_animal(identifier: str = Route(pattern="^[a-zA-Z0-9_-]{1,30}$"), roleId: str = Route(pattern="^[a-zA-Z0-9_-]{1,30}$"), Accept_Language: Optional[str] = Form("de")):  # noqa: E501
    """Get a specific animal including the task

    Get a specific animal including the task # noqa: E501

    :param identifier: Identifier to get an animal information
    :type identifier: str
    :param roleId: 
    :type roleId: str
    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: AnimalWithTask
    """
    return 'do some magic!'


def list_animal(Accept_Language=None):  # noqa: E501
    """List of all available animals with exercises

    List of all available animals with exercises # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: AnimalResponse
    """
    return 'do some magic!'


def list_park(Accept_Language=None):  # noqa: E501
    """List of parks containing a QR-Code

    List of parks containing a QR-Code # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: ParksResponse
    """
    return 'do some magic!'


def roles_get(Accept_Language=None):  # noqa: E501
    """List of roles which can be chosen to complete different exersices

    List of roles which can be chosen to complete different exersices # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: RoleResponse
    """
    return 'do some magic!'
