# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 2.10
# Date:         27 8 2023
from math import*
#Positions are in meters
xOne=8
xTwo=-5
yOne=6
yTwo=30
zOne=7
zTwo=9
#Time: measured in seconds. The times at which
#position was measured.
timeOne=12
timeTwo=85 
#interpolate at t = 30 seconds
interpolateTimes=[30.0,37.5,45.0,52.5,60.0]
#iterate for loop
iterator=0
for x in interpolateTimes:
    iterator+=1
    interpolateTime1=x
    #slope calculation
    slopeX = (xTwo-xOne)/(timeTwo-timeOne)
    slopeY = (yTwo-yOne)/(timeTwo-timeOne)
    slopeZ = (zTwo-zOne)/(timeTwo-timeOne)
    #interpolation calculation
    xInterpolate=slopeX*(interpolateTime1-timeOne)+xOne
    yInterpolate=slopeY*(interpolateTime1-timeOne)+yOne
    zInterpolate=slopeZ*(interpolateTime1-timeOne)+zOne
    print("At time",x,"seconds:")
    print(f"x{iterator} =",xInterpolate,"m")
    print(f"y{iterator} =",yInterpolate,"m")
    print(f"z{iterator} =",zInterpolate,"m")
    if(x==60.0):
        break
    print("-----------------------")
    