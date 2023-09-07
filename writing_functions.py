# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 3.18
# Date:         6 9 2023

from math import*
def areaTriangle(side):
    height = (side/2)/tan(radians(30))
    area = side*height*0.5
    return round(area,3)
def areaSquare(side):
    area = side*side
    return round(area,3)
def areaPenta(side):
    #360 degrees / 5 sides = 72 degrees per triangle
    #half the triangle is 36 degrees. Needed for a right angle trig.
    height = (side/2)/tan(radians(36))
    triangleArea5 = side*height*0.5
    area = triangleArea5*5
    return round(area,3)
def areaDodeca(side):
    height = (side/2)/tan(radians(15))
    triangleArea12 = side*height*0.5
    area = triangleArea12*12
    return round(area,3)

sideLength = float(input("Please enter the side length: "))
print(f"A triangle with side {sideLength:.2f} has area {areaTriangle(sideLength):.3f}")
print(f"A square with side {sideLength:.2f} has area {areaSquare(sideLength):.3f}")
print(f"A pentagon with side {sideLength:.2f} has area {areaPenta(sideLength):.3f}")
print(f"A dodecagon with side {sideLength:.2f} has area {areaDodeca(sideLength):.3f}")