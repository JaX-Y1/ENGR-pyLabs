# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 3.17
# Date:         6 9 2023

from math import*
#Force
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
accel = float(input("Please enter the acceleration (m/s^2): "))
force = mass * accel
print("Force is",f"{force:.1f}", "N")
print("")
#Wavelength
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = 2*distance*sin((angle/180)*pi)
print("Wavelength is",f"{wavelength:.4f}","nm")
print("")
#Half life of Radon-222
print("This program calculates how much Radon-222 is left given time and initial amount")
daysOfDecay = float(input("Please enter the time (days): "))
initialMass = float(input("Please enter the initial amount (g): "))
radon222HalfLife = 3.8
radon222 = initialMass* (2**(-daysOfDecay/radon222HalfLife))
print("Radon-222 left is",f"{radon222:.2f}","g")
print("")
#Pressure
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
tempK = float(input("Please enter the temperature (K): "))
gasConstant = 8.314 #m^3Pa/K*mol
#PV = nRT P = pressure, V = volume, n = # of moles, R = universal gas constant(8.314), and T = temperature in Kelvin
pressure = ((moles*tempK*gasConstant)/volume)/1000
print("Pressure is",round(pressure),"kPa")