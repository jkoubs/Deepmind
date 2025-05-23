from setuptools import setup
import os
from glob import glob

package_name = 'advanced_perception'


setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.xml')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),  # Add this line to include .py launch files
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),  # Add this line to include .rviz files
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='user',
    maintainer_email='user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'yolo_object_detection = advanced_perception.yolo_object_detection:main',
            'yolo_person_follower = advanced_perception.yolo_person_follower:main',
            'yolo_pose_estimation = advanced_perception.yolo_pose_estimation:main',
            'yolo_segmentation = advanced_perception.yolo_segmentation:main',
            'fruit_mask_saver = advanced_perception.fruit_mask_saver:main'
        ],
    },
    scripts=[
        'advanced_perception/yolo_object_detection.py',
        'advanced_perception/yolo_person_follower.py',
        'advanced_perception/yolo_pose_estimation.py',
        'advanced_perception/yolo_segmentation.py',
        'advanced_perception/fruit_mask_saver.py'
    ],
)
