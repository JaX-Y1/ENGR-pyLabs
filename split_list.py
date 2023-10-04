# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Andrew Marshall
# Section:      522
# Assignment:   Lab 7.27
# Date:         3 10 2023
userInput = input("Enter numbers: ")
words = userInput.rsplit(" ")
for i in range(len(words)):
    words[i] = int(words[i])
#print(words)
for i in range(len(words)):
    iter = 0
    leftAdd = 0
    rightAdd = 0
    while iter<=i: #adds all the elements up to and including i in the current iteration.
        leftAdd += words[iter]
        iter +=1
    #print(f"left sum: {leftAdd}")
    iter = i+1 #use an iterator value 1 more than the left
    while iter<=len(words)-1: #add the remaining elements after the left sum
        rightAdd += words[iter]
        iter +=1
    #print(f"right sum: {rightAdd}")
    if(leftAdd == rightAdd):
        #print(f"List splits evenly at index {i}.")
        print(f"Left: {words[0:i+1]}")
        print(f"Right: {words[i+1:]}")
        print(f"Both sum to {leftAdd}")
        break
    else:
        if(i == len(words)-1):
            print("Cannot split evenly")    
   
