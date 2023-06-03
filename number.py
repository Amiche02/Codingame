import sys
import math


n = int(input())

if n > 0:
    lst = ""
else:
    lst = f"{n}"


if n != 0:
    while n != 0:
        if n > 0:
            n -= 1
        else:
            n += 1
        if len(lst) != 0:
            lst += " " + str(n)
        else:
           lst += str(n) 

    print(lst)

else:
    print("Already Zero")