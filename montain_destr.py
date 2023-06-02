import sys

while True:
    max_height = -1
    max_index = -1

    for i in range(8):
        mountain_h = int(input())  

        if mountain_h > max_height:
            max_height = mountain_h
            max_index = i


    print(max_index)
    sys.stdout.flush() 