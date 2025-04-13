from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    basics_sensor_data_share = get_package_share_directory('perception_ros2')
    rviz_config_file = os.path.join(basics_sensor_data_share, 'rviz', 'yolo_person_follower.rviz')


    return LaunchDescription([
        DeclareLaunchArgument(
            'rviz_config',
            default_value=rviz_config_file,
            description='Path to rviz config file'
        ),

        LogInfo(
            msg=['RViz config file: ', rviz_config_file]
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', LaunchConfiguration('rviz_config')],
            output='screen'
        ),

        Node(
            package='advanced_perception',
            executable='yolo_object_detection.py',
            name='yolo_object_detection',
            output='screen'
        ),

        Node(
            package='advanced_perception',
            executable='yolo_person_follower.py',
            name='yolo_person_follower',
            output='screen'
        ),
    ])
