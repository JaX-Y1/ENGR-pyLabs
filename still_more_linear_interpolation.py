# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 3.16
# Date:         1 9 2023
from math import*
time1 = float(input("Enter time 1: "))
xPos1 = float(input("Enter the x position of the object at time 1: "))
yPos1 = float(input("Enter the y position of the object at time 1: "))
zPos1 = float(input("Enter the z position of the object at time 1: "))
time2 = float(input("Enter time 2: "))
xPos2 = float(input("Enter the x position of the object at time 2: "))
yPos2 = float(input("Enter the y position of the object at time 2: "))
zPos2 = float(input("Enter the z position of the object at time 2: "))
#calculate slope
slopeX = (xPos2-xPos1)/(time2-time1)
slopeY = (yPos2-yPos1)/(time2-time1)
slopeZ = (zPos2-zPos1)/(time2-time1)
interval = ((time2-time1)/4)
times = []
#gets the 5 time intervals to interpolate
for i in range(5):
    times.append((i*interval)+time1)
#calculate the interpolations
for x in times:
    xInterpolate=slopeX*(x-time1)+xPos1
    yInterpolate=slopeY*(x-time1)+yPos1
    zInterpolate=slopeZ*(x-time1)+zPos1
    print(f"At time {x:.2f} seconds the object is at ({xInterpolate:.3f} , {yInterpolate:.3f} , {zInterpolate:.3f})")
