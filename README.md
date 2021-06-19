# Basic information
This is the server implementation for the game concept Memory. <br>
To keep the clients logic to a minimum this server implementation provides all information clients need. This gives us the flexibility to add/update animals, roles, images and exercises without updating clients.
---

# Workflow
* Player starts a game
* --> Client calls `GET /parks` to retrieve a list of supported parks
    * If the park is not supported the player has to choose how many cards (QR-Codes) are available.
* --> The client requests a list of cards (animals) `GET /animals/memory/random?size=4` including with how many cards.
* <-- The server returns a list of randomly sorted cards (animals) (all animals are returned twice).
* --> The client requests a list of all available roles `GET /roles`.
* --> The player can now scan QR-Codes and the client matches each QR-Code the next element in the list.
    * The client calls `GET /animals/{identifier}/task/{roleId}` using the animal's identifier and the role's identifier to get the exercise.
* Game is finished when all pairs have been found.    


# Configuration files:
All configuration files can be found in `/parktiv_server/config/<languageCode>/`
* The file `animals.yaml` holds information of animals and related exercises.
* The file `parks.yaml` holds information of parks supported by Parktiv.
* The file `roles.yaml` holds information of available roles.

# Program language:
*Python*<br> 
*Framework:* flask

# Setup:
* `pip install -r requirements.txt`
* `pip install -r test-requirements.txt (for testing)`<br>
The application `Parktiv` was tested with python versions `[3.7, 3.8, 3.9]`

# Running tests:
`cd ./parktiv` <br>
`pytest`

# Running application:
* `cd ./parktiv`
* `python -m parktiv_server`<br>

The current configuration runs a development server on port `8080`. To change port or server implementation modify `./partkiv_server/__main__.py`

# Repository
* https://github.com/leonharj-fh/parktiv (Repository is private)

# Deployment
* We use the service <https://www.digitalocean.com/> to deploy our project.
* Note: If the service is needed, please contact `Josef Leonhartsberger` <dh201816@fhstp.ac.at> (will take around 5-10 minutes to deploy the service.

# Visualizing the projects API 
* Copy the content of `parktiv_swagger_file.yaml` to the website <https://editor.swagger.io/>
* The editor shows all available endpoints which can be called

# Example Endpoint
* `http(s)://<ip-address>:<port>/parktiv/<endpoint>`
* e.g. `http(s)://localhost:8080/parktiv/animals/elephant/task/faenger`

# Info
Contact information: Josef Leonhartsberger <dh201816@fhstp.ac.at>