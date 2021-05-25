import logging

import connexion
from flask_testing import TestCase

from parktiv_server.encoder import JSONEncoder

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.FlaskApp(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app