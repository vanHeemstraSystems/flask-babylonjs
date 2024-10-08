#!/usr/bin/env python
from app.extensions import db
from app.models.camera_type import CameraType

def seed_camera_types():
    camera_types = [
        'FollowCamera',
        'ArcRotateCamera',
        'FreeCamera',
        'UniversalCamera',
        'TargetCamera',
        'DeviceOrientationCamera',
        'TouchCamera',
        'AnaglyphCamera',
        'VRDeviceOrientationCamera',
        'WebXRCamera'
    ]
    
    # Clear existing data (optional)
    db.session.query(CameraType).delete()
    db.session.commit()
    
    for title in camera_types:
        camera_type = CameraType(title=title)
        db.session.add(camera_type)

    db.session.commit()
    print("Camera types seeded!")

# if __name__ == "__main__":
#     from app import create_app  # Adjust as necessary
#     app = create_app()
#     with app.app_context():
#         seed_camera_types()