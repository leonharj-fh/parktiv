# coding: utf-8

import yaml
import os

from swagger_server.models.animal_response import AnimalResponse
from swagger_server.models.parks_response import ParksResponse
from swagger_server.models.role_response import RoleResponse

from jsonschema import validate
from pathlib import Path


def getFileAsYaml(fileName):
    with open(fileName, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exception:
            raise exception

def checkUniqueIdsInFile(dict, key):
    assert dict[key]

    ids = list(map(lambda x : x['id'], dict[key]))
    assert len(ids) >= 1
    assert len(ids) == len(set(ids))


class TestParkController():

    def test_animals_schema_get(self):
        rootDir = Path(__file__).parent.parent

        yaml = getFileAsYaml(os.path.join(rootDir,"config","animals","de","animals.yaml"))
        schema = getFileAsYaml(os.path.join(rootDir,"schemas","animals.schema.yaml"))
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "animals")

        response = AnimalResponse.from_dict(yaml)
        assert response
        assert type(response.animals) == list
        assert response.animals[0].id

    def test_parks_schema_get(self):
        rootDir = Path(__file__).parent.parent

        yaml = getFileAsYaml(os.path.join(rootDir,"config","parks","de","parks.yaml"))
        schema = getFileAsYaml(os.path.join(rootDir,"schemas","parks.schema.yaml"))
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "parks")

        response = ParksResponse.from_dict(yaml)
        assert response
        assert type(response.parks) == list
        assert response.parks[0].id


    def test_roles_schema_get(self):
        rootDir = Path(__file__).parent.parent

        yaml = getFileAsYaml(os.path.join(rootDir,"config","roles","de","roles.yaml"))
        schema = getFileAsYaml(os.path.join(rootDir,"schemas","roles.schema.yaml"))
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "roles")

        response = RoleResponse.from_dict(yaml)
        assert response
        assert type(response.roles) == list
        assert response.roles[0].id


    def test_animals_role_relation_exists(self):
        rootDir = Path(__file__).parent.parent

        yamlAnimals = getFileAsYaml(os.path.join(rootDir,"config","animals","de","animals.yaml"))
        yamlRoles = getFileAsYaml(os.path.join(rootDir,"config","roles","de","roles.yaml"))

        roleIds = list(map(lambda x : x['id'], yamlRoles["roles"]))

        for animal in yamlAnimals["animals"]:
            animalRoleIds = list(map(lambda x : x['roleId'], animal["tasks"]))
            assert len(animalRoleIds) > 0
            assert set(roleIds) == set(animalRoleIds)
            #assert all(elem in roleIds for elem in animalRoleIds)


    def test_parse_to_objects(self):
        rootDir = Path(__file__).parent.parent
        yamlAnimals = getFileAsYaml(os.path.join(rootDir,"config","animals","de","animals.yaml"))


