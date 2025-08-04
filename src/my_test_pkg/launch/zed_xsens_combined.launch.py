from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    zed_launch_path = os.path.join(
        get_package_share_directory('zed_wrapper'),
        'launch',
        'zed_camera.launch.py'
    )

    xsens_launch_path = os.path.join(
        get_package_share_directory('xsens_mti_ros2_driver'),
        'launch',
        'xsens_mti_node.launch.py'
    )

    zed_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(zed_launch_path),
        launch_arguments={'camera_model': 'zed2i'}.items()
    )

    xsens_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(xsens_launch_path)
    )

    hr_data_node = Node(
        package='my_test_pkg',
        executable='hr_pub',
        name='hr_data_node'
    )
    return LaunchDescription([
        zed_launch,
        xsens_launch,
  #      hr_data_node
    ])

