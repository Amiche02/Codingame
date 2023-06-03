import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(input())
H = int(input())
T = input()

artArr = [[""] * 27 for _ in range(H)]

for i in range(H):
    row = input()
    for j in range(27):
        artArr[i][j] = row[(j + 1) * L - L:(j + 1) * L]

indexArr = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z ?".split()

T = T.upper()

for p in range(H):
    outputLine = ""
    for item in T:
        index = indexArr.index(item) if item in indexArr else -1
        if index == -1:
            outputLine += artArr[p][26]
        else:
            outputLine += artArr[p][index]
    print(outputLine)



