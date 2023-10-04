# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 7.28
# Date:         3 10 2023
userInput = input("Enter a four-digit integer: ")
numList = []
finalAnswer = 0
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

#converting the userInput to 4 digits and making sure atleast 2 digits are unique

if(len(userInput) == 1): #adds leading zeros to make a 4-digit integer
    userInput = "000" + userInput
elif(len(userInput) == 2):
    userInput = "00" + userInput
elif(len(userInput) == 3):
    userInput = "0" + userInput

if(userInput[0]!=userInput[1] or userInput[0]!=userInput[2] or userInput[0]!=userInput[3]):
    #print("Good")
    for i in range(len(userInput)):
        numList.append(int(userInput[i]))
    print(listToInt(numList),end=" > ")
    while finalAnswer != 6174:
        ascending = numList.copy()
        descending = numList.copy()
        ascending.sort()
        descending.sort(reverse=True)
        finalAnswer = listToInt(descending) - listToInt(ascending)
        numList = intToList(finalAnswer)
        totalIterations +=1
        if(listToInt(numList)==6174):
            print(listToInt(numList))
        else:
            print(listToInt(numList),end=" > ")
    if(finalAnswer == 6174):
        print(f"{listToInt(userInput)} reaches 6174 via Kaprekar's routine in {totalIterations} iterations")
else:
    print(f"{listToInt(userInput)} > 0")
    print(f"{listToInt(userInput)} reaches 0 via Kaprekar's routine in 1 iterations")