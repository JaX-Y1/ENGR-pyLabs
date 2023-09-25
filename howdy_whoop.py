# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Andrew Marshall
# Section:      522
# Assignment:   Lab 6.13
# Date:         22 9 2023
firstInt = int(input("Enter an integer: "))
secondInt = int(input("Enter another integer: "))
#runs through 1-100 inclusive
for i in range(1, 101):
    #if current num is divisible by both
    if(i%firstInt ==0 and i%secondInt ==0):
        print("Howdy Whoop")
    #if current num is divisible by the first int
    elif(i%firstInt ==0):
        print("Howdy")
    #if current num is divisible by the second int
    elif(i%secondInt ==0):
        print("Whoop")
    #else print the actual number
    else:
        print(i)