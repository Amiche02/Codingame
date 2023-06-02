n = int(input())

if n == 1:
    print(0)
else:
    power = 0
    while n > 1 and n % 2 == 0:
        n //= 2
        power += 1

    if n == 1:
        print(power)
    else:
        print(-1)
