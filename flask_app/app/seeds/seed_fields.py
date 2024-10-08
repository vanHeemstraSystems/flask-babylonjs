#!/usr/bin/env python
from app.extensions import db
from app.models.field import Field

def seed_fields():
    fields = [1,2,3,4,5,6,7,8,9,10,
              11,12,13,14,15,16,17,18,19,20,
              21,22,23,24,25,26,27,28,29,30,
              31,32,33,34,35,36,37,38,39,40,
              41,42,43,44,45,46,47,48,49,50,
              51,52,53,54,55,56]
    
    # Clear existing data (optional)
    db.session.query(Field).delete()
    db.session.commit()
    
    for number in fields:
        field = Field(number=number)
        db.session.add(field)

    db.session.commit()
    print("Fields seeded!")