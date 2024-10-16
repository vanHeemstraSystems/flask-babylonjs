#!/usr/bin/env python
from app.extensions import db

def seed_data(Model, Seed):
    print("Seed Data for " + str(Model))
    if not Model.query.first():
        Seed()
        # db.session.add(Model(...))
        # db.session.commit()
        print(str(Model) + " seeded")

def init_db(Models, Seeds):
    print("Initializing database")
    db.create_all()
    for i in range(len(Models)):
       seed_data(Models[i], Seeds[i])
