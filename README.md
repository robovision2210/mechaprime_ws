# Mechaprime WS 🚀

ROS2 workspace for **Mechaprime autonomous robot**.

## Quickstart
\`\`\`bash
source /opt/ros/humble/setup.bash
cd mechaprime_ws
colcon build --symlink-install
source install/setup.bash
ros2 launch mechaprime_description gazebo.launch.py
\`\`\`

## Packages
- \`mechaprime_controller\` → Joy teleop, controllers
- \`mechaprime_description\` → URDF, Gazebo models/worlds

## Launch Files
- \`ros2 launch mechaprime_description display.launch.py\` → RViz
- \`ros2 launch mechaprime_controller joystick.launch.py\` → Teleop
