# 200 - Creating and Interacting with the Scene Model

In large applications, you may have hundreds of database tables, which means you would need to write hundreds of SQLAlchemy models to manage them. Putting all your models in one file will make your application hard to maintain, so you will split your models into separate Python files inside a models directory. Each file will hold the models and functions related to a specific part of your application. For example, you may put models and functions for managing scenes inside a scene.py file in a directory called models in the app directory.

At this point in the tutorial, your flask_app directory structure is as follows (excluding the virtual environment’s directory):

```
.
├── flask_app
|    ├── .venv
|    ├── app
|    |   ├── __init__.py
|    |   ├── extensions.py
|    |   ├── main
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── scenes
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   ├── questions
|    |   │   ├── __init__.py
|    |   │   └── routes.py
|    |   └── templates
|    |       ├── base.html
|    |       ├── index.html
|    |       ├── scenes
|    |       |   ├── shots.html
|    |       |   └── index.html
|    |       └── questions
|    |           └── index.html
|    ├── config.py
|    ├── instance
|    |   └── app.db
|    └── requirements.txt
└── README.md
```

To create a database model for scenes in its own file, first create a directory called ```models``` inside your ```app``` directory:

```
(.venv) gitpod /workspace/flask-babylonjs/flask_app (main) $ mkdir app/models
```

Then, open a new file called ```scene.py``` inside your ```models``` directory:

```
(.venv) gitpod /workspace/flask-babylonjs/flask_app (main) $ nano app/models/scene.py
```

Add the following code to the newly created file:

```
#!/usr/bin/env python
from app.extensions import db

class Scene(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)

    def __repr__(self):
        return f'<Scene "{self.title}">'
```
flask_app/app/models/scene.py

Save and close the file.

You import the ```db``` database object from the ```app.extensions``` module. Then you create a Flask-SQLAlchemy database model called ```Scene``` using the ```db.Model``` class. In the model, you have an ID integer column as a primary key (```id```), a column to hold strings for the scene title (```title```), and a text column for content (```content```). You use the special ```__repr__()``` method to provide a string representation for each scene object using its title. For more on Flask-SQLAlchemy, you can review [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application).

Next, open the Flask shell to create the scene table based on the scene model:

```
(.venv) gitpod /workspace/flask-babylonjs/flask_app (main) $ flask shell
```

Run the following code to create the scenes table:

```
>>> from app.extensions import db
>>> from app.models.scene import Scene
>>> db.create_all()
```

You import the ```db``` object from the ```app.extensions``` module and the ```Scene``` model from the ```app.models.scene``` module. Then you use the ```create_all()``` method to create the scenes table.

The code should execute without an output. If you receive an error, check your ```app/extensions.py``` and ```app/models/scene.py``` files, and review the previous steps to ensure you have followed them as written.

**Note**: A file called ```app.db``` should appear in ```flask-app/app/instance/``` directory.

**Note**: The ```db.create_all()``` function does not recreate or update a table if it already exists. For example, if you want to modify your model by adding a new column and so you run the ```db.create_all()``` function, the change you make to the model will not be applied to the table if the table already exists in the database. The solution is to delete all existing database tables with the ```db.drop_all()``` function and then recreate them with the ```db.create_all()``` function like so:

```
>>> db.drop_all()
>>> db.create_all()
```

These commands will apply the modifications you make to your models and will delete all the existing data in the database. To update the database and preserve existing data, you’ll need to use *[schema migration](https://en.wikipedia.org/wiki/Schema_migration)*, which allows you to modify your tables and preserve data. You can use the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) extension to perform SQLAlchemy schema migrations through the Flask command-line interface.

Next, run the following code to create ten random scenes:

```
>>> from app.extensions import db 
>>> from app.models.scene import Scene
>>> import random
>>>
>>> for i in range(0, 10):
>>>    random_num = random.randrange(1, 1000)
>>>    scene = Scene(title=f'Scene #{random_num}',
>>>                content=f'Content #{random_num}')
>>>    db.session.add(scene)
>>>    print(scene)
>>>    print(scene.content)
>>>    print('--')
>>>    db.session.commit()
```

You import the ```db``` database object, the ```Scene``` database model, and the ```random``` Python module. You’ll use this module to generate random numbers to create sample scenes with different titles and contents. You use a ```for``` loop with the ```range()``` Python function to repeat a code block ten times.

In the ```for``` loop, you use the ```random.randrange()``` method to generate a random integer number between ```1``` and ```1000``` and save it to a variable called ```random_num```. You then create a scene object using the ```Scene``` model and use the random number in the ```random_num``` variable to generate a sample scene title and content.

You then add the scene object to the database session, print the object itself and its content, and commit the transaction.

You’ll receive an output similar to the following but with different numbers:

```
<Scene "Scene #923">
Content #923
--
<Scene "Scene #245">
Content #245
--
<Scene "Scene #124">
Content #124
--
<Scene "Scene #282">
Content #282
--
<Scene "Scene #130">
Content #130
--
<Scene "Scene #650">
Content #650
--
<Scene "Scene #763">
Content #763
--
<Scene "Scene #282">
Content #282
--
<Scene "Scene #423">
Content #423
--
<Scene "Scene #899">
Content #899
--
```

Each scene has a randomly generated number attached to it. These scenes will now be in your database.

Leave the Flask shell running and open a new terminal window. Source your environment and navigate to your application folder.

Now that you have some sample scenes in your table, you can display them on the scenes’ index page. First, open the scenes routes file to modify the index route:

```
(.venv) gitpod /workspace/flask-babylonjs/flask_app (main) $ nano app/scenes/routes.py
```

Edit the imports and the index route as follows:

```
#!/usr/bin/env python
from flask import render_template
from app.scenes import bp
from app.extensions import db
from app.models.scene import Scene

@bp.route('/')
def index():
    scenes = Scene.query.all()
    return render_template('scenes/index.html', scenes=scenes)

@bp.route('/shots/')
def shots():
    return render_template('scenes/shots.html')    
```
flask_app/app/scenes/routes.py

Save and close the file.

You import the ```db``` database object and the ```Scene``` model. You get all the scenes in the database and then pass them to the scenes’ index template.

Open the scenes’ index template for modification to display the scenes you passed to it:

```
(.venv) gitpod /workspace/flask-babylonjs/flask_app (main) $ nano app/templates/scenes/index.html
```

Edit the file as follows:

```
{% extends 'base.html' %}

{% block content %}
    <span class="title"><h1>{% block title %} The Scenes Page {% endblock %}</h1></span>
    <div class="content">
        <h2>This is the scenes Flask blueprint</h2>
        {% for scene in scenes %}
            <div class="scene">
                <p><b>#{{ scene.id }}</b></p>
                <p class="title">
                    <b>
                        <a href="#">
                            {{ scene.title }}
                        </a>
                    </b>
                </p>
                <div class="content">
                    <p>{{ scene.content }}</p>
                </div>
                <hr>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```
flask_app/app/templates/scenes/index.html

Save and close the file.

Here, you loop through scenes and display each scene’s ID, title, and content.

With the development server running, visit the scenes’ index page or refresh it if you have it open:

```
http://127.0.0.1:5000/scenes/
```

The sample scenes you’ve generated will be displayed on the index page, similar to the following image:

![image](https://github.com/user-attachments/assets/f7ee1c22-0c36-4fcf-b5cd-1a259e0bd05b)

You now have a database model for scenes. You can now add features to your application with new routes and templates, such as creating, editing, and deleting scenes.