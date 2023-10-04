# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Andrew Marshall
# SK Thippireddy
# Rishi Bandhu
# Preston Montgomery
# Section:      522
# Assignment:   Lab 6.11
# Date:         6 10 2023
boardList = []
# print(boardList)
#each sublist will have [xvalue, yvalue, boolean isOccupied, boolean Color]
#boolean color: 
global color
global stop
color = True
#stop variable used to ensure that printBoard() doesn't run after askInput() is declared after the except statement.
stop = False
#white = False
#black = True
for y in range(1,10):
    for x in range(1,10):
        boardList += [[x,y]]
#print(boardList)
#how to find the index from values.

#Create a seperate print board that prints first stuff.

def printBoard():
    endStop = ""
    #print(boardList.index([1,1]))
    for i in boardList:
        if(i[0]%9 != 0): #if x-spot on board in 9, then start a new line for the next row
            endStop = ""
        else:
            endStop = "\n"
        try: #if a color and occupied boolean have been assigned to a spot, then print that color's symbol. Else print a .
            if(i[2] == True):
                if(i[3] == True):
                    print(chr(9675), end=endStop) #empty circle = black
                else:
                    print(chr(9679), end=endStop) #filled circle = white
            else:
                print(".",end=endStop)
        except:
            print(".",end=endStop)
    askInput() #continue thhe game, advance the turn.


def askInput():
    #global variables can be used and changed in or out of functions
    global color
    global stop
    #color used for switching turns
    if(color == True):
        print("Black's turn:")
    else:
        print("White's turn")
    print('TYPE "stop" to quit the game.')
    #determines whether input is stop or a number
    input1 = input("Please enter a number(integer) for the x-coordinate: ")
    if(input1.lower() == "stop"):
        stop = True
        return
    else:
        xCord = int(input1)
    #determines whether input is stop or a number
    input2 = input("Please enter a number(integer) for the y-coordinate: ")
    if(input2.lower() == "stop"):
        stop = True
        return
    else:
        yCord = int(input2)
    #tries to place a stone at the given spot on the board.
    try:
        inputIndex = boardList.index([xCord,yCord])
        boardList[inputIndex] += [True, color]
    #if an error raises, then that space is occupied, so try again
    except:
        print("\nTry Again. You can't pick a space that's already occupied or doesn't exist.\n")
        #rerun the askInput function
        askInput()
    color = not color #alternate color boolean so turns can switch
    #print(boardList[inputIndex])
    if(stop == False): #print board if game is not stopped
        printBoard()

#initialize game    
printBoard()