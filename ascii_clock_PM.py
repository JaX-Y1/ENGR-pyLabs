#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Preston Montgomery
# Section: 522
# Assignment: Lab 8 Team Individual Part
# Date: 10/18/23
#

#initial variables
digitList = []
user_char_empty = False

#create a function that can replace a given digitList with a given character.
def replaceDigits(listOfDigits, character):
    for j in range(len(listOfDigits)):
        for i in range(len(listOfDigits[j])):
            listOfDigits[j][i] = listOfDigits[j][i].replace(str(j),str(character))

#############
### Input ###
#############

#Get Time
user_time = input(f'Enter the time: ')

#Use String.split(“:”) to separate the digits into a time list.
user_time_split = user_time.split(':')

#reassign 1st and 2nd element as sublists containing each side's digits.
user_time_split[0] = list(user_time_split[0])
user_time_split[1] = list(f"{user_time_split[1]:0>2}")

#Get Clock type
user_clock = int(input(f'Choose the clock type (12 or 24): '))

#Get preferred character
user_char = str(input(f'Enter your preferred character: '))

#Check if user inputted a character. If not, use each digit as the character for that digit.(Store as bool)
if bool(user_char) == False:
    user_char_empty = True

#Check if character is in a string containing all permitted characters (abcdeghkmnopqrsuvwxyz@$&*=) and is 1 character long.
elif (user_char in 'abcdeghkmnopqrsuvwxyz@$&*=' and len(user_char)==1):
    #replace digits in digitList with the provided character using a function.
    replaceDigits(digitsList, user_char)
    
#While loop that asks for input again if character is not in permitted character string and is not 1 character long.
else:
    while user_char not in 'abcdeghkmnopqrsuvwxyz@$&*=' or len(user_char)!=1:
        user_char = input(f'Character not permitted! Try again: ')
    #Replace digits in digitList with the provided character with the function that does so.
    replaceDigits(digitsList, user_char)


