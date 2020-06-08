# Getting Started

## Required Dependencies

- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [pip](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-pip)
- [virtualenv (venv module)](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv)
- [docker](https://docs.docker.com/get-docker/)

## Setup

1. Ensure all Required Dependencies are installed
2. Create a python virtual environment for the project named `env`
   - On macOS and Linux:
        ```
        python3 -m venv env
        ```
   - On Windows:
        ```
        py -m venv env
        ```
3. Activate the virtual environment
   - On macOS and Linux:
        ```
        source env/bin/activate
        ```
   - On Windows: 
        ```
        .\env\Scripts\activate
        ```
4. Install python packages
    ```
    pip3 install -r requirements.txt
    ```
5. Start up instance of the database using docker
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

## Running Tests

To run all unit tests within the tests directory, ensure setup is completed and execute the command:
```
python -m unittest
```

## Running the Application

To run the application, ensure setup is completed and the docker postgres instance is running, then execute the command:
```
python main.py
```

Notifications will be written to console when a scan occurs and added or updated news articles are discovered.

To exit the running application use the keyboard interrupt with `CTRL + C`.
