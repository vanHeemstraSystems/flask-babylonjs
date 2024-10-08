#!/usr/bin/env python
from app.extensions import db
from app.models.field_type import FieldType

def seed_field_types():
    field_types = ['Go','Portfolio','Programs','Plans',
                   'Product Portfolio','Product Vision',
                   'Business Impact, Principles, Values',
                   'Product Mission','Goals','Objectives',
                   'Targets','What (Ends)','How (Means)',
                   'Strategies','Initiatives, Tactics',
                   'Research','Opportunities','Ideas','Solutions',
                   'Refine','Epics, Themes','Features','Stories',
                   'Tasks','Refactor','Operations',
                   'Company Mission','Company Values', 
                   'Company Purpose','']
    
    # Clear existing data (optional)
    db.session.query(FieldType).delete()
    db.session.commit()
    
    for name in field_types:
        field_type = FieldType(name=name)
        db.session.add(field_type)

    db.session.commit()
    print("Field types seeded!")