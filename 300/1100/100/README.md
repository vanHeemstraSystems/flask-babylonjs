# 100 - Introduction

[Flask](https://palletsprojects.com/p/flask/) is a lightweight Python web framework that provides valuable tools and features for creating web applications in the Python Language. 

[SQLAlchemy](https://www.sqlalchemy.org/) is an SQL toolkit offering efficient and high-performing relational database access. It provides ways to interact with several database engines, such as SQLite, MySQL, and PostgreSQL. It gives you access to the database’s SQL functionalities. It also gives you an Object Relational Mapper (ORM), which allows you to make queries and handle data using simple Python objects and methods. 

[Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/) is a Flask extension that makes using SQLAlchemy with Flask easier, providing you with tools and techniques to interact with your database in your Flask applications through SQLAlchemy.

[Flask-Migrate](https://flask-migrate.readthedocs.io/en/latest/index.html) is a Flask extension based on the [Alembic](https://alembic.sqlalchemy.org/en/latest/) library, allowing you to manage database migrations.

Database migration is transferring data between different database schemas without any data loss. It’s commonly used to upgrade a database, change its schema by adding new table columns or relationships, and ensure a smooth transition with minimal downtime and no data loss.

For example, if you have a table called ```Product``` with a list of product names and want to add a price column to this table, you can use database migration to add the price column without losing the existing product data.

In this tutorial, you’ll use Flask-Migrate with Flask-SQLAlchemy to perform ```database schema migrations``` to modify your tables and preserve data.

## 100 - Prerequisites

- For A local Python 3 programming environment, follow the tutorial for your distribution in [How To Install and Set Up a Local Programming Environment for Python 3](https://www.digitalocean.com/community/tutorial_series/how-to-install-and-set-up-a-local-programming-environment-for-python-3) series. In this tutorial, we’ll call our project directory ```flask_app```.

- An understanding of basic Flask concepts, such as routes, view functions, and templates. If you are not familiar with Flask, check out [How to Create Your First Web Application Using Flask and Python](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3) and [How to Use Templates in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-templates-in-a-flask-application).

- An understanding of basic HTML concepts. Review our [How To Build a Website with HTML](https://www.digitalocean.com/community/tutorial_series/how-to-build-a-website-with-html) tutorial series.

- Understand basic Flask-SQLAlchemy concepts, such as setting up a database, creating database models, and inserting data into the database. See [How to Use Flask-SQLAlchemy to Interact with Databases in a Flask Application](https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application) for background knowledge.