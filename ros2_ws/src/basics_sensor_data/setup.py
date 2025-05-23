from setuptools import setup
import os
from glob import glob

package_name = 'basics_sensor_data'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
         (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
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
        'mona_lisa_approach = basics_sensor_data.mona_lisa_approach:main',
        'color_detector = basics_sensor_data.color_detector:main',
        'point_cloud_marker = basics_sensor_data.point_cloud_marker:main',        
        
        ],
    },
)
