# fastapi-and-mongodb-crud-and-Authentication

## Features

+ Python FastAPI backend.
+ MongoDB database.
+ Authentication
+ Deployment

## Using the applicaiton

To use the application, follow the outlined steps:

1. Clone this repository and create a virtual environment in it:

```console
$ python3 -m venv venv
```

2. Install the modules listed in the `requirements.txt` file:

```console
(venv)$ pip3 install -r requirements.txt
```
3. You also need to start your mongodb instance either locally or on Docker as well as create a `.env.dev` file. See the `.env.example` for configurations.

4. Start the application:

```console
python main.py
```


The starter listens on port 8000 on address [0.0.0.0](0.0.0.0:8080). 

## Deployment

This application can be deployed on any PaaS such as [Heroku](https://heroku.com) or [Okteto](https://okteto) and any other cloud service provider.

## Contributing ?


Fork the repo, make changes and send a PR. We'll review it together!

## License

This project is licensed under the terms of MIT license.
