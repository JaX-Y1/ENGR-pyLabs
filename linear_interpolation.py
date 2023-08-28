# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section: 522
# Assignment: Lab 2.8
# Date: 1 9 2023
#
from math import*
#PART 1
print("Part 1:")
#Positions are based on Kilometers past Houston,TX
positionOne=2027
positionTwo=23027
#Time: measured in minutes. The times at which
#position was measured.
timeOne=10
timeTwo=55 #10 min + 45 min later
#interpolate at t = 25 minutes
interpolateTime1=25
#slope calculation
slope = (positionTwo-positionOne)/(timeTwo-timeOne)
#interpolation calculation
calculatedPos=slope*(interpolateTime1-timeOne)+positionOne
print("For t = 25 minutes, the position p =",calculatedPos,"kilometers")
#PART 2
print("Part 2:")
interpolateTime2=300
calculatedPos2=slope*(interpolateTime2-timeOne)+positionOne
#Earth's circumference in km. Linear Interpolation
#shouldn't calculated distance travelled, which is
#what would happen without the modulo.
earthCircum = 6745
circumDistance=earthCircum*2*pi

print("For t = 300 minutes, the position p=",calculatedPos2%circumDistance,"kilometers")