# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 7.26.1
# Date:         2 10 2023
leetDict = {"a": 4, "e": 3, "o": 0, "s": 5, "t": 7} #dictionary
userInput = input("Enter some text: ")
finalLeet = ""
words = userInput.rsplit(" ")
for word in words: #for each word
    for leet in leetDict: #search through each element in dictionary
        if word.find(leet) >= 0: #replace all found dictionary keys with their values
            word = word.replace(leet,str(leetDict[leet]))
    #print(word)
    finalLeet += word + " "
print(f"In leet speak, \"{userInput}\" is:\n{finalLeet}")

