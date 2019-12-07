import functools

problem_input = []
with open("1dayinput", "r") as f:
    problem_input = f.readlines()
total_fuel = functools.reduce(lambda ac, cv: ac + ((cv//3)-2), [int(x) for x in problem_input], 0)

calc_mass = lambda mass: (mass//3)-2


def mass_per_fuel (mass):
    if (calc_mass(mass) <= 0): return 0
    else:
        return calc_mass(mass) + mass_per_fuel(calc_mass(mass))
total_recursive_fuel = functools.reduce(lambda ac, cv: ac + mass_per_fuel(cv), [int(x) for x in problem_input], 0)

print(f"the total fuel is {total_fuel}, the total recursive fuel is {total_recursive_fuel}")

print (mass_per_fuel (100))
