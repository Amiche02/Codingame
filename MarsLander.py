import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
surface = []
for i in range(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x, land_y))

# Function to check if the given position is within the landing zone
def within_landing_zone(x):
    for i in range(len(surface)-1):
        if surface[i][0] <= x <= surface[i+1][0]:
            return True
    return False

# Game loop
while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    # Calculate the desired rotation and power settings
    rotate = 0  # Keep the rotation angle at 0 for level 1
    power = 0   # Initialize the power to 0
    
    # Check if the capsule is within the landing zone
    if within_landing_zone(x):
        # Adjust the power to control the vertical speed
        if v_speed < -40:
            power = 4
        elif v_speed < -20:
            power = 3
        elif v_speed < 0:
            power = 2
        else:
            power = 1

    # Print the desired rotation and power settings
    print(rotate, power)
