#!/usr/bin/env python
from app.extensions import db
from app.models.character_type import CharacterType

def seed_character_types():
    # Clear existing data (optional)
    db.session.query(CharacterType).delete()
    db.session.commit()

    # Create new character types
    new_character_type = CharacterType(name="Innocent", description="Seeks safety and happiness, often embodying purity and optimism.")
    db.session.add(new_character_type)
    db.session.commit()

    new_character_type = CharacterType(name="Orphan", description="Represents a sense of loss and seeks belonging and connection.")
    db.session.add(new_character_type)
    db.session.commit()  

    new_character_type = CharacterType(name="Hero", description="Embodies courage and determination, striving to prove worth through challenges.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Caregiver", description="Nurtures and protects others, driven by compassion and selflessness.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Explorer", description="Values freedom and discovery, seeking new experiences and adventure.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Rebel", description="Challenges authority and norms, advocating for change and revolution.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Lover", description="Pursues passion and intimacy, focused on relationships and emotional connections.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Creator", description="Innovates and expresses through art, driven by imagination and vision.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Jester", description="Brings joy and humor, often using wit to challenge seriousness.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Sage", description="Pursues wisdom and knowledge, guiding others with insight and understanding.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Magician", description="Transforms situations through insight and vision, creating change and possibility.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Ruler", description="Seeks control and order, driven by a desire for power and leadership.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Heroine", description="A female counterpart to the Hero, embodying strength and resilience.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Mentor", description="Guides and supports others, sharing knowledge and experience.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Trickster", description="Uses cunning and cleverness to navigate challenges, often blurring boundaries.")
    db.session.add(new_character_type)
    db.session.commit() 

    new_character_type = CharacterType(name="Destroyer", description="Represents chaos and change, often breaking down the old to make way for the new.")
    db.session.add(new_character_type)
    db.session.commit() 

    print("Character types seeded!")     