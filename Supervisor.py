from controller import Supervisor
import random

# Create the supervisor
supervisor = Supervisor()

# List of available shapes in Webots
available_shapes = ["Cube", "Cube2", "Cube3", "Cube4", "Cube5", "Cube6","Cube7", "Cube8", "Cube9", "Cube10", "Cube11", "Cube12"]

# Define specific positions for each cube
cube_positions = {
    "Cube": [6.83, -0.82, 0.96],
    "Cube1": [6.83, -0.82, 0.96],
    "Cube2": [6.83, -0.82, 0.96],
    "Cube3": [6.83, -0.82, 0.96],
    "Cube4": [6.83, -0.82, 0.96],
    "Cube5": [6.83, -0.82, 0.96],
    "Cube6": [6.83, -0.82, 0.96],
    "Cube7": [6.83, -0.82, 0.96],
    "Cube8": [6.83, -0.82, 0.96],
    "Cube9": [6.83, -0.82, 0.96],
    "Cube10": [6.83, -0.82, 0.96],
    "Cube11": [6.83, -0.82, 0.96],
    "Cube12": [6.83, -0.82, 0.96],
}

# Loop and spawn a new random cube every 2 seconds
while True:

    # Wait for 2 seconds
    supervisor.step(time_step=8000)

    # Spawn a new random cube
    random_shape = random.choice(available_shapes)
    obj = supervisor.getFromDef(random_shape)

    if obj is not None:

        # Set position for the cube
        if random_shape in cube_positions:
            obj.getField("translation").setSFVec3f(cube_positions[random_shape])
            print(f"Object {random_shape} spawned successfully at {cube_positions[random_shape]}.")

        else:
            print(f"No specific position defined for {random_shape}. Using random position.")
            obj.getField("translation").setSFVec3f([0, 0, 0])  # Default to (0, 0, 0)
            
while supervisor.step(32) != -1:
    # Your simulation logic goes here
    pass

