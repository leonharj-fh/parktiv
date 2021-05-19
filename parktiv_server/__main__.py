#!/usr/bin/env python3

import connexion
from parktiv_server import encoder

def main():
	options = {"swagger_ui": False}
	# app = connexion.FlaskApp(__name__, specification_dir='./swagger/', server='tornado')
	app = connexion.FlaskApp(__name__, specification_dir='./swagger/', server="gevent")
	app.app.json_encoder = encoder.JSONEncoder
	app.add_api('swagger.yaml', arguments={'title': 'Parktiv'}, options=options, validate_responses=True)
	app.run(port=8080)


if __name__ == '__main__':
	main()
