## 400 - Step 03: Adding Flask-Migrate to Your Application

In this step, you will modify your ```flask_app/app/__init__.py``` application file to add Flask-Migrate and use it to manage your Flask-SQLAlchemy database.

```
#!/usr/bin/env python
from flask_migrate import Migrate
...
```
flask_app/app/\_\_init__.py

You import the ```Migrate``` class from the ```flask_migrate``` package.

After the db declaration, you use the Migrate class to initiate a migration instance called ```migrate```.

Pass ```migrate``` to the Flask ```app``` instance and the ```db``` database instance,like so:

```
...
from flask_migrate import Migrate
... 
    ##
    # Migrate database
    ##

    migrate = Migrate(app,db)
...
```
flask_app/app/\_\_init__.py

Flask-Migrate provides a ```flask db``` command helper to manage your database.

To finish setting up Flask-Migrate and add support to your current project, use the following command in your flask_app directory:

```
 (.venv) flask_app $ flask db init
```

You will receive output similar to the following:

```
  Creating directory '/usr/local/opt/code/flask-babylonjs/flask_app/migrations' ...  done
  Creating directory '/usr/local/opt/code/flask-babylonjs/flask_app/migrations/versions' ...  done
  Generating /usr/local/opt/code/flask-babylonjs/flask_app/migrations/script.py.mako ...  done
  Generating /usr/local/opt/code/flask-babylonjs/flask_app/migrations/env.py ...  done
  Generating /usr/local/opt/code/flask-babylonjs/flask_app/migrations/README ...  done
  Generating /usr/local/opt/code/flask-babylonjs/flask_app/migrations/alembic.ini ...  done
  Please edit configuration/connection/logging settings in '/usr/local/opt/code/flask-babylonjs/flask_app/migrations/alembic.ini' before proceeding.
```

This creates a new migrations directory inside your ```flask_app``` folder, where all the migration scripts that manage your migrations will be stored.

If you are familiar with Alembic and want to add advanced configurations to your database migration system, you can modify the generated ```migrations/alembic.ini``` file. For our purposes, we will leave it as is.

**NOTE**: The ```migrations``` directory contains files that manage your app’s database migrations, and they must be added to your version control repository with the rest of your app’s code.

With Flask-Migrate connected to your application, you will perform an initial database migration. Using the ```User``` class will create the ```users``` table you declared earlier.

## Creating the Users Table using a Migration Script

You will now perform your first migration, creating your database’s ```users``` table.

In your ```flask_app``` directory, run the following command. This flask db migrate command detects all the new tables or modifications you perform on your Flask-SQLAlchemy database models.

The ```-m``` flag allows you to specify a short message describing the modification you performed:

```
(.venv) flask_app $ flask db migrate -m "initial migration"
```


MORE