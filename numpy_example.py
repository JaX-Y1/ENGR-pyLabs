# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 11 Group
# Date:         10 11 2023
import numpy as np
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
a = np.arange(12).reshape(3,4)
b = np.arange(8).reshape(4,2)
c = np.arange(6).reshape(2,3)
d = a@b@c
dT = d.T
e = np.sqrt(d)/2
print(f"A = {a}")
print(f"B = {b}")
print(f"C = {c}")
print(f"D = {d}")
print(f"D^T = {dT}")
print(f"E = {e}")