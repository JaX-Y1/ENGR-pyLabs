# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 4.14
# Date:         15 9 2023
from math import *
coeffA = int(input("Please enter the coefficient A: "))
coeffB = int(input("Please enter the coefficient B: "))
coeffC= int(input("Please enter the coefficient C: "))
quadEqation = ""
#Coeff A
if(coeffA<0):
    quadEqation = quadEqation + "- "
if(abs(coeffA)==1):
    quadEqation = quadEqation + "x^2 "
elif(abs(coeffA)>0):
    quadEqation = quadEqation + str(abs(coeffA)) + "x^2 "
#Coeff B   
if(coeffA!=0): 
    if(coeffB<0):
        quadEqation = quadEqation + "- "
    elif(coeffB>0):
        quadEqation = quadEqation + "+ "
if(abs(coeffB)==1):
    quadEqation = quadEqation + "x "
elif(abs(coeffB)>0):
    quadEqation = quadEqation + str(abs(coeffB)) + "x "
#Coeff C   
if(coeffB!=0 or coeffA!=0): 
    if(coeffC<0):
        quadEqation = quadEqation + "- "
    elif(coeffC>0):
        quadEqation = quadEqation + "+ "
if(abs(coeffC)>0):
    quadEqation = quadEqation + str(abs(coeffC))+ " "
#finish equation. set equal to zero
quadEqation = quadEqation + "= 0"
print(f"The quadratic equation is {quadEqation}")
