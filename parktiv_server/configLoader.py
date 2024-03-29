import yaml
import os
from pathlib import Path

animalFileName = "animals.yaml"
parkFileName = "parks.yaml"
roleFileName = "roles.yaml"

animalSchemaFileName = "animals.schema.yaml"
parkSchemaFileName = "parks.schema.yaml"
roleSchemaFileName = "roles.schema.yaml"

__staticImageFolder = os.path.join("static","images")

def __transformAnimalsImageUrl(animalDict):
    for animal in animalDict["animals"]:
        if "image" in animal and "url" in animal["image"]:
            animal["image"]["url"] = os.path.join(__staticImageFolder, animal["image"]["url"])
    return animalDict

def getAnimalsConfig(language):
    return getFileAsYaml(os.path.join(__getConfigFolder(language), animalFileName))
    # TODO add filepath really necessary is it will be a web resource / vs \
    # return __transformAnimalsImageUrl(animalDict)

def getAnimalsSchema():
    return getFileAsYaml(os.path.join(__getSchemaFolder(), animalSchemaFileName))

def getParksConfig(language):
    return getFileAsYaml(os.path.join(__getConfigFolder(language), parkFileName))

def getParksSchema():
    return getFileAsYaml(os.path.join(__getSchemaFolder(), parkSchemaFileName))

def getRolesConfig(language):
    return getFileAsYaml(os.path.join(__getConfigFolder(language), roleFileName))

def getRolesSchema():
    return getFileAsYaml(os.path.join(__getSchemaFolder(), roleSchemaFileName))

def __getConfigFolder(language):
    return os.path.join(Path(__file__).parent, "config", language)

def __getSchemaFolder():
    return os.path.join(Path(__file__).parent, "schemas")

def getFileAsYaml(fileName):
    with open(fileName, 'r', encoding="UTF-8") as stream:
        try:
            return yaml.load(stream, Loader=yaml.SafeLoader)
        except yaml.YAMLError as exception:
            raise exception


class ConfigurationLoader(object):

    def __init__(self, language):
        assert language is not None
        self.language = language
        self.animalsData = getAnimalsConfig(language)
        self.rolesData = getRolesConfig(language)
        self.parksData = getParksConfig(language)
