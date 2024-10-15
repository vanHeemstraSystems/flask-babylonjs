# 500 - Conclusion

You have created a small Flask application with a database and integrated it with Flask-Migrate. You learned to modify your database models, upgrade them to a new version, and downgrade them to a previous version.

In general, you can take the following steps to manage your database migrations as you develop your Flask applications:

1) Modify the database models.

2) Generate a migration script with the ```flask db migrate -m "some comment"``` command.

3) Review the generated migration script and correct it if necessary.

4) Apply the changes to the database with the ```flask db upgrade``` command.

5) To restore a previous database version, use the ```flask db downgrade``` command.

See the [Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) documentation for more information.