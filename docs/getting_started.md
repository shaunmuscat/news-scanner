# Getting Started

## Required Dependencies

- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-pip)
- [virtualenv (venv module)](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)
- [docker](https://docs.docker.com/get-docker/)

## Setup

1. Create a python virtual environment for the project named `env`
   - On macOS and Linux:
        ```
        python3 -m venv env
        ```
   - On Windows:
        ```
        py -m venv env
        ```
2. Activate the virtual environment
   - On macOS and Linux:
        ```
        source env/bin/activate
        ```
   - On Windows: 
        ```
        .\env\Scripts\activate
        ```
3. Install python packages
    ```
    pip3 install -r requirements.txt
    ```
4. Start up instance of the database using docker
    ```
    docker run --name news_scanner-orm-psql -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=usr -e POSTGRES_DB=news_scanner -p 5432:5432 -d postgres
    ```
   - When finished with the application, use the following commands to stop and remove the docker db instance:
        ```
        # stop instance
        docker stop news_scanner-orm-psql
        
        # destroy instance
        docker rm news_scanner-orm-psql
        ```
