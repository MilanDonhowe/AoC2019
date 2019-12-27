# MLG planet orbiting model

# ehh just made a hash map with the stuff
# LAYOUT:
# "name" : [pos, vel]
# where pos & vel are 3d vectors as lists
# with layout  [x, y, z]

input_moons = {
    "Io": [
        [0, 4, 0],
        [0, 0, 0]
    ],
    "Europa": [
        [-10, -6, -14],
        [0, 0, 0]
    ],
    "Ganymede": [
        [9, -16, -3],
        [0, 0, 0]
    ],
    "Callisto": [
        [6, -1, 2],
        [0, 0, 0]
    ]
}


def apply_gravity(bodies):
    checked = []
    for k1, v1 in bodies.items():
        for k2, v2 in bodies.items():
            if ( {k1,k2} not in checked) and (k1 != k2):
                checked.append({k1, k2})
                for cord in range(3):
                    if (v1[0][cord] != v2[0][cord]):
                        if v1[0][cord] > v2[0][cord]:
                            v1[1][cord] -= 1
                            v2[1][cord] += 1
                        else:
                            v1[1][cord] += 1
                            v2[1][cord] -= 1
    return bodies

def apply_velocity(bodies):
    for _, val in bodies.items():
        for cord in range(3):
            val[0][cord] += val[1][cord]
    return bodies


def calculate_energy(bodies):
    total_energy = 0
    for _, val in bodies.items():
        potent_energy = 0
        kinetic_energy = 0
        for cord in range(3):
            potent_energy += abs(val[0][cord])
            kinetic_energy += abs(val[1][cord])
        total_energy += (potent_energy * kinetic_energy)
    return total_energy

moons = input_moons
for i in range(1000):
    moons = apply_velocity(apply_gravity(moons))

# part 1
print(f"After 1000 steps the energy is {calculate_energy(moons)}")


# part 2 uhh idk
print("Please wait 10,000 years for me to do some long divison...")
all_positions = set()
this_moon = input_moons


#print(f"IT TOOK {step} STEPS TO GET THE FUCKING ANSWER-- PLEASE SenD HELP")