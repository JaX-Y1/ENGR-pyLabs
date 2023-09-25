# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Andrew Marshall
# Section:      522
# Assignment:   Lab 6.16
# Date:         22 9 2023
from math import *
num = int(input("Enter a value for n: "))
#declare variables
r = 0
leftSum = 0
rightSum = 0
iterator = num + 1
#calculate left sum (add the integers up until num but not including num)
for i in range(1,num):
    leftSum += i
#calculate right sum (add the integers past num till = leftSum)
while(rightSum<leftSum):
    rightSum += iterator
    iterator += 1
    r += 1
else: #print results
    if(leftSum==rightSum):
        print(f"{num} is a balancing number with r={r}")
    else:
        print(f"{num} is not a balancing number")