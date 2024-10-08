#!/usr/bin/env python
from app.extensions import db
from app.models.camera_type import CameraType

def seed_camera_types():
    # Clear existing data (optional)
    db.session.query(CameraType).delete()
    db.session.commit()

    # Create new camera types
    new_camera_type = CameraType(name="FollowCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="ArcRotateCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="FreeCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="UniversalCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()


    new_camera_type = CameraType(name="TargetCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="UniversalCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="DeviceOrientationCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="TouchCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="AnaglyphCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="VRDeviceOrientationCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()                    

    new_camera_type = CameraType(name="WebXRCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit() 

    print("Camera types seeded!")     