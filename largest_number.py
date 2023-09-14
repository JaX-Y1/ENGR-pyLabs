#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Preston Montgomery
# Section: 522
# Assignment: Lab 4 Individual
# Date: 9/11/23
#
from math import *
user_first_num=float(input("Enter number 1: ")) #key part is the float command as it will be converted to string without it
user_second_num=float(input("Enter number 2: "))
user_third_num=float(input("Enter number 3: "))
if ((user_first_num > user_second_num)and(user_first_num > user_third_num)): #must pass these two tests in order for the first number to qualifiy as the largest number
    print("The largest number is",user_first_num,)
elif (user_third_num < user_second_num):
    print("The largest number is",user_second_num,)
else:
    print("The largest number is",user_third_num,)