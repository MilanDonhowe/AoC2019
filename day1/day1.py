#Advent of Code Day 1
import math 

modules = []
with open("1dayinput", "r") as file:
    modules = file.readlines()
#part 1:
def calculateFuelPerMass(mass):
    return math.floor(mass/3)-2
totalFuelSum = 0
for i in modules:
    totalFuelSum += calculateFuelPerMass(int(i))
print(f"the total fuel is {totalFuelSum}")

#part 2:
def calculateFuelPerFuelMass(mass):
    thisAmountsMass = math.floor(mass/3)-2
    if (thisAmountsMass <= 0):
        return 0
    else:
        return thisAmountsMass + calculateFuelPerFuelMass(thisAmountsMass)

newTotalSum = 0
for i in modules:
    newTotalSum += calculateFuelPerFuelMass(int(i))
print(f"the total fuel mass is {newTotalSum}")