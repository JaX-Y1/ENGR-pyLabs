#By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Preston Montgomery
# SK Thippireddy
# Andrew Marshall
# Rishi Bandhu
# Section: 522
# Assignment: Lab 4 Team
# Date: 9/14/2023
#
from math import *

############ Part A ############

a_user_input=str(input("Enter True or False for a: "))
b_user_input=str(input("Enter True or False for b: "))
c_user_input=str(input("Enter True or False for c: "))
dict_1 = {'False':0,'F':0,'f':0,'True':1,'T':1,'t':1}

############ Part B ############

print(f'a and b and c: {bool(dict_1[a_user_input] and dict_1[b_user_input] and dict_1[c_user_input])}')
print(f'a or b or c: {bool(dict_1[a_user_input] or dict_1[b_user_input] or dict_1[c_user_input])}')

############ Part C ############

print(f'XOR: {bool(bool(dict_1[a_user_input] == dict_1[b_user_input]) == bool(dict_1[a_user_input] < dict_1[b_user_input] and dict_1[a_user_input] > dict_1[b_user_input]))}')
print(f'Odd number: {bool((dict_1[a_user_input]+dict_1[b_user_input]+dict_1[c_user_input] == 3) or (dict_1[a_user_input]+dict_1[b_user_input]+dict_1[c_user_input] == 1))}')

