#!/usr/bin/env python
from app.extensions import db
from app.models.field_type import FieldType

def seed_field_types():
    # Clear existing data (optional)
    db.session.query(FieldType).delete()
    db.session.commit()

    # Create new field types
    new_field_type = FieldType(name="Go", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Portfolio", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Programs", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Plans", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Product Portfolio", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Product Vision", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Business Impact, Principles, Values", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Product Mission", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Goals", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Objectives", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Targets", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="What (Ends)", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="How (Means)", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Strategies", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Initiatives, Tactics", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Research", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Opportunities", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Ideas", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Solutions", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Refine", description="...")
    db.session.add(new_field_type)
    db.session.commit()

    new_field_type = FieldType(name="Epics, Themes", description="...")
    db.session.add(new_field_type)
    db.session.commit()                                

    new_field_type = FieldType(name="Features", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Stories", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Tasks", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Refactor", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Operations", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Company Mission", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="Company Values", description="...")
    db.session.add(new_field_type)
    db.session.commit()     

    new_field_type = FieldType(name="Company Purpose", description="...")
    db.session.add(new_field_type)
    db.session.commit() 

    new_field_type = FieldType(name="...", description="...")
    db.session.add(new_field_type)
    db.session.commit()     

    print("Field types seeded!")     