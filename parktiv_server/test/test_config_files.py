# coding: utf-8

from parktiv_server.models.animal_response import AnimalResponse
from parktiv_server.models.parks_response import ParksResponse
from parktiv_server.models.role_response import RoleResponse
import parktiv_server.configLoader as loader

from jsonschema import validate

defaultLanguage = "de"

def checkUniqueIdsInFile(dict, key):
    assert dict[key]

    ids = list(map(lambda x : x['id'], dict[key]))
    assert len(ids) >= 1
    assert len(ids) == len(set(ids))

class TestParkController():

    def test_animals_schema_get(self):

        yaml = loader.getAnimalsConfig(defaultLanguage)
        schema = loader.getAnimalsSchema()
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "animals")

        response = AnimalResponse.from_dict(yaml)
        assert response
        assert type(response.animals) == list
        assert response.animals[0].id

    def test_parks_schema_get(self):
        yaml = loader.getParksConfig(defaultLanguage)
        schema = loader.getParksSchema()
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "parks")

        response = ParksResponse.from_dict(yaml)
        assert response
        assert type(response.parks) == list
        assert response.parks[0].id


    def test_roles_schema_get(self):
        yaml = loader.getRolesConfig(defaultLanguage)
        schema = loader.getRolesSchema()
        validate(yaml, schema)

        checkUniqueIdsInFile(yaml, "roles")

        response = RoleResponse.from_dict(yaml)
        assert response
        assert type(response.roles) == list
        assert response.roles[0].id


    def test_animals_role_relation_exists(self):
        yamlAnimals = loader.getAnimalsConfig(defaultLanguage)
        yamlRoles = loader.getRolesConfig(defaultLanguage)

        roleIds = list(map(lambda x : x['id'], yamlRoles["roles"]))

        for animal in yamlAnimals["animals"]:
            animalRoleIds = list(map(lambda x : x['roleId'], animal["tasks"]))
            assert len(animalRoleIds) > 0
            assert set(roleIds) == set(animalRoleIds)
            #assert all(elem in roleIds for elem in animalRoleIds)



