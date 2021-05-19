from parktiv_server.configLoader import ConfigurationLoader
import logging

__data = {}

def __initData():
    languages = "de"

    logging.info("Initialize data")
    __data[languages] = ConfigurationLoader(languages)
    logging.info("Initialize finished for languages {}".format(languages))

def getConfigurationData(language):
    return __data[language]

__initData()