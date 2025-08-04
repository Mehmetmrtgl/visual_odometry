from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    zed_launch = os.path.join(
        get_package_share_directory('zed_wrapper'),
        'launch',
        'zed_camera.launch.py'
    )

    xsens_launch = os.path.join(
        get_package_share_directory('xsens_mti_ros2_driver'),
        'xsens_mti_node.launch.py'
    )

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(zed_launch),
            launch_arguments={'camera_model': 'zed2i'}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(xsens_launch)
        )
    ])
