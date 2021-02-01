# Poke Trader

Poke Trader is a public platform to evaluate trade Pokemons. 
The idea was developed on **Python Django REST / React** technologies with 
the use of Postgres database. 

The main features follow the goal of searching a Pokemon to compare their 
potential against to the others. So here you'll find the following features:

 - Comparison between two groups of pokemons:
 - Save a verified Trade
 - List all saved trades

**Link to the frontend application**: :rocket: 

[https://bx-poketrader.herokuapp.com/][https://bx-poketrader.herokuapp.com/]

 ## Table of contents
* **[Requirements](#requirements)**
* **[Install](#Install with docker)**
* **[Tests](#Running Tests)**
* **[Endpoints](#endpoints)**

# Requirements

If you use docker, just go to the next step. If don't:

 - Python3
 - Pip3
 - virutalenv
 - postgres

```shell
$ virutalenv env -p python3
```

```shell
$ source env/bin/activate
```

```shell
$ cd poke_trader_backend
```

```shell
$ pip install -r requirements.txt
```

```shell
$ python manage.py migrate
```

```shell
$ python manage.py runserver
```

# Install with docker

You'll need to have installed in your machine:

-   [Docker](https://www.docker.com/)
-   [docker-compose](https://docs.docker.com/compose/)

```
$ cd poke_trader_backend
```
```
$ docker-compose up
```
# Running Tests
This platform is tested by unit tests, integration tests and **BDD** tests. 
The last one was thought to cover the backend as a black-box and verify if all components works well together. 
You can use the .feature files as a requirement artifact to understand how the system behaves against some use 
scenarios.

The command bellow run all tests (unit, integration and BDD):

```
$ make docker-test
```

# Endpoints

    - POST - /trade/verify/
    - POST - /trade/save/
    - GET - /trade/

From the `.feature` files it is possible to consult more information about the format of the requests for each 
endpoint. Some example of a body request are listed below:

    {"right_side": [
      {"name": "Charmander", "base_experience": 100, "image": "url"
    }
      ], "left_side": [
          {"name": "Charmander", "base_experience": 100, "image": "url"
          }
      ], "result": ""
    }