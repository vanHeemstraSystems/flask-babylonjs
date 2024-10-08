#!/usr/bin/env python
from app.extensions import db
from app.models.camera_type import CameraType

def seed_camera_types():
    # Clear existing data (optional)
    db.session.query(CameraType).delete()
    db.session.commit()

    # Create new camera types
    new_camera_type = CameraType(name="FollowCamera", description="This camera is designed to follow a target object while maintaining a specified distance and angle from it. It's useful for scenarios like third-person character controls.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="ArcRotateCamera", description="This camera revolves around a target point, simulating an orbiting behavior. It's commonly used for 3D visualization, architectural walkthroughs, and camera animations.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="FreeCamera", description="This camera allows the user to navigate the scene using keyboard and mouse controls freely. It provides a first-person perspective and is often used in games and interactive applications.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="UniversalCamera", description="It is a versatile camera that combines features of different camera types, such as free movement and optional automatic collision avoidance.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="TargetCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="UniversalCamera", description="This camera is controlled by the keyboard, mouse, touch, or gamepad depending on the input device used, with no need for the controller to be specified. This extends and replaces the Free Camera, the Touch Camera and the Gamepad Camera, which are all still available.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="DeviceOrientationCamera", description="This is a camera designed to react to a device being tilted forward or back and left or right.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="TouchCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="AnaglyphCamera", description="Extending the use of the Universal and Arc Rotate Cameras for use with red and cyan 3D glasses.")
    db.session.add(new_camera_type)
    db.session.commit()

    new_camera_type = CameraType(name="VRDeviceOrientationCamera", description="A newer set of cameras that extend the cameras above to handle device orientation from a VR device.")
    db.session.add(new_camera_type)
    db.session.commit()                    

    new_camera_type = CameraType(name="WebXRCamera", description="...")
    db.session.add(new_camera_type)
    db.session.commit() 

    print("Camera types seeded!")     