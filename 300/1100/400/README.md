## 400 - Step 03: Adding Flask-Migrate to Your Application

In this step, you will modify your ```flask_app/app/extensions.py``` application file to add Flask-Migrate and use it to manage your Flask-SQLAlchemy database.

```
#!/usr/bin/env python
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
socketio = SocketIO()
```
flask_app/app/extensions.py

You import the ```Migrate``` class from the ```flask_migrate``` package.

After the db declaration, you use the Migrate class to initiate a migration instance called ```migrate```.

Next, pass ```migrate``` to the Flask ```app``` instance and the ```db``` database instance,like so:

```
...
    # Set migrations
    migrate(app,db)
...
```
flask_app/app/\_\_init__.py




MORE