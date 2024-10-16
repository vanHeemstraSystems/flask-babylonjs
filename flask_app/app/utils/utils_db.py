#!/usr/bin/env python
from app.extensions import db

def seed_data(Model, Seed):
    if not Model.query.first():
        print("Seed Data for " + str(Model))
        Seed()
        print(str(Model) + " seeded")

def init_db(Models, Seeds):
    print("Initializing database")
    # drop_table('profile') # Fails
    db.create_all()
    for i in range(len(Models)):
       seed_data(Models[i], Seeds[i])

# Call with: drop_table('mytablename')
def drop_table(table_name, db=db):
    Base = db.declarative_base()
    metadata = db.MetaData()
    metadata.reflect(bind=db)
    # table = metadata.tables[table_name]
    # if table is not None:
    #     print("Dropping table " + str(table_name))
    #     Base.metadata.drop_all(db, [table], checkfirst=True)
    #     print("Dropped table " + str(table_name))