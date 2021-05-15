#!/usr/bin/env python3

import connexion
from swagger_server import encoder

def main():
	server='tornado'
	options = {"swagger_ui": False}
	app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
	app.app.json_encoder = encoder.JSONEncoder
	app.add_api('swagger.yaml', arguments={'title': 'Parktiv'}, options=options)
	app.run(port=8080)


if __name__ == '__main__':
	main()
