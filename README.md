## About

This repo contains all the services being used by ew-ui. `ew-api` is built using Django and deployed on heroku.

## Prerequisites

- Python 3.9+
- PostgreSQL 13+

## Setup Local environment

1. Create virtual environment

    `python3 -m venv <your environment name>`

2. `cd` into your virtual environment which you just created and run below command -

    `source env\Scripts\activate`

3. Install `Django` and `Django REST framework` into the virtual environment.

    ```
    pip install django

    pip install djangorestframework
    ```

4. Local Database setup

Follow the tutorial below to set up the postgres on your machine.

> https://www.postgresqltutorial.com/install-postgresql

## Configure PEP8 and Pylint

1. If you are using VS Code for development you should install `Python` extension developed by Microsoft.
2. Add below configuration to your user settings JSON file.

```
"python.formatting.autopep8Path": "<Path to your virtual environment directory>\\Scripts\\autopep8",
"python.linting.pylintPath": "<Path to your virtual environment directory>\\Scripts\\pylint",
"python.linting.pylintArgs": [
    "--load-plugins=pylint_django",
    "--disable=django-not-configured",
    "--django-settings-module=bookandstayapi.settings",
]
```
3. If you are being prompt to install `autopep8` and `pylint` then go ahead and do so.

## Contribution

Your PR should be raised against `develop` branch, and it should have naming convention in the format `ew-api-#`, where `#` denotes the issue number you want to work.