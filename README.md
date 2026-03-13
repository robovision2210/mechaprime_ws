# 🤖 MechaPrime — Autonomous Mobile Robot

A ROS2-based differential drive robot simulated in Gazebo with full teleop control,
twist_mux priority handling, ros2_control integration, and autonomous maze solving
via QR code navigation.

---

## ✨ Features

- Differential drive with `diff_drive_controller`
- Gazebo Ignition simulation
- Twist multiplexer for multi-input velocity control
- Joystick and keyboard teleop support
- Safety lock mechanism via `twist_mux`
- Sensor scripts for Camera, IMU, and LiDAR
- Autonomous maze solving with QR code commands
- ArUco / QR marker detection node
- Bringup package for full system launch

---

## 📦 Packages

| Package | Description |
|---------|-------------|
| `mechaprime_description` | URDF, meshes, Gazebo config |
| `mechaprime_controller` | Controllers, twist_mux, teleop config |
| `mechaprime_scripts` | Sensor nodes, maze solver, marker detection |
| `mechaprime_bringup` | Full system bringup launch |

---

## 🚀 Quick Start

### 1. Clone and Build
    git clone https://github.com/robovision2210/mechaprime_ws.git
    cd mechaprime_ws
    colcon build
    source install/setup.bash

### 2. Launch Gazebo (includes controllers)
    ros2 launch mechaprime_description gazebo.launch.py

> ⚠️ Do NOT run controller.launch.py separately — controllers are auto-spawned by gazebo.launch.py

### 3. Full System Bringup (Alternative)
    ros2 launch mechaprime_bringup simulated_robot.launch.py

### 4. Launch Teleop and Twist Mux
    ros2 launch mechaprime_controller joystick.launch.py

### 5. Keyboard Control
    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/key_vel

### 6. Read Camera Feed
    ros2 run mechaprime_scripts read_camera

### 7. Read IMU Data
    ros2 run mechaprime_scripts read_imu

### 8. Read LiDAR Data
    ros2 run mechaprime_scripts read_lidar

### 9. Autonomous Maze Solver (QR Navigation)
    ros2 run mechaprime_scripts maze_solver

> Robot reads QR codes ("left", "right", "stop") and navigates autonomously using LiDAR + IMU

### 10. Marker Detection
    ros2 run mechaprime_scripts detect_marker

---

## 🧠 Autonomous Navigation — maze_solver

| Topic | Type | Role |
|-------|------|------|
| `/camera/image_raw` | `sensor_msgs/Image` | QR code detection |
| `/scan` | `sensor_msgs/LaserScan` | Obstacle detection |
| `/imu/out` | `sensor_msgs/Imu` | Yaw-based turn control |
| `/cmd_vel` | `geometry_msgs/Twist` | Velocity output |

**QR Commands:** `left` → turn 90° left | `right` → turn 90° right | `stop` → halt

---

## 🛠️ Tech Stack

| Tool | Version |
|------|---------|
| ROS2 | Humble |
| Gazebo | Ignition Harmonic |
| Ubuntu | 22.04 |
| ros2_control | diff_drive_controller |
| twist_mux | velocity multiplexer |
| OpenCV | QR + marker detection |

---

## 👤 Author

**Sesha Sai Jagadeswar Patnala**  
Robotics and Mechatronics Engineer  
https://github.com/robovision2210
