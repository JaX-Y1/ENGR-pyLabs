#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Preston Montgomery
# Section: 522
# Assignment: Lab 8 Team Individual Part
# Date: 10/18/23
#

#variables
zero = ["000", "0 0", "0 0 ", "0 0", "000"]

one = [" 1 ", "11 ", " 1 ", " 1 ", "111"]

two = ["222", "  2", "222", "2  ", "222"]

three = ["333", "  3", "333", "  3", "333"]

four = ["4 4", "4 4", "444", "  4", "  4"]

five = ["555", "5  ", "555", "  5", "555"]

six = ["666", "6  ", "666", "6 6", "666"]

seven = ["777", "  7", "  7", "  7", "  7"]

eight = ["888", "8 8", "888", "8 8", "888"]

nine = ["999", "9 9", "999", "  9", "999"]

am = [" A   M   M", "A A  MM MM", "AAA  M M M", "A A  M   M", "A A  M   M"]

pm = ["PPP  M   M", "P P  MM MM", "PPP  M M M", "P    M   M", "P    M   M"]

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
print(user_time_split)

#Get Clock type
user_clock = int(input(f'Choose the clock type (12 or 24): '))

#Get preferred character
user_char = str(input(f'Enter your preferred character: '))

#Check if user inputted a character. If not, use each digit as the character for that digit.(Store as bool)
if bool(user_char) == False:
    user_char_empty = True
    

#Check if character is in a string containing all permitted characters (abcdeghkmnopqrsuvwxyz@$&*=) and is 1 character.
elif (user_char in 'abcdeghkmnopqrsuvwxyz@$&*=' and len(user_char)==1):
    user_char = user_char
    
#While loop that asks for input again if character is not in permitted character string and is not 1 character.
else:
    while user_char not in 'abcdeghkmnopqrsuvwxyz@$&*=' or len(user_char)!=1:
        user_char = input(f'Enter your preferred character: ')
    #print(user_char)