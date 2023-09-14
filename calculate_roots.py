#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Preston Montgomery
# Section: 522
# Assignment: Lab 4 Individual
# Date: 9/13/23
#
from math import *
a=float(input("Please enter the coefficient A:"))
b=float(input("Please enter the coefficient B:"))
c=float(input("Please enter the coefficient C:"))

if (a == 0)and(a == b):
    print("You entered an invalid combination of coefficients!")
elif (a != 0):
    imaginary_test=((b**2)-(4*a*c))
    if (0 <= imaginary_test):
        x_negative=((-b-sqrt((b**2)-(4*a*c)))/(2*a))
        x_positive=((-b+sqrt((b**2)-(4*a*c)))/(2*a))
        if (x_negative == x_positive):
            print(f"The root is x = {x_positive}")
        elif (x_negative != x_positive):
            if(x_negative > x_positive):
                print(f"The roots are x = {x_negative} and x = {x_positive}")
            else:
                print(f"The roots are x = {x_positive} and x = {x_negative}")
    else: #you're now in the imaginary numbers realm
        i_positive_x=(f'{-b/(2*a)} + {abs(((b**2)-4*a*c)/(4*a))}i') #why it is 4*a in the denominator instead of 2*a idk save it for the SI
        i_negative_x=(f'{-b/(2*a)} - {abs(((b**2)-4*a*c)/(4*a))}i')
        print(f"The roots are x = {i_positive_x} and x = {i_negative_x}")
elif (a == 0): #if a = 0 that is 0 = bx + c or in other words a linear equation, which only has one root
    x_linear=((-c)/(b))
    print(f"The root is x = {x_linear}")
