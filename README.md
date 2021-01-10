# Poople-Trends

## Project made for ASCI: 20-21

by Prajjwal Datir
using Python3, Flask, bs4

[Problem Statement](./Problem.md)

## To run the application you can either use the flask command or python’s -m switch with Flask. Before you can do that you need to tell your terminal the application to work with by exporting the FLASK_APP environment variable.

```bash
$ export FLASK_APP=app.py
$ flask run

 * Running on http://127.0.0.1:5000/
```
### If you are on Windows, the environment variable syntax depends on command line interpreter. 

#### On Command Prompt:
```C:\path\to\app>set FLASK_APP=app.py```
And on PowerShell:
```PS C:\path\to\app> $env:FLASK_APP = "app.py"```
Alternatively you can use python -m flask:

```bash
$ export FLASK_APP=app.py
$ python -m flask run
 * Running on http://127.0.0.1:5000/
```
This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in production. For deployment options see Deployment Options.

## Now head over to http://127.0.0.1:5000/, and you should see the app running.

for more info visit [here](https://flask.palletsprojects.com/en/1.1.x/quickstart/)