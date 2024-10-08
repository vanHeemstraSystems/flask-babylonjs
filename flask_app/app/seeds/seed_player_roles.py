#!/usr/bin/env python
from app.extensions import db
from app.models.player_role import PlayerRole

def seed_player_roles():
    # Clear existing data (optional)
    db.session.query(PlayerRole).delete()
    db.session.commit()

    # Create new player roles
    new_player_role = PlayerRole(name="Product Owner", description="Defines the product vision, prioritizes the backlog, and ensures the team delivers value to stakeholders.")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Scrum Master", description="Facilitates the agile process, removes obstacles, and supports the team in following agile principles.")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Security Engineer", description="Ensuring security is part of the development process from the beginning (DevSecOps).")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Architect", description="Establishing the overall architecture and design principles for the project.")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="DevOps Engineer", description="A member of the development team responsible for designing, building, and testing the software.")
    db.session.add(new_player_role)
    db.session.commit()

    new_player_role = PlayerRole(name="Stakeholder", description="Individual with an interest in the project, providing input and feedback.")
    db.session.add(new_player_role)
    db.session.commit()              

    new_player_role = PlayerRole(name="Agile Coach", description="Guides teams in adopting agile practices and improving their processes.")
    db.session.add(new_player_role)
    db.session.commit()   

    new_player_role = PlayerRole(name="UX/UI Designer", description="Focuses on user experience and interface design, ensuring the product meets user needs.")
    db.session.add(new_player_role)
    db.session.commit() 

    new_player_role = PlayerRole(name="Quality Assurance Engineer", description="Ensures the product meets quality standards through testing and validation.")
    db.session.add(new_player_role)
    db.session.commit()   

    new_player_role = PlayerRole(name="Infrastructure Engineer", description="Overseeing the deployment and management of servers, networks, and cloud services.")
    db.session.add(new_player_role)
    db.session.commit()       

    print("Player roles seeded!")      