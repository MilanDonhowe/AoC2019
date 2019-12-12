#ok this time instead of ray casting let's try calculating the distance between points, then checking the degree.

from math import *



#def can_see_asteroid(pos, vec, map, tolerence=0.4):


def viewable_asteroids(asteroid_pos, map):
    # check angle between each thing or whatever

                        
    #print(measured_angles)
    return len(measured_angles)
                    


def find_locations(map):
    max_nm = set()
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '#':
                max_nm.add(viewable_asteroids((x, y), map))
    
    print(max(max_nm))


asteroid_map = """.#..#
.....
#####
....#
...##""".split("\n")

with open("input", "r") as f:
    problem = f.read().split("\n")[:-1]

#import pprint
#pprint.pprint(problem)

find_locations(problem)