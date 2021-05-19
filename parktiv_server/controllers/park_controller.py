import random

import connexion
import six

from parktiv_server.models.animal_response import AnimalResponse  # noqa: E501
from parktiv_server.models.animal_with_task import AnimalWithTask  # noqa: E501
from parktiv_server.models.parks_response import ParksResponse  # noqa: E501
from parktiv_server.models.role_response import RoleResponse  # noqa: E501
import parktiv_server.controllers as controller
from parktiv_server import util
from flask import abort
from flask_parameter_validation import ValidateParameters, Route, Form, Query
from typing import List, Optional


@ValidateParameters()
def animals_memory_random_get(
    size: int = Query(min_int=0, max_int=100, default=5),
    Accept_Language: Optional[str] = Form("de"),
):  # noqa: E501
    """Retrieve a random list of animal ids

    Retrieve a random list of animals. Each animal id is returned twice. # noqa: E501

    :param size: 
    :type size: int
    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: List[str]
    """
    animals = AnimalResponse.from_dict(
        controller.getConfigurationData(Accept_Language).animalsData
    ).animals
    if size > len(animals):
        abort(409, "Parameter size must be smaller equals {}".format(len(animals)))
    animalIds = list(map(lambda animal: animal.id, animals))
    randomIds = random.sample(animalIds, k=size)

    # duplicate all ids and shuffle it again.
    return random.sample(randomIds * 2, k=len(randomIds) * 2)


@ValidateParameters()
def get_animal(
    identifier: str = Route(pattern="^[a-zA-Z0-9_-]{1,30}$"),
    roleId: str = Route(pattern="^[a-zA-Z0-9_-]{1,30}$"),
    Accept_Language: Optional[str] = Form("de"),
):  # noqa: E501
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

    animals = AnimalResponse.from_dict(
        controller.getConfigurationData(Accept_Language).animalsData
    ).animals
    oAnimal = next(filter(lambda animal: animal.id == identifier, animals), None)

    if oAnimal is None:
        abort(404, "'{}' not found.".format(identifier))

    oTask = next(filter(lambda task: task.role_id == roleId, oAnimal.tasks), None)
    if oTask is None:
        abort(404, "'{}' not found.".format(roleId))

    return AnimalWithTask(oAnimal.id, oAnimal.title, oAnimal.image, oTask)


def list_animal(Accept_Language="de"):  # noqa: E501
    """List of all available animals with exercises

    List of all available animals with exercises # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: AnimalResponse
    """
    return AnimalResponse.from_dict(
        controller.getConfigurationData(Accept_Language).animalsData
    )


def list_park(Accept_Language="de"):  # noqa: E501
    """List of parks containing a QR-Code

    List of parks containing a QR-Code # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: ParksResponse
    """
    return ParksResponse.from_dict(
        controller.getConfigurationData(Accept_Language).parksData
    )


def roles_get(Accept_Language="de"):  # noqa: E501
    """List of roles which can be chosen to complete different exersices

    List of roles which can be chosen to complete different exersices # noqa: E501

    :param Accept_Language: The desired language for response content. [RFC 2616](https://tools.ietf.org/html/rfc2616#page-104) 
    :type Accept_Language: str

    :rtype: RoleResponse
    """
    return RoleResponse.from_dict(
        controller.getConfigurationData(Accept_Language).rolesData
    )
