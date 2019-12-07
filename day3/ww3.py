# Day 3: let's get this bread 🍞
import pprint

def manhattan_distance(pos):
    return abs(pos[0]) + abs(pos[1])
def generate_vertices(pathstr, return_list=False):
    steps = pathstr.split(",")
    vertices = set()
    list_option = []
    # x, y
    this_x = 0
    this_y = 0
    for step in steps:
        change_magnitude = int(step[1:])
        for i in range(change_magnitude):
            if (step[0] == 'D'):
                this_y -= 1
            elif (step[0] == 'U'):
                this_y += 1
            elif (step[0] == 'L'):
                this_x -= 1
            elif (step[0] == 'R'):
                this_x += 1
            vertices.add((this_x, this_y))
            list_option.append((this_x, this_y))
    if (return_list == True):
        return list_option
    else:
        return vertices


# Reading the actual input
pathways = []
with open("input.txt", "r") as file:
    pathways = file.readlines()

vertex_list_one = generate_vertices(pathways[0])
vertex_list_two = generate_vertices(pathways[1])
#vertex_list_one = generate_vertices("R75,D30,R83,U83,L12,D49,R71,U7,L72")
#vertex_list_two = generate_vertices("U62,R66,U55,R34,D71,R55,D58,R83")


distances = []    

for point in vertex_list_two:
    if (point in vertex_list_one):
        distances.append(manhattan_distance(point))
print(f"the minimum distance is {min(distances)}")

# part 2 finding the number of steps involved
#list_one = generate_vertices("R75,D30,R83,U83,L12,D49,R71,U7,L72", True)
#list_two = generate_vertices("U62,R66,U55,R34,D71,R55,D58,R83", True)
list_one = generate_vertices(pathways[0], True)
list_two = generate_vertices(pathways[1], True)

paces_list_one = 0
intersects_one = {}
for pos in list_one:
    paces_list_one += 1
    if (pos in vertex_list_two):
        intersects_one[pos] = paces_list_one

paces_list_two = 0
intersects_two = {}
for pos in list_two:
    paces_list_two += 1
    if (pos in vertex_list_one):
        intersects_two[pos] = paces_list_two

steps_taken = set()
for key, value in intersects_one.items():
    this_step = value + intersects_two[key]
    steps_taken.add(this_step)
print(f"the minimum number of steps required is {min(steps_taken)}")