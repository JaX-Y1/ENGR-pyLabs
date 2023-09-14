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

user_input = int(input("Please enter a positive value for day: ")) #The user input is measured in days
if (user_input < 0): #detects if the input is negative if so the calcualtions won't occur as you can't have 0 days for this problem
    print("You entered an invalid number!")

elif (user_input <= 10): #gadgets produced for first ten days
    gadgets_produced_first_10_days=(user_input*10)
    print(f"The sum total number of gadgets produced on day {int(user_input)} is {int(gadgets_produced_first_10_days)}")

elif (user_input <= 50):
    gadgets_produced_10_through_50=((1/2)*(user_input**2)+(1/2)*(user_input)+45)
    print(f"The sum total number of gadgets produced on day {int(user_input)} is {int(gadgets_produced_10_through_50)}")

elif (101 > user_input > 50):
    gadgets_produced_50_through_100=(1320+(50*(user_input-50)))
    print(f"The sum total number of gadgets produced on day {int(user_input)} is {int(gadgets_produced_50_through_100)}")

else:
    print("The sum total number of gadgets produced on day 102 is 3820")