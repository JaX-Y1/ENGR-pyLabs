# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Preston Montgomery
#SK Thippireddy
#Rishi Bandu
#Andrew Marshall
# Section: 522
# Assignment: Lab 1 Topic 2 (Team) Activity 3
# Date: 9/1/23
#
from math import *
user_variable = float(input("Please enter the quantity to be converted: "))
#input for intial value inputted above
def pounds_to_newtons(user_variable):
    newtons = 4.4482216 * user_variable
    return newtons
print(f"{user_variable:.2f} pounds force is equivalent to {pounds_to_newtons(user_variable):.2f} Newtons")
def meters_to_feet(user_variable):
    feet = 3.28084 * user_variable
    return feet
print(f"{user_variable:.2f} meters is equivalent to {meters_to_feet(user_variable):.2f} feet")
def atomspheres_to_kilopascals(user_variable):
    atomsphere = 101.325 * user_variable
    return atomsphere
print(f"{user_variable:.2f} atmospheres is equivalent to {atomspheres_to_kilopascals(user_variable):.2f} kilopascals")
def watts_to_BTU_per_hour(user_variable):
    watts = 3.412141633 * user_variable
    return watts
print(f"{user_variable:.2f} watts is equivalent to {watts_to_BTU_per_hour(user_variable):.2f} BTU per hour")
def liters_per_second_to_US_gallons_per_minute(user_variable):
    liters_per_second = 15.850323141489 * user_variable
    return liters_per_second
print(f"{user_variable:.2f} liters per second is equivalent to {liters_per_second_to_US_gallons_per_minute(user_variable):.2f} US gallons per minute")
def degree_celsius_to_degrees_fahrenheit(user_variable):
    degree_celsius = 32 + 9/5 * user_variable
    return degree_celsius
print(f"{user_variable:.2f} degrees Celsius is equivalent to {degree_celsius_to_degrees_fahrenheit(user_variable):.2f} degrees Fahrenheit")