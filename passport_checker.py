# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 10 Group
# Date:         3 11 2023

def isValid(item):
    if "byr" not in item:
        return False
    if "iyr" not in item:
        return False
    if "eyr" not in item:
        return False
    if "hgt" not in item:
        return False
    if "hcl" not in item:
        return False
    if "pid" not in item:
        return False
    if "cid" not in item:
        return False
    return True
filName = input("Enter the name of the file: ")
passports = open(f"{filName}","r")
seperatedPassports = []
validPassList = []
currentPassPort = ""
for line in passports: #add each passport into a list
    if line == "\n":
        seperatedPassports.append(currentPassPort)
        currentPassPort = ""
    currentPassPort += f"{line}"
seperatedPassports.append(currentPassPort)
passports.close()
#print(seperatedPassports[0],end="")
validCount = 0
for passport in seperatedPassports:
    if(isValid(passport)):
        validCount+=1
        validPassList.append(passport)

validPassports = open("valid_passports.txt","w")
for passport in validPassList:
    if(validPassList[0] == passport):
        if(passport[0] == "\n"):
            passport = passport[1:]
        #print(passport)
    if(validPassList[-1] == passport):
        if(passport[-1] == "\n"):
            passport = passport[:-1]
    validPassports.write(passport)
validPassports.close()
print(f"There are {validCount} valid passports")
#print(seperatedPassports)