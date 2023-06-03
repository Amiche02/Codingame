import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

height_of_playground = int(input())
playground = []

for i in range(height_of_playground):
    row = input()
    playground.append(row)

# Find the position of the asterisk (*)
your_position = None
for i in range(height_of_playground):
    if '*' in playground[i]:
        your_position = (i, playground[i].index('*'))
        break

# Calculate the distances to each child
closest_distance = math.inf
closest_child = None

for i in range(height_of_playground):
    for j in range(len(playground[i])):
        if playground[i][j].isalpha():
            distance = math.sqrt((i - your_position[0]) ** 2 + (j - your_position[1]) ** 2)
            if distance < closest_distance:
                closest_distance = distance
                closest_child = playground[i][j]

# Write an answer using print
print(closest_child)
