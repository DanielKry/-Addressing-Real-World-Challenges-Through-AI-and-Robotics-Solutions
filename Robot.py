#my project simulates an automatic sorting system using camera detection to detect colours 
#and objects in a simulated manufactring/logistics in a simulated environmnet
#Importing modules
from controller import Robot, DistanceSensor, Motor, PositionSensor

# Define the time step for the simulation
TIME_STEP = 32

# Different states of the robot
class State:
    WAITING = 0
    GRASPING = 1
    ROTATING = 2
    RELEASING = 3
    ROTATING_BACK = 4

# Initialise the robot and set initial parameters
robot = Robot()
counter = 0
state = State.WAITING
speed = 2.0

# Define motors for hand and arm movements
hand_motors = [robot.getDevice("finger_1_joint_1"),
               robot.getDevice("finger_2_joint_1"),
               robot.getDevice("finger_middle_joint_1")]

ur_motors = [robot.getDevice("shoulder_lift_joint"),
             robot.getDevice("elbow_joint"),
             robot.getDevice("wrist_1_joint"),
             robot.getDevice("wrist_2_joint")]

# Set initial velocities for arm motors
for motor in ur_motors:
    motor.setVelocity(speed)

# Initialise distance sensor and enable it
distance_sensor = robot.getDevice("distance sensor")
distance_sensor.enable(TIME_STEP)

# Initialise position sensor for wrist joint and enable it
position_sensor = robot.getDevice("wrist_1_joint_sensor")
position_sensor.enable(TIME_STEP)

# Add camera initialisation
camera = robot.getDevice("camera")
camera.enable(2 * TIME_STEP)
camera.recognitionEnable(2 * TIME_STEP)

# Define target positions for different colored objects
#[x,y,z,w] coordinates in a 3d environment
# coordiantes on where to drop specific objects
target_positions_red = [-1.88, -4.0, -2.38, -1.51]
target_positions_green = [-1.88, 2.14, -2.38, -1.51]
target_positions_blue = [-1.88, -1.14, -2.38, -1.51]
target_positions_foreign = [0, -1.14, -2.38, -1.51]

# Main control loop
while robot.step(TIME_STEP) != -1:
    # Counter logic to manage time delays between actions
    foreign_color = True #Any colour that is no green red or blue will be defined as 
    #foreign colour

    # Camera recognition code
    if counter <= 0:
        if state == State.WAITING:
            # Transition to GRASPING state when an object is within a certain distance
            if distance_sensor.getValue() < 500:
                state = State.GRASPING
                counter = 8
                print("Grasping object")
                for motor in hand_motors:
                    motor.setPosition(0.85)

        elif state == State.GRASPING:
            # Camera colour recognition code
            colors = camera.getRecognitionObjects()# Retrieves the list of objects 
            #reconised by the camera
            target_positions = None  # Initialise target_positions variable 
            #outside the loop

            # Identify the colour of the detected object
            for color in colors:
                color_rgb = color.getColors()#This gets the RGB values of the
                #current object.
                red, green, blue = color_rgb[0], color_rgb[1], color_rgb[2]
                # Set target positions based on detected colour
                # This section uses RGB values to determine the colour of the objects
                #If the conditions are not met it assumes its a foreign object
                # based on the detected colour, it sets the target poition variable to
                #the corresponding  list of positions
                if red > 0.8 and green < 0.2 and blue < 0.2:  # Red
                    print("Detected Red object")
                    target_positions = target_positions_red
                elif red < 0.2 and green < 0.2 and blue > 0.8:  # Blue
                    print("Detected Blue object")
                    target_positions = target_positions_blue
                elif red < 0.2 and green > 0.8 and blue < 0.2:  # Green
                    print("Detected Green object")
                    target_positions = target_positions_green
                elif foreign_color:  # Set foreign_color to True for any other color
                    print("Detected foreign object")
                    target_positions = target_positions_foreign

            # Move the robot arm based on the detected colour
            if target_positions is not None:
                for i in range(4):
                    ur_motors[i].setPosition(target_positions[i])
                print("Rotating arm")
                state = State.ROTATING

        elif state == State.ROTATING:
            # Rotate the arm back after reaching a certain position
            if position_sensor.getValue() < -2.3:
                counter = 8
                print("Releasing object")
                state = State.RELEASING
                for motor in hand_motors:
                    motor.setPosition(motor.getMinPosition())

        elif state == State.RELEASING:
            # Release the object by resetting arm positions
            for motor in ur_motors:
                motor.setPosition(0.0)
            print("Rotating arm back")
            state = State.ROTATING_BACK

        elif state == State.ROTATING_BACK:
            # Transition back to WAITING state after arm rotation
            if position_sensor.getValue() > -0.1:
                state = State.WAITING
                print("Waiting for object")

    #Counter for managing time delays
    counter -= 1

# Cleanup after the main loop
robot.cleanup()
