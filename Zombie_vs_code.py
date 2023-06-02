import sys
import math

WIDTH = 16000
HEIGHT = 9000
ASH_SPEED = 1000
ZOMBIE_SPEED = 400
ASH_ATTACK_DISTANCE = 2000
ZOMBIE_ATTACK_DISTANCE = 400


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


class Action:
    ash_x = ash_y = None
    humans = {}
    zombies = {}
    zombie_attack_human = {}

    def read_situation(self):
        self.ash_x, self.ash_y = [int(i) for i in input().split()]
        human_count = int(input())
        self.humans.clear()
        for i in range(human_count):
            human_id, human_x, human_y = [int(j) for j in input().split()]
            self.humans[human_id] = {'x': human_x, 'y': human_y}
        self.zombies.clear()
        zombie_count = int(input())
        for i in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
            self.zombies[zombie_id] = {'x': zombie_x, 'y': zombie_y, 'next_x': zombie_xnext, 'next_y': zombie_ynext}
        self.zombie_attack_human.clear()
        for human_id, human in self.humans.items():
            for zombie_id, zombie in self.zombies.items():
                if (zombie['next_x'] > human['x'] - 600 or zombie['next_x'] < human['x'] + 600) and (
                        zombie['next_y'] > human['y'] - 600 or zombie['next_y'] < human['y'] + 600):
                    self.zombie_attack_human[zombie_id] = human_id

    def perform_action(self):
        zombie = self.get_closest_zombie()
        if zombie:
            print(zombie['x'], zombie['y'])

    def get_closest_zombie(self):
        distance_to_human = distance_to_hero = WIDTH
        closest_to_human = None
        closest_to_hero = None
        for zombie_id, zombie in self.zombies.items():
            human = self.humans[self.zombie_attack_human[zombie_id]]
            distance_to_human = calculate_distance(zombie['x'], zombie['y'], human['x'], human['y'])
            hero_distance = calculate_distance(self.ash_x, self.ash_y, human['x'], human['y'])
            if (distance_to_human < WIDTH) and (hero_distance - ASH_ATTACK_DISTANCE) / ASH_SPEED < (
                    distance_to_human + ZOMBIE_ATTACK_DISTANCE) / ZOMBIE_SPEED:
                closest_to_human = zombie
                distance_to_human = calculate_distance(zombie['x'], zombie['y'], human['x'], human['y'])
            if distance_to_hero > hero_distance:
                closest_to_hero = zombie
                distance_to_hero = hero_distance
        if closest_to_human:
            return closest_to_human
        else:
            return closest_to_hero


action = Action()
while True:
    action.read_situation()
    action.perform_action()
