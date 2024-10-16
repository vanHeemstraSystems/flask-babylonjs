#!/usr/bin/env python
from app.extensions import db

def seed_data(Model, Seed):
    if not Model.query.first():
        print("Seed Data for " + str(Model))
        Seed()
        print(str(Model) + " seeded")

def init_db(Models, Seeds):
    print("Initializing database")
    db.create_all()
    for i in range(len(Models)):
       seed_data(Models[i], Seeds[i])
