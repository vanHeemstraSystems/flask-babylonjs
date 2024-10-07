

from app import db, Story  # Adjust the import based on your app structure

def seed_stories():
    # Clear existing data (optional)
    db.session.query(Story).delete()
    db.session.commit()

    # Create a new story
    new_story = Story(title="Agility", content="A story about agility and quickness in movement.")
    db.session.add(new_story)
    db.session.commit()

    print("Stories seeded!")

if __name__ == "__main__":
    from app import create_app  # Adjust as necessary
    app = create_app()
    with app.app_context():
        seed_stories()
