# staying alive, staying alive
from computer import *

with open("input", "r") as data:
    repair_program = data.read()

# inputs
# 1 is north
# 2 is south
# 3 is west
# 4 is east

# possible outputs
# 0 droid hit wall, position unchanged
# 1 droid moved
# 2 repair droid has moved and reached oxygen system
repair_droid = int_computer(repair_program)
repair_droid.run()