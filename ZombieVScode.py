import sys
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append((human_id, human_x, human_y))
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append((zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))


    if len(humans)==2:
        z_h_pas = []
        h_id = []
        target_x, target_y = 0, 0

        for zombie in zombies:
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = zombie
            z_h_pas_i = []
            h_id_ = []

            for human in humans:
                human_id, human_x, human_y = human
                pas = distance(human_x, human_y, zombie_x, zombie_y) // 400
                z_h_pas_i.append(pas)
                h_id_.append(human_id)

            z_h_pas.append(min(z_h_pas_i))
            h_id.append(h_id_[z_h_pas_i.index(min(z_h_pas_i))])

        max_pas = max(z_h_pas)
        id_ = h_id[z_h_pas.index(max_pas)]

        for human in humans:
            if id_ == human[0]:
                human_id, human_x, human_y = human
                target_x = human_x
                target_y = human_y
                break

        print(f"{target_x} {target_y}")
    else:
        target_x, target_y = 0, 0
        for zombie in zombies:
            z_id, z_x, z_y, z_xnext, z_ynext = zombie
            dist = distance(x, y, z_x, z_y)
            if dist <= 2000:
                target_x, target_y = z_x, z_y
                break

        if target_x != 0 and target_y != 0:
            print(f"{target_x} {target_y}")
        else:
            closest_human = min(humans, key=lambda h: math.sqrt((x - h[1]) ** 2 + (y - h[2]) ** 2))
            target_x, target_y = closest_human[1], closest_human[2]
            print(f"{target_x} {target_y}")
