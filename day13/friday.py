# LET'S CODE!
from computer import *

with open("input", "r") as file:
    problem = file.read()

arcade_cabinet = int_computer(problem)
arcade_cabinet.run()
