import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
dict_ = {}
for elt in s:
    if elt.lower() not in dict_.keys():
        n = 0
        for j in s:
            if j.lower() == elt.lower():
                n += 1

        if elt.lower() not in dict_.keys():
            dict_[elt.lower()] = n

for k, values in dict_.items():
    print(f"{k} {values}")