# How to use Backstage Web Framework
Here we will see how we can use Backstage Web Framework for RESTful services. This repo contains an apis folder, which contains xml files with instructions how to handle the rest. 

# Dependencies
- backstage - The backstage web framework library.
- lxml - The library that is used to parse the XML work file 
- gunicorn - Backstage can be started as a simple WSGI server and a Gunicorn server with multiple instances
- sqlalchemy- SQLAlchemy is the Python SQL toolkit and Object Relational Mapper taht we are going to use for SQL.


# Installation
```console
$ pip install -r requirements.txt
```
### Running the server
```console
$ backstage_serve simple apis/ <host> <port> --settings=<absolute-path-to-settings-file>
```
