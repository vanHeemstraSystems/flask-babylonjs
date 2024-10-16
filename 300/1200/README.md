# 1200 - Connecting with DB Hub

Based on "pydbhub" at https://pypi.org/project/pydbhub/

> A Python library for accessing and using SQLite databases on DBHub.io.

Connect our Flask SQLAlchemy database to DB Hub online for easier, centralized data management.

## 100 - What works now

- Run read-only queries (eg SELECT statements) on databases, returning the results as JSON
- Upload and download your databases
- List the databases in your account
- List the tables, views, and indexes present in a database
- List the columns in a table, view or index, along with their details
- List the branches, releases, tags, and commits for a database
- Generate diffs between two databases, or database revisions
- Download the database metadata (size, branches, commit list, etc.)
- Retrieve the web page URL of a database

## 200 - Still to do
- Anything else people suggest and seems like a good idea. Please try it out, submits PRs to extend or fix things, and report any weirdness or bugs you encounter. :smile:

## 300 - Pre-requisites

- Python version 3.7<br/>
Older Python releases should NOT be OK. Newer Python releases should be OK, but only Python 3.7 has been tested (so far).

- A DBHub.io API key<br/>
These can be generated in your Settings page, when logged in.

## 400 - Installation

```
$ pip install pydbhub
```

Or better, make it part of flask_app/requirements.txt, and run:

```
$ cd flask_app
$ pip install -r requirements.txt
```

MORE