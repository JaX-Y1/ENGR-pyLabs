# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 7.25
# Date:         2 10 2023
userInput = input("Enter word(s) to convert to Pig Latin: ")
words = userInput.rsplit(" ") #splits words into a list
#or in the future create a list of the vowels/2 letter consontants to compare with
finalString = ""
for i in words:
    #checks for a vowel
    if i[0:1].lower() == "a" or i[0:1].lower() == "e" or i[0:1].lower() == "i" or i[0:1].lower() == "o" or i[0:1].lower() == "u" or i[0:1].lower() == "y":
        finalString += i + "yay "
    else:
        if i[0:2].lower() == "wh" or i[0:2].lower() == "ph" or i[0:2].lower() == "th" or i[0:2].lower() == "gr" or i[0:2].lower() == "bl" or i[0:2].lower() == "wr" or i[0:2].lower() == "br" or i[0:2].lower() == "pr":
            temp = i[0:2]
            finalString += i[2:] + temp + "ay "
        else:
            temp = i[0:1]
            finalString += i[1:] + temp + "ay "
#print final string
print(f"In Pig Latin, \"{userInput}\" is: {finalString}")