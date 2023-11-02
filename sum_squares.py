# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 10.13 Group
# Date:         31 10 2023

from time import time
from math import *
def list_nums(n, shouldCount=False):
    '''chatgpt solution'''
    counter = []
    aBig = False
    addToD = True
    addToC = True
    addToB = True
    
    for a in range(0, n):
        bBig = False
        if(aBig == False):
            if(a**2>n):
                aBig=True
        else:
            break
        for b in range(a, n):
            cBig = False
            addToC = True
            if(bBig == False):
                if(b**2>n):
                    bBig=True
                if(b**2 + a**2>n):
                    break
            else:
                break
            for c in range(b, n):
                dBig = False
                addToD = True
                if(cBig == False):
                    if(c**2>n):
                        cBig=True
                    if(c**2 + b**2 + a**2>n):
                        break
                else:
                    break
                if a**2 + b**2 + c**2 + (n-(a**2+b**2+c**2)) == n and (n-(a**2+b**2+c**2))!=n:
                    d = sqrt((n-(a**2+b**2+c**2)))
                    if(shouldCount == False):
                        if(d == int(d)):
                            return [a, b, c, int(d)]
                    else:
                        if(d == int(d)):
                            sortList = [a,b,c,int(d)]
                            sortList.sort()
                            if(sortList not in counter):
        
                                counter += [sortList]


                # for d in range(c, n):
                #     if(dBig == False):
                #         if(d**2>n):
                #             dBig=True
                #         if(d**2 + c**2 + b**2 + a**2>n):
                #             break
                        
                #     else:
                #         break
                #     if a**2 + b**2 + c**2 + d**2 == n:
                #         if(shouldCount == False):
                #             return [a, b, c, d]
                #         else:
                #             if([a,b,c,d] not in counter):
                #                 counter+= [[a,b,c,d].sort()]
    if(shouldCount == True):
        return len(counter)
                            

def count_sets(posInt):
    return int(list_nums(posInt,True))


# how to measure how long your function takes to run:
t1 = time() # get start time
#print(count_sets(84000))
#print(list_nums(10))
t2 = time() # get end time
print(f"This took {t2-t1} seconds") # print result

