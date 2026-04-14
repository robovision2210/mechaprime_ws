import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    serial_port = LaunchConfiguration("serial_port")

    serial_port_arg = DeclareLaunchArgument(
        "serial_port",
        default_value="/dev/ttyUSB0",
        description="Serial port for ESP32"
    )

    lidar_driver = Node(
        package="rplidar_ros",
        executable="rplidar_node",
        name="rplidar_node",
        parameters=[{
            "channel_type": "serial",
            "serial_port": serial_port,
            "serial_baudrate": 115200,
            "frame_id": "lidar_sensor_link",
            "inverted": False,
            "angle_compensate": True,
            "scan_mode": "Sensitivity",
            "range_min": 0.05
        }],
        output="screen"
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(
            get_package_share_directory("mechaprime_localization"),
            "rviz",
            "global_localization.rviz"   # ✅ Fix #3: .rviz not .launch.py
        )],
        output="screen",                          # ✅ Fix #1: moved inside Node
        parameters=[{"use_sim_time": False}]      # ✅ Fix #1: moved inside Node
    )

    controller = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(           # ✅ Fix #2: wrapped correctly
            os.path.join(
                get_package_share_directory("mechaprime_controller"),
                "launch",
                "controller.launch.py"
            )
        )
    )

    return LaunchDescription([
        serial_port_arg,
        lidar_driver,
        rviz,
        controller,  # ← add when ready
    ])