"""
# = asteroid
. = clear

X distance from left edge
Y distance from top edge
(0,0) (1,0)
 pos1  pos2

monitoring station can see any asteroid within LOS

"""

from math import *



def can_see_asteroid(pos, vec, map, prev=None, bypass=False):
    # send line out, if it hits an asteroid then returns the vector, else return None
    vec_x = pos[0]
    vec_y = pos[1]
    final_pos = None
    
    while round(vec_x+vec[0]) in range(0, len(map[0])) and round(vec_y+vec[1]) in range(0, len(map)):
        vec_x += vec[0]
        vec_y += vec[1]
        p_y = round(vec_y)
        p_x = round(vec_x)
        if (map[p_y][p_x] == "#") and (p_y != pos[1]) and (p_x != pos[0]):
            if (bypass == True):
                if not ( (p_x, p_y) in prev ):
                    final_pos = (p_x, p_y)
                    break
            else:
                final_pos = (p_x, p_y)
                break
        

    return final_pos



def viewable_asteroids(asteroid_pos, map):

    checked_vectors = set()
    asteroid_vectors = set()
    degrees = set()
    bp = True
    for angle in range(0, 360):
        
        dx = cos(radians(angle))
        dy = sin(radians(angle))
        this_vector = (dx, dy) #x, y
        
        if not this_vector in checked_vectors:
            checked_vectors.add(this_vector)

            new_astroid = can_see_asteroid(asteroid_pos, this_vector, map, asteroid_vectors, bp)
            if (new_astroid != None):
                asteroid_vectors.add(new_astroid)
    print(asteroid_vectors)
    return len(asteroid_vectors)


def find_locations(map):

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '#':
                print(viewable_asteroids((x, y), map))


asteroid_map = """.#..#
.....
#####
....#
...##""".split("\n")

find_locations(asteroid_map)