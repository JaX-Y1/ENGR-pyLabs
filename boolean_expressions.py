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

a=str(input("Enter True or False for a: "))
b=str(input("Enter True or False for b: "))
c=str(input("Enter True or False for c: "))
dict_1 = {'False':0,'F':0,'f':0,'True':1,'T':1,'t':1}

############ Part B ############

print(f'a and b and c: {bool(dict_1[a] and dict_1[b] and dict_1[c])}')
print(f'a or b or c: {bool(dict_1[a] or dict_1[b] or dict_1[c])}')

############ Part C ############

print(f'XOR: {bool(bool(dict_1[a] == dict_1[b]) == bool(dict_1[a] < dict_1[b] and dict_1[a] > dict_1[b]))}')
print(f'Odd number: {bool((dict_1[a]+dict_1[b]+dict_1[c] == 3) or (dict_1[a]+dict_1[b]+dict_1[c] == 1))}')

#comp1 = (not(a and not(b)) or (not(c) and b) and (not(b)) or (not(a) and b and not(c)) or (a and not(b)))
comp1 = (not (a and not b) or (not c and b)) and (not b) or (not a and b and not c) or (a and not b)
comp2 = (not ((b or not c) and (not a or not c))) or (not (c or not (b and c))) or (a and not c) and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
simp1 = (False) #not(B) + (not(A) and B and not(c))
simp2 = (True)
print(f"Complex 1: {comp1}")
print(f"Complex 2: {comp2}")
print(f"Simple 1: {simp1}")
print(f"Simple 2: {simp2}")
