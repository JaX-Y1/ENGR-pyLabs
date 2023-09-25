# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Andrew Marshall
# Section:      522
# Assignment:   Lab 6.14
# Date:         22 9 2023
def doublefactorial(num):
    #declare variables
    tempNum = num
    count = 0
    #return 1: definition of a factorial--> !0 = 1
    if(num==0):
        return 1
    while(tempNum >= 1):
        if(count==0):
            count=tempNum #set the first num of factorial
            tempNum-=2
            continue #skip the rest of the current iteration
        
        count*=tempNum
        tempNum-=2

    return count
print(doublefactorial(0))
print(doublefactorial(6))
print(doublefactorial(9))