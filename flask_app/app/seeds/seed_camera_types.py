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

    for name in camera_types:
        camera_type = CameraType(name=name)
        db.session.add(camera_type)

    db.session.commit()
    print("Camera types seeded!")