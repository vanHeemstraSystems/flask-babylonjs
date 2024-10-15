# 200 - Step 01 - Installing the Required Python Packages

In this step, you’ll install the necessary packages for your application.

In your flask_app directory, activate your virtual environment from within the ```flask_app``` directory:

```
$ cd flask_app
$ . .venv/bin/activate
```

With your virtual environment activated, use pip to install Flask, Flask-SQLAlchemy, and Flask-Migrate (here: these are stored in ```flask_app/requirements.txt```):

```
$ cd flask_app
$ pip install -r requirements.txt
```

Once the installation has finished, the output will print a line similar to the following:

```
OutputSuccessfully installed Flask-2.2.3 Flask-Migrate-3.1.0 Flask-SQLAlchemy-3.0.2 Jinja2-3.1.2 Mako-1.3.0 MarkupSafe-2.1.3 Werkzeug-2.2 alembic-1.12.1 blinker-1.7.0 click-8.1.7 greenlet-3.0.1 itsdangerous-2.1.2 sqlalchemy-2.0.23 typing-extensions-4.8.0
```

With the required Python packages installed, you’ll set up an example database and model next.