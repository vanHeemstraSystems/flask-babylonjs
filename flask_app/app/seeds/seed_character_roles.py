#!/usr/bin/env python
from app.extensions import db
from app.models.character_role import CharacterRole

def seed_character_roles():
    # Clear existing data (optional)
    db.session.query(CharacterRole).delete()
    db.session.commit()

    # Create new character roles
    new_character_role = CharacterRole(name="Antagonist", description="Opposes the protagonist, creating conflict and challenges throughout the story.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Protagonist", description="The central character who drives the narrative, facing obstacles and seeking growth.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Mentor", description="Guides and advises the protagonist, sharing wisdom and experience to aid their journey.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Love Interest", description="Provides emotional depth and romantic tension, influencing the protagonist's motivations.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Sidekick", description="Supports the protagonist with loyalty and humor, often providing comic relief and assistance.")
    db.session.add(new_character_role)
    db.session.commit() 

    new_character_role = CharacterRole(name="Foil", description="Contrasts with the protagonist to highlight their traits and decisions.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Anti-Hero", description="A flawed protagonist who lacks traditional heroic qualities but still engages the audience.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Confidant", description="A trusted character to whom the protagonist reveals thoughts and feelings, aiding character development.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Villain", description="A more malevolent antagonist, embodying evil and creating significant obstacles.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Catalyst", description="Instigates change or prompts action in the protagonist's journey.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Narrator", description="Provides the story's perspective, guiding the audience through the events.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Damsel in Distress", description="A character who needs rescue, often motivating the protagonist's actions.")
    db.session.add(new_character_role)
    db.session.commit()

    new_character_role = CharacterRole(name="Trickster", description="Uses wit and cunning to create chaos or challenge other characters, often with humorous intent.")
    db.session.add(new_character_role)
    db.session.commit()

    print("Character roles seeded!")   

