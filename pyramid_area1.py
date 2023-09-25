# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 6.11
# Date:         22 9 2023
from math import *
#area of an equilateral triangle is (sqrt(3)/4) * sideLength**2
#area of the top of a given layer is just the top area of the last(largest) layer
#The area of the sides of the triagle is (side length*current # of layers) * 3
sideLength = float(input("Enter the side length in meters: "))
numLayers = int(input("Enter the number of layers: "))
tempLayers = numLayers
totalSideGold = 0
totalTopGold = 0
while tempLayers>0:
    totalSideGold += ((sideLength**2)*tempLayers)*3
    tempLayers-=1
totalTopGold = (sideLength*numLayers)**2 * (sqrt(3)/4)
totalGold = totalTopGold + totalSideGold
print(f"You need {totalGold:.2f} m^2 of gold foil to cover the pyramid")