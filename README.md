# Automatic Sorting System Using AI and Robotics

This project addresses real-world challenges in manufacturing and logistics through an automated 
sorting system using the UR5e robotic arm and machine vision technology. The system identifies 
and sorts objects by color, demonstrating potential applications in recycling centers, warehouses, 
and e-commerce fulfillment centers. By simulating a manufacturing environment in Webots, the project 
showcases precise control and flexibility of the UR5e robot, integrated with advanced sensors and 
cameras. Despite challenges like potential misclassification under varying lighting conditions, 
the project illustrates the transformative potential of AI and robotics, highlighting both technical 
achievements and ethical considerations.

## Instructions to run all the code from the project:

### Running in Webots:

1. Ensure Python is installed. The most compatible version is Python 3.10.11.
2. Install Webots from the official [Webots website](https://cyberbotics.com/).
3. Ensure all required libraries for each code file are installed. These can typically be installed using PIP commands included in the files if needed.
4. Download the [World](https://github.com/DanielKry/-Addressing-Real-World-Challenges-Through-AI-and-Robotics-Solutions/blob/main/worlds/Automatic%20Sorting%20System%20Using%20AI%20and%20Robotics.wbt) and place it in the `worlds` directory.
5. Download the [controller](https://github.com/DanielKry/-Addressing-Real-World-Challenges-Through-AI-and-Robotics-Solutions/tree/main/worlds/Controllers) and place them in the `controllers` directory.
6. Open Webots and load the downloaded world file.
7. Open the code in your preferred IDE (Visual Studio Code is recommended) or directly in Webots.
8. Select the correct Python environment (Python 3.10.11).
9. Run each code segment in order, starting from the top, to avoid errors.

## What do the files do?

- **Addressing Real-World Challenges Through AI and Robotics Solutions (1).pdf**: A detailed implementation of an automatic sorting system using the UR5e robotic arm and camera detection to identify and sort objects by colour.
- **Robot.py**: Contains the code for the UR5e robot's state management, sensor and motor initialisation, camera recognition, and object handling logic.
- **Supervisor.py**: Simulates a manufacturing environment, generating custom shapes and placing them on a conveyor belt for the robot to sort.

### !!WARNING!!

This code must be run in a Webots environment due to the need for a graphical interface and simulation capabilities.

For more information or to view additional files, please message me.

Thank you for reading!
