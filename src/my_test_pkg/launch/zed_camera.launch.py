from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zed_wrapper',
            executable='zed_wrapper_node',
            name='zed_node',
            output='screen',
            parameters=[{
                'general.camera_model': 'zed2i',
                'general.verbose': True,
                'pos_tracking.enabled': True,
                'depth.quality': 1
            }],
            remappings=[
                # Remap ZED topics if needed
            ]
        )
    ])

