import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

x_min, y_min = 0, 0
x_max, y_max = w - 1, h - 1
# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if 'U' in bomb_dir:
        y_max = y0 - 1
    elif 'D' in bomb_dir:
        y_min = y0 + 1
    if 'L' in bomb_dir:
        x_max = x0 - 1
    elif 'R' in bomb_dir:
        x_min = x0 + 1
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    x = (x_min + x_max) // 2
    y = (y_min + y_max) // 2
    

    x0, y0 = x, y
    # the location of the next window Batman should jump to.
    print(f"{x} {y}")
