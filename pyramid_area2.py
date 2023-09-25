# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 6.12
# Date:         22 9 2023
from math import *
#area of an equilateral triangle is (sqrt(3)/4) * sideLength**2
#area of the top of a given layer is 
# (sideLength times the current number of layers) times sqrt(3)/4 - the last layer
#The area of the sides of the triagle is (side length*current # of layers) * 3
#1:3 -> 9
#1:2 -> 6
#1:1 -> 3
#2:3 -> 18
#2:2 -> 12
#2:1 -> 6
#the difference is the side length * 3 for the sequence
sideLength = float(input("Enter the side length in meters: "))
numLayers = int(input("Enter the number of layers: "))

totalSideGold = 0
totalTopGold = 0

sideGoldForumula = (sideLength*numLayers)*3

sumOfTerms = (numLayers/2)*((2*(sideLength**2*3))+((numLayers-1)*(sideLength**2*3)))
totalSideGold = sumOfTerms

totalTopGold = (numLayers*sideLength)**2 * (sqrt(3)/4)
totalGold = totalTopGold + totalSideGold
print(f"You need {totalGold:.2f} m^2 of gold foil to cover the pyramid")