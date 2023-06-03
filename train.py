import math

def train_track(s, l):
    pos = 0
    while s > 0:
        pos += s
        s /= 2

    return pos >= l

s = float(input())
l = float(input())

result = train_track(s, l)

print(str(result).lower())
