# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Andrew Marshall
# Section:      522
# Assignment:   Lab 6.15
# Date:         22 9 2023
from math import *
num = int(input("Enter a positive integer: "))
count = []
print(f"The Juggler sequence starting at {num} is:")
count.append(num) #add the entered number to the sequence

nextNum = num
iterations = 0
#run the juggle sequence
while nextNum!=1:
    #if even
    if(nextNum%2==0):
        nextNum = floor(sqrt(nextNum))
        count.append(nextNum)
        #if odd
    elif(nextNum%2==1):
        nextNum = floor(nextNum**(3/2))
        count.append(nextNum)
    #counter for number of runs of the sequence
    iterations+=1
for i in count:
    if(i != count[len(count)-1]):
        print(f"{i}, ", end="")
    else:
        print(i)
print(f"It took {iterations} iterations to reach 1")