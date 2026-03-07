# 🤖 MechaPrime — Autonomous Mobile Robot

A ROS2-based differential drive robot simulated in Gazebo with full teleop control, twist_mux priority handling, and ros2_control integration.

---

## ✨ Features

- Differential drive with `diff_drive_controller`
- Gazebo Ignition simulation
- Twist multiplexer for multi-input velocity control
- Joystick and keyboard teleop support
- Safety lock mechanism via `twist_mux`

---

## 📦 Packages

| Package | Description |
|---------|-------------|
| `mechaprime_description` | URDF, meshes, Gazebo config |
| `mechaprime_controller` | Controllers, twist_mux, teleop config |

---

## 🚀 Quick Start

### 1. Clone and Build
    git clone https://github.com/robovision2210/mechaprime_ws.git
    cd mechaprime_ws
    colcon build
    source install/setup.bash

### 2. Launch Gazebo
    ros2 launch mechaprime_description gazebo.launch.py

### 3. Launch Controllers
    ros2 launch mechaprime_controller controller.launch.py

### 4. Launch Teleop and Twist Mux
    ros2 launch mechaprime_controller joystick.launch.py

### 5. Keyboard Control
    ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args -r cmd_vel:=/key_vel

---

## 🛠️ Tech Stack

| Tool | Version |
|------|---------|
| ROS2 | Humble |
| Gazebo | Ignition Fortress |
| Ubuntu | 22.04 |
| ros2_control | diff_drive_controller |
| twist_mux | velocity multiplexer |

---

## 👤 Author

**Sesha Sai Jagadeswar Patnala**
Robotics and Mechatronics Engineer
https://github.com/robovision2210
