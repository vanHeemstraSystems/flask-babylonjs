#!/usr/bin/env python
from app.extensions import db
from app.models.light_type import LightType

def seed_light_types():
    # Clear existing data (optional)
    db.session.query(LightType).delete()
    db.session.commit()

    # Create new light types
    new_light_type = LightType(name="Point Light", description="Think light bulb.")
    db.session.add(new_light_type)
    db.session.commit()

    new_light_type = LightType(name="Directional Light", description="Think planet lit by a distant sun.")
    db.session.add(new_light_type)
    db.session.commit()

    new_light_type = LightType(name="Spot Light", description="Think of a focused beam of light.")
    db.session.add(new_light_type)
    db.session.commit()

    new_light_type = LightType(name="Hemispheric Light", description="Think of the ambient light.")
    db.session.add(new_light_type)
    db.session.commit()

    print("Light types seeded!")    