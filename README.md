flask-babylonjs
# Flask BabylonJS

> Slugline

Based on "How To Structure a Large Flask Application with Flask Blueprints and Flask-SQLAlchemy" at https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

Based on "Flask SQLAlchemy" at https://github.com/vanHeemstraSystems/flask-sqlalchemy/

Based on "Factory Pattern" at https://github.com/vanHeemstraSystems/factory-pattern

Based on "Text-Based Entity Relationship Diagrams with Mermaid.js" at https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/

Based on "FlowBite" at https://github.com/themesberg/flowbite

Open this URL with ```https://github.dev/``` instead of ```https://github.dev/``` to use the Visual Studio Code web-based IDE.

Run this application as follows:

1) Enter ```flask_app``` directory: ```$ cd flask_app```
2) If non-existent, create a virtual environment inside the ```flask_app``` directory: ```$ python3 -m venv .venv``` (macOS: ```$ virtualenv .venv```)

In case of the following, follow its advice:

The virtual environment was not created successfully because ensurepip is not
available.  

On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    sudo apt-get update
    sudo apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

On macOS see https://sourabhbajaj.com/mac-setup/Python/virtualenv.html


3) Start the virtual environment and enter: ```. .venv/bin/activate``` (macOS: ```source .venv/bin/activate```)
4) Run ```$ pip install -r requirements.txt```
5) Move down into the ```app``` directory: ```$ cd app``` and run: ```$ npm install```
6) Move back up into the ```flask_app``` directory: ```$ cd ../```
7) Set the Flask App to app directory: ```(.venv) $ export FLASK_APP=app```
8) Set the Flask Environment to True for development: ```(.venv) $ export FLASK_DEBUG=True```
9) Set the SQLAlchemy Database URI: ```(.venv) $ export SQLALCHEMY_DATABASE_URI=...```, default is ```sqlite:///app.db```
10) Set SQLAlchemy Track Modifications: ```(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True```
11) Set Secret Key: ```(.venv) $ export SECRET_KEY=********```
12) Run the flask app: ```(.venv) $ flask run```
13) Open the web interface as prompted
14) Use ```CTRL+c``` to exit the web server.
15) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
16) Execute any flask commands: >>>
17) Use ```exit()``` to exit from the command line interface.

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
