# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section: 522
# Assignment:   Lab 9.15
# Date:         27 10 2023

def print_puzzle(puzzle):
    ''' Print puzzle as a long division problem. '''
    puzzle = puzzle.split(',')
    for i in range(len(puzzle)):
        if i == 1:
            print(f'{len(puzzle[i].split("|")[1]) * "_": >16}')
        print(f'{puzzle[i]: >16}')
        if i > 1 and i % 2 == 0:
            print(f"{'-'*len(puzzle[i]): >16}")

def get_valid_letters(puzString):
    uniqueLetters = []
    for char in puzString:
        if(char.isalpha() and char not in uniqueLetters and len(uniqueLetters)<=10):
            uniqueLetters.append(char)
    return "".join(uniqueLetters)

def is_valid_guess(validString, userGuess):
    if(len(userGuess)!=10):
        return False
    for char in userGuess:
        if char not in validString or userGuess.count(char)>1:
            break
    else:
        return True
    return False

def check_user_guess(dividend, quotient, divisor, remainder):
    if(dividend == quotient*divisor + remainder):
        return True
    else:
        return False

def make_number(wordToConvert, userStringKey):
    keyValueString = {}
    numberList = []
    for index, value in enumerate(userStringKey):
        keyValueString[value] = index
    for char in wordToConvert:
        if char in keyValueString:
            numberList.append(str(keyValueString[char]))
    return int("".join(numberList))

def make_numbers(puzString, userGuess):
    puzString = puzString.split(",")
    dividendDivisorString = puzString[1].split("|")

    dividendString = dividendDivisorString[1].strip()
    divisorString = dividendDivisorString[0].strip()
    quotientString = puzString[0]
    remainderString = puzString[-1]

    dividend = make_number(dividendString, userGuess)
    divisor = make_number(divisorString,userGuess)
    quotient = make_number(quotientString,userGuess)
    remainder = make_number(remainderString,userGuess)
    return dividend, quotient, divisor, remainder

def main():
    # The lines below demonstrate what the print_puzzle function outputs.
    #test puzzle: "RUE,EAR | RUMORS,UEII  ,UKTR ,EAR ,KEOS,KAIK,USA"
    puzzle = input("Enter a word arithmetic puzzle: ")
    print()
    print_puzzle(puzzle)
    print()
    userInput = input("Enter your guess, for example ABCDEFGHIJ: ")
    if(is_valid_guess(get_valid_letters(puzzle),userInput)):
        a,b,c,d = make_numbers(puzzle,userInput)
        if(check_user_guess(a,b,c,d)):
            print("Good job!")
        else:
            print("Try again!")
    else:
        print("Your guess should contain exactly 10 unique letters used in the puzzle.")
    

if __name__ == '__main__':
    main()

