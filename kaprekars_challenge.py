# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 7.28
# Date:         3 10 2023
totalIterations = 0
#functions
def listToInt(list): #converts and returns a given list to an integer including strings
    finalInt = ""
    for i in range(len(list)):
        finalInt += str(list[i])
    return int(finalInt)

def intToList(integer): #converts and returns a given integer to a list(with leading zeros)
    intConversion = str(integer)
    if(len(intConversion) == 1): #adds leading zeros to make a 4-digit integer
        intConversion = "000" + intConversion
    elif(len(intConversion) == 2):
        intConversion = "00" + intConversion
    elif(len(intConversion) == 3):
        intConversion = "0" + intConversion
    finalList = []
    for i in range(len(intConversion)):
        finalList.append(int(intConversion[i]))
    return finalList

#converting the kapsNumber to 4 digits and making sure atleast 2 digits are unique
for kapsNumber in range(10000):
    finalAnswer = 0
    numList = []
    kapsNumber = str(kapsNumber)
    if(int(kapsNumber)<1000):
        if(len(kapsNumber) == 1): #adds leading zeros to make a 4-digit integer
            kapsNumber = "000" + kapsNumber
        elif(len(kapsNumber) == 2):
            kapsNumber = "00" + kapsNumber
        elif(len(kapsNumber) == 3):
            kapsNumber = "0" + kapsNumber

    if(kapsNumber[0]!=kapsNumber[1] or kapsNumber[0]!=kapsNumber[2] or kapsNumber[0]!=kapsNumber[3]):
    #print("Good")
        if(int(kapsNumber)==6174): #skip over 6174 because kaprekars constant has 0 iterations
            continue
        for i in range(len(kapsNumber)):
            numList.append(int(kapsNumber[i]))
        while finalAnswer != 6174:
            ascending = numList.copy()
            descending = numList.copy()
            ascending.sort()
            descending.sort(reverse=True)
            finalAnswer = listToInt(descending) - listToInt(ascending)
            numList = intToList(finalAnswer)
            totalIterations +=1
            
            
    else:
        #rep digits reach in 1 iteration EXCEPT for 0.
        if(int(kapsNumber)!=0):
            totalIterations +=1
print(f"Kaprekar's routine takes {totalIterations} total iterations for all four-digit numbers")
#0 doesn't count for an iteration.
#6174(Kaprekar's constant) doesn't count for an iteration.