from swagger_server.configLoader import ConfigurationLoader

__data = {}

def __initData():
    data = {}
    __data["de"] = ConfigurationLoader("de")

def getConfigurationData(language):
    return __data[language]

__initData()