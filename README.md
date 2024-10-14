flask-babylonjs
# Flask BabylonJS

> Slugline

Based on "How To Structure a Large Flask Application with Flask Blueprints and Flask-SQLAlchemy" at https://www.digitalocean.com/community/tutorials/how-to-structure-a-large-flask-application-with-flask-blueprints-and-flask-sqlalchemy

Based on "Flask SQLAlchemy" at https://github.com/vanHeemstraSystems/flask-sqlalchemy/

Based on "Factory Pattern" at https://github.com/vanHeemstraSystems/factory-pattern

Based on "Text-Based Entity Relationship Diagrams with Mermaid.js" at https://newdevsguide.com/2023/04/08/creating-erds-with-mermaid/

Based on "TailwindsCSS Getting Started" at https://tailwindcss.com/docs/installation

Based on "FlowBite" at https://github.com/themesberg/flowbite

Based on "Flowbite + Tailwind CSS Crash Course | Learn Flowbite for React & Next.js (Full Tutorial)" at https://www.youtube.com/watch?v=FTNBPSPy6P8

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
5) Run: ```$ npm install```
6) Set the Flask App to app directory: ```(.venv) $ export FLASK_APP=app```
7) Set the Flask Environment to True for development: ```(.venv) $ export FLASK_DEBUG=True```
8) Set the SQLAlchemy Database URI: ```(.venv) $ export SQLALCHEMY_DATABASE_URI=...```, default is ```sqlite:///app.db```
9) Set SQLAlchemy Track Modifications: ```(.venv) $ export SQLALCHEMY_TRACK_MODIFICATIONS=True```
10) Set Secret Key: ```(.venv) $ export SECRET_KEY=********```
11) Run the flask app: ```(.venv) $ flask run```
12) Open the web interface as prompted
13) Use ```CTRL+c``` to exit the web server.
14) Alternatively run the flask command line interface: ```(.venv) $ flask shell```
15) Execute any flask commands: >>>
16) Use ```exit()``` to exit from the command line interface.

## 100 - Introduction

See [README.md](./100/README.md)

## 200 - Requirements

See [README.md](./200/README.md)

## 300 - Building Our Application

See [README.md](./300/README.md)

## 400 - Conclusion

See [README.md](./400/README.md)
