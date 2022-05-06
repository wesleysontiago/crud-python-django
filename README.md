# crud-python-django

## Description

User Project CRUD with Python Django, JWT and SQLite3

## Instalation

```bash
$ pip install -r requirements.txt
```

## Run Application

```bash
# Go to Directory App
$ cd appPython

# development
$ python3 manage.py runserver
```

## Swagger Documentation

After run server, access URL:

```bash
$ http://localhost:8000/
```

## Authentication

```bash
# For authentication execute:
$ curl --location --request GET 'http://localhost:8000/api/token/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
	    "username": "wesleysontiago",
	    "password": "testing123"
    }'

# development
$ python3 manage.py runserver
```

## Database

Implementated with SQLite3.
In VSCode there is an extension to view the Database, follow the link: [Extensão](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite)

## Developer

- Author - [Wesleyson Tiago](https://www.instagram.com/wesleysontiago/)
- LinkedIn - [@wesleysontiago](https://www.linkedin.com/in/wesleyson-tiago-43a06b17b/)
