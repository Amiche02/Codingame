import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:

    actionx= ""
    actiony = ""
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    if light_x < initial_tx:
        actionx =  "W"
        initial_tx -= 1
    elif light_x > initial_tx:
        actionx =  "E"
        initial_tx += 1

    if light_y < initial_ty:
        actiony =  "N"
        initial_ty -= 1
    elif light_y > initial_ty:
        actiony =  "S"
        initial_ty += 1

    if (light_x < initial_tx) & (light_y < initial_ty):
        action = actionx + actiony
    else:
        action = actiony + actionx

    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    

    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(action)