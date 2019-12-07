# okay I think this is a tree thing... time to see if I can parse this out
# funny story, accidentally streamlined the orbit counting by botching a recursive function which
# ended up setting the indirect_orbit variable I had to the total number of orbits in general!
# so I just used that for the problem :)



class solar_system():
    def __init__(self):
        self.bodies = {};
        self.total_orbits = 0
        self.total_moves = 0

        
    def show_orbits(self):
        print(f"the total orbits are {self.total_orbits}")

    def count_orbits(self, planet, prior_bodies):
        self.total_orbits += prior_bodies
        if(planet in self.bodies):
            for moon in self.bodies[planet]:
                self.count_orbits(moon, prior_bodies+1)

    def push_data(self, str_line):
        relationship_data = str_line.replace("\n", "").split(")")
        this_planet = relationship_data[0]
        this_moon = relationship_data[1]

        if (this_planet in self.bodies):
            self.bodies[this_planet].add(this_moon)
        else:
            self.bodies[this_planet] = {this_moon}

    def start_santa_search(self):
        # first find node YOU is in.
        initial_body = ''
        # find which planet YOU are on
        for body, moons in self.bodies.items():
            if "YOU" in moons:
                initial_body = body
                break
        self.searchedPlanets = []
        self.find_santa(initial_body, 0)

    def find_santa(self, planet, points):
        # is SANTA HERE?
        if "SAN" in self.bodies[planet]:
            print(f"SANTA AT {points} MOVES")
        else:
            self.searchedPlanets.append(planet)
            # search those (unsearched) child nodes
            for moon in self.bodies[planet]:
                if (moon in self.bodies) and not (moon in self.searchedPlanets):
                    self.find_santa(moon, points+1)
            
            # search those (unsearched) parent nodes
            for body, moons in self.bodies.items():
                if planet in moons:
                    if not (body in self.searchedPlanets):
                        self.find_santa(body, points+1)


        
map_data = []
with open("input.txt", "r") as f:
    map_data = f.readlines()

# part 1
milky_way = solar_system()
for line in map_data:
    milky_way.push_data(line)
milky_way.count_orbits('COM', 0)
milky_way.show_orbits()

# part 2
milky_way.start_santa_search()