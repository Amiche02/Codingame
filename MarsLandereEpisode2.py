previous_y, previous_x = 0, 0
central_x, central_y = 0, 0
land_start_x, land_end_x = 0, 0
land_length = 0

surfaceN = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surfaceN):
    landX, landY = map(int, input().split())
    if landY == previous_y:
        land_start_x = previous_x
        land_end_x = landX
        central_x = (land_start_x + land_end_x) // 2
        central_y = landY
    previous_y = landY
    previous_x = landX

land_length = land_end_x - land_start_x
land_start_x += land_length // 20
land_end_x -= land_length // 20

# game loop
while True:
    X, Y, hSpeed, vSpeed, fuel, rotate, power = map(int, input().split())

    power = 4

    if X < land_start_x:
        if hSpeed <= 60:
            rotate = -30
        elif hSpeed >= 70:
            rotate = 30
        else:
            rotate = 0

    if X > land_end_x:
        if hSpeed >= -60:
            rotate = 30
        elif hSpeed <= -70:
            rotate = -30
        else:
            rotate = 0

    if land_start_x < X < land_end_x:
        if hSpeed < -5:
            rotate = -45
        elif hSpeed > 5:
            rotate = 45
        else:
            rotate = 0
            if vSpeed < -30:
                power = 4
            else:
                power = 0

    print(rotate, power)
