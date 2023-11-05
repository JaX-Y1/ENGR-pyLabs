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

def formatPassport(passPort):
    passPort = passPort.replace("\n"," ")
    fields = passPort.strip().split(" ")
    return fields

def validBYR(birthYear):
    year = int(birthYear.split(":")[1])
    if(len(birthYear.split(":")[1])!=4):
        return False
    if(1920<=year<=2007):
        return True
    else:
        return False

def validIYR(issueYear):
    year = int(issueYear.split(":")[1])
    if(len(issueYear.split(":")[1])!=4):
        return False
    if(2013<=year<=2023):
        return True
    else:
        return False 

def validEYR(expireYear):
    year = int(expireYear.split(":")[1])
    if(len(expireYear.split(":")[1])!=4):
        return False
    if(2023<=year<=2033):
        return True
    else:
        return False 
def validHGT(height):
    heightNum = height.split(":")[1]
    if "cm" in heightNum:
        heightNum = heightNum.replace("cm","")
        heightNum = int(heightNum)
        if(150<=heightNum<=193):
            return True
        else:
            return False
    elif "in" in heightNum:
        heightNum = heightNum.replace("in","")
        heightNum = int(heightNum)
        if(59<=heightNum<=76):
            return True
        else:
            return False
    else:
        return False
def validHCL(hairColor):
    color = hairColor.split(":")[1]
    if color[0]!="#":
        return False
    for i in color[1:]:
        if (i not in "0123456789") and (i not in "abcdef"):
            return False
    else:
        return True
def validPID(passID):
    iD = passID.split(":")[1]
    try:
        int(iD)
        if(len(iD)==9):
            return True
        else:
            return False
    except:
        return False
def validCID(countryID):
    newConID = countryID.split(":")[1]
    try:
        int(newConID)
        if(newConID[0] == "0"):
            return False
        if(len(newConID)==3):
            return True
        else:
            return False
    except:
        return False
    
def isValid2(formattedPass):
    for field in formattedPass:
        if("byr" in field):
            if(validBYR(field)==False):
                return False
        elif("iyr" in field):
            if(validIYR(field)==False):
                return False
        elif("eyr" in field):
            if(validEYR(field)==False):
                return False
        elif("hgt" in field):
            if(validHGT(field)==False):
                return False
        elif("hcl" in field):
            if(validHCL(field)==False):
                return False
        elif("pid" in field):
            if(validPID(field)==False):
                return False
        elif("cid" in field):
            if(validCID(field)==False):
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
#print(formatPassport(seperatedPassports[0]))
validCount = 0
for passport in seperatedPassports:
    if(isValid(passport)):
        formatPass = formatPassport(passport)
        if(isValid2(formatPass)):
            validCount+=1
            validPassList.append(passport)

validPassports = open("valid_passports2.txt","w")
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
#a=formatPassport(seperatedPassports[-1])
#print(a)
#print(validHGT("cid:143"))
