import turtle as turt
#import easygui as popUp
from math import sqrt
import numpy as np
import playsound #INSTALL VERSION 1.2.2
#put boom.wav into the same directory as this file.
totalBoardWidth = 200
totalBoardHeight = 200
winnerDeclared = False
turn = 1
def drawXMatrix(boardHeight):
    for i in range(boardHeight+1):
        turt.up()
        turt.setpos(0,-i*(totalBoardHeight/boardHeight))
        turt.down()
        turt.forward(totalBoardWidth)
    turt.up()
    turt.setpos(0,0)
    turt.down()
def drawYMatrix(boardWidth):
    turt.right(90)
    for i in range(boardWidth+1):
        turt.up()
        turt.setpos((i*(totalBoardWidth/boardWidth)),0)
        turt.down()
        turt.forward(totalBoardHeight)
    turt.up()
    turt.setpos(0,0)
    turt.down()
    turt.left(90)

def drawDiagonal(boardHeight, boardWidth,direction):
    turt.right(direction)
    startPos = 0
    if(direction>45):
        startPos = totalBoardWidth
    else:
        startPos = 0
    turt.setpos(startPos,0)
    segmentWidth = totalBoardWidth/boardWidth
    segmentHeight = totalBoardHeight/boardHeight
    for i in range(boardHeight):
        turt.up()
        turt.setpos(startPos,-i*(totalBoardHeight/boardHeight))
        turt.down()
        decreaser = -i + boardHeight
        diagLength = sqrt((decreaser*segmentWidth)**2 + (decreaser*segmentHeight)**2)
        turt.forward(diagLength)
    turt.up()
    turt.setpos(startPos,0)
    turt.down()
    for i in range(boardWidth):
        turt.up()
        if(startPos==0):
            turt.setpos(i*(totalBoardWidth/boardWidth),0)
        else:
            turt.setpos(startPos-(i*(totalBoardWidth/boardWidth)),0)
        turt.down()
        decreaser = -i + boardWidth
        diagLength = sqrt((decreaser*segmentWidth)**2 + (decreaser*segmentHeight)**2)
        turt.forward(diagLength)
    turt.up()
    turt.setpos(0,0)
    turt.down()
    turt.left(direction)

def drawCircleFrames(boardHeight,boardWidth,circleRadius):
    for i in range(boardHeight+1):
        for j in range(boardWidth+1):
            turt.up()
            turt.setpos((j*(totalBoardWidth/boardWidth)),(-i*(totalBoardHeight/boardHeight))-circleRadius)
            turt.down()
            turt.begin_fill()
            turt.circle(circleRadius)
            turt.end_fill()
    turt.up()
    turt.setpos(0,0)
    turt.down()

def initializeBoard(boardHeight,boardWidth,circleRadius):
    turt.speed(10.5)
    turt.setpos(0,0)
    turt.fillcolor("white")
    turt.pencolor("black")
    drawXMatrix(boardHeight)
    drawYMatrix(boardWidth)
    drawDiagonal(boardHeight,boardWidth,45)
    drawDiagonal(boardHeight,boardWidth,45+90)
    drawCircleFrames(boardHeight,boardWidth,circleRadius)

def askInputs():
    print("Hello. Welcome to Python Popup Teeko!")
    successFile = False
    boardContents = []
    while(successFile==False):
        try:
            boardFile = input("Please enter the name of the file containing the board: ")
            if(boardFile==""):
                print("Quitting...")
                return
            boardMatrix = open(boardFile,"r")
            boardContents = boardMatrix.readlines()
            successFile = True
        except:
            print()
            print("Try again! Please enter the full file name for the board.")
    boardMatrix.close()
    #print(boardContents)
    return boardContents
#C:\Users\Jacks\Desktop\ENGR102\ENGR-pyLabs\sounds\boom.mp3


def createMatrix(boardList):
    boardWidth = boardList[0].strip().split(" ")
    theBoard = np.zeros((len(boardWidth),len(boardList)))
    return theBoard

def drawUserCircles(boardMatrix,boardHeight,boardWidth,circleRadius):
    for i in range(boardHeight+1):
        for j in range(boardWidth+1):
            noCircle=False
            turt.up()
            turt.setpos((j*(totalBoardWidth/boardWidth)),(-i*(totalBoardHeight/boardHeight))-circleRadius)
            turt.down()
            if(boardMatrix[j,i]==1):
                turt.fillcolor("black")
                try:
                    playsound.playsound("boom.wav",False)
                except:
                    print("Sound not available")
            elif(boardMatrix[j,i]==2):
                turt.fillcolor("red")
                try:
                    playsound.playsound("boom.wav",False)
                except:
                    print("Sound not available")
            else:
                turt.fillcolor("white")
                noCircle=True
            if(noCircle):
                #turt.hideturtle()
                turt.pencolor("white")
                turt.begin_fill()
                turt.pos()
                turt.circle(circleRadius+1)
                turt.end_fill()
                turt.pencolor("black")
            else:
                #turt.showturtle()
                turt.begin_fill()
                turt.circle(circleRadius)
                turt.end_fill()
    turt.up()
    turt.setpos(0,0)
    turt.down()

def processTurn(matrix,startingPlayerColor,turnNumber):
    matrixWidth = matrix.shape[1]
    matrixHeight = matrix.shape[0]
    colorNumber = 0
    turnColor=""
    menuTitle = "Python Teeko"
    option1 = "-Type \"instructions\" to Display Instructions in Terminal"
    option2 = "-Type \"turns\" to Display Turn Count in Terminal"
    option3 = "-Type \"quit\" to Quit Early"
    menuList = f"{menuTitle}\n{option1}\n{option2}\n{option3}\n"
    placeMove=False
    if(turnNumber==1):
        if(startingPlayerColor == "Red"):
            turnColor = "Red"
            colorNumber = 2
        else:
            turnColor = "Black"
            colorNumber = 1
    else:
        if(turnNumber%2==1):
            if(startingPlayerColor == "Red"):
                turnColor = "Red"
                colorNumber = 2
            else:
                turnColor = "Black"
                colorNumber = 1
        else:
            if(startingPlayerColor == "Black"):
                turnColor = "Red"
                colorNumber = 2
            else:
                turnColor = "Black"
                colorNumber = 1
    if(turnNumber<9):    
        userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result==True):
                placeMove=True
            else:
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nEnter a Valid Coordinate!\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        nums = userInput.split(",")
        xCord=int(nums[0])-1
        yCord=int(nums[1])-1
        matrix[xCord,yCord] = colorNumber
        drawUserCircles(matrix,matrixHeight-1,matrixWidth-1,6) #6 is hardcoded circle radius
        return turnNumber+1
    else:
        userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput,turnColor)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result==True):
                nums = userInput.split(",")
                xCord=int(nums[0])-1
                yCord=int(nums[1])-1
                if(checkSurroundings(matrix,xCord,yCord)):
                    placeMove=True
                else:
                    userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nThat Piece Can't Move Anywhere. Try Again!\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            else:
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nPlease Choose a Tile With Your Color To Move From!\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        placeMove=False
        userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput2)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result==True):
                nums = userInput2.split(",")
                xCord=int(nums[0])-1
                yCord=int(nums[1])-1
                if(checkAdjacent(userInput2,userInput)):
                    placeMove=True
                else:
                    userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nPlease Choose an Adjacent Tile. Try Again!\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
            else:
                userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nEnter a Valid Coordinate!\nCoordinates: (1,1) - ({matrixWidth},{matrixHeight})")
        moveAdjacent(matrix,userInput2,userInput,turnColor)
        drawUserCircles(matrix,matrixHeight-1,matrixWidth-1,6) #6 is hardcoded circle radius
        return turnNumber+1

def checkMoves(matrix):
    """This function checks the state of the board to see if a player
    won. It takes in the numpy matrix of the game board and returns 0 if
    no player has won yet, returns "Black Won!" if black wins, and returns
    "Red Won!" if red wins."""
    matrixRows = matrix.shape[0]
    matrixColumns = matrix.shape[1]
    Hresults = checkHorizontal(matrix,matrixRows,matrixColumns)
    Vresults = checkVertical(matrix,matrixRows,matrixColumns)
    Dresults = checkDiagonal(matrix,matrixRows,matrixColumns)
    Sresults = checkSquare(matrix,matrixRows,matrixColumns)
    if(Hresults>0):
        if(Hresults==1):
            return "Black Won!"
        else:
            return "Red Won!"
    elif(Vresults>0):
        if(Vresults==1):
            return "Black Won!"
        else:
            return "Red Won!"
    elif(Dresults>0):
        if(Dresults==1):
            return "Black Won!"
        else:
            return "Red Won!"
    elif(Sresults>0):
        if(Sresults==1):
            return "Black Won!"
        else:
            return "Red Won!"
    return 0

def checkHorizontal(matrix,rows,columns):
    for i in range(rows):
        blackRow=0
        redRow=0
        #print(matrix[0:columns-1,i].sum())
        for j in range(columns):
            if(matrix[j,i] == 1):
                blackRow+=1
                redRow=0
            elif(matrix[j,i] == 2):
                redRow+=1
                blackRow=0
            #print code
            #print(blackRow)
            if(blackRow==4):
                return 1
            elif(redRow==4):
                return 2
            if(matrix[j,i] == 0): #if tile is empty.
                blackRow=0
                redRow=0
    return 0
        
def checkVertical(matrix,rows,columns):
    for i in range(columns):
        blackCol=0
        redCol=0
        #print(matrix[0:columns-1,i].sum())
        for j in range(rows):
            if(matrix[i,j] == 1):
                blackCol+=1
                redCol=0
            elif(matrix[i,j] == 2):
                redCol+=1
                blackCol=0
            #print(blackCol)
            if(blackCol==4):
                return 1
            elif(redCol==4):
                return 2
            if(matrix[i,j]==0): #if tile is empty.
                blackCol=0
                redCol=0
    return 0

def checkDiagonal(matrix,rows,columns):
    translateH=0
    translateV=1
    for l in range(2):
        if(l==0):
            horizontalStart=0
            translateH=1
        elif(l==1):
            horizontalStart=-1
            translateH=-1
        for k in range(2):
            for i in range(rows):
                if(k==0):
                    startX = horizontalStart
                    startY = i
                else:
                    if(l==0):
                        startX = i
                        startY = 0
                    elif(l==1):
                        startX = -1 + -i
                        startY = 0
                blackDiag = 0
                redDiag = 0
                for j in range(i,columns):
                    if(matrix[startX,startY]==1):
                        blackDiag+=1
                        redDiag=0
                    if(matrix[startX,startY]==2):
                        redDiag+=1
                        blackDiag=0
                    #return statements
                    #print(blackDiag)
                    if(blackDiag==4):
                        return 1
                    elif(redDiag==4):
                        return 2
                    if(matrix[startX,startY]==0): #if tile is empty.
                        blackDiag=0
                        redDiag=0
                    startX+=translateH
                    startY+=translateV
    return 0

def checkSquare(matrix,rows,columns):
    for i in range(rows-1):
        for j in range(columns-1):
            if(matrix[j,i]==1):
                if(matrix[j+1,i]==1):
                    if(matrix[j,i+1]==1):
                        if(matrix[j+1,i+1]==1):
                            return 1
            elif(matrix[j,i]==2):
                if(matrix[j+1,i]==2):
                    if(matrix[j,i+1]==2):
                        if(matrix[j+1,i+1]==2):
                            return 2
    return 0

def moveAdjacent(matrix,moveToInput,moveFromInput,color):
    numsTo = moveToInput.split(",")
    xToCord=int(numsTo[0])-1
    yToCord=int(numsTo[1])-1
    numsFrom = moveFromInput.split(",")
    xFromCord=int(numsFrom[0])-1
    yFromCord=int(numsFrom[1])-1
    matrix[xFromCord,yFromCord]=0
    if(color == "Black"):
        matrix[xToCord,yToCord]=1
    elif(color == "Red"):
        matrix[xToCord,yToCord]=2

def checkAdjacent(moveToInput,moveFromInput):
    """This function checks if an adjacent move is valid. Valid
    adjacent moves are cardinal and intercardinal directions around
    the starting point, not including the edge of the board, which counts
    as out of bounds. This function takes in the string containing the
    coordinates of the piece to be moves, as well as the coordinates
    for where to move the piece. It returns true if the coordinate
    the piece moves to is a valid adjacent spot, returns false if not."""
    numsTo = moveToInput.split(",")
    xToCord=int(numsTo[0])-1
    yToCord=int(numsTo[1])-1
    numsFrom = moveFromInput.split(",")
    xFromCord=int(numsFrom[0])-1
    yFromCord=int(numsFrom[1])-1
    # print(xFromCord,yFromCord)
    # print(xToCord,yToCord)
    # print()
    # print(abs(xToCord-xFromCord),abs(yToCord-yFromCord))
    if(xToCord-xFromCord==0 and yToCord-yFromCord==0):
        return False
    if(abs(xToCord-xFromCord)>1 and abs(yToCord-yFromCord)>1):
        return False
    else:
        if(xToCord-xFromCord==0 and abs(yToCord-yFromCord)==1):
            return True
        elif(abs(xToCord-xFromCord)==1 and yToCord-yFromCord==0):
            return True
        elif(abs(xToCord-xFromCord)==1 and abs(yToCord-yFromCord)==1):
            return True
        else:
            return False

def isValidMove(matrix,moveToInput,moveFromInput=False):
    matrixWidth = matrix.shape[1]
    matrixHeight = matrix.shape[0]
    if(moveToInput=="quit"):
        return "quit"
    elif(moveToInput=="instructions"):
        return "instructions"
    elif(moveToInput=="turns"):
        return "turns"
    try:
        nums = moveToInput.split(",")
        if(len(nums)>2):
            return False
        xCord=int(nums[0])-1
        yCord=int(nums[1])-1
        if(xCord<0 or xCord>matrixWidth-1):
            return False
        if(yCord<0 or yCord>matrixHeight-1):
            return False
        if(moveFromInput==False):
            if(matrix[xCord,yCord]==0):
                return True
            else:
                return False
        else:
            
            if(matrix[xCord,yCord]==1 and moveFromInput=="Black"):
                return True
            elif(matrix[xCord,yCord]==2 and moveFromInput=="Red"):
                return True
            else:
                return False
    except:
        return False
        
def checkSurroundings(matrix,xCord,yCord):
    """This function checks to make sure that a piece can be moved
    adjacently before selecting it. It predetermines all the adjacent
    tiles, giving the result into a list, if that list contains any valid
    adjacent points, this function returns true, and returns false if not.
    This function takes in the numpy matrix for the board, and the x and y
    coordinates. These allow it to predetermine validity for a given tile."""
    matrixWidth = matrix.shape[1]
    matrixHeight = matrix.shape[0]
    adjacentCheckList = []
    adjacentTranslations = [[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1],[-1,0]]
    #1 = filled spot or edge of board
    #2 = open spot
    for trans in adjacentTranslations:
        try:
            adjustedX = xCord+trans[0]
            adjustedY = yCord+trans[1]
            if(adjustedX == -1):
                adjustedX = -1 - matrixWidth
            if(adjustedY == -1):
                adjustedY = -1 - matrixHeight
            if(matrix[adjustedX,adjustedY]==0):
                adjacentCheckList.append(2)
            else:
                adjacentCheckList.append(1)
        except:
            adjacentCheckList.append(1)
    #print(xCord,yCord)
    #print(adjacentCheckList)
    if(2 in adjacentCheckList):
        return True
    else:
        return False






#driver code
boardContentes = askInputs()
matrix = createMatrix(boardContentes)
boardMatrixWidth = matrix.shape[1]
boardMatrixHeight = matrix.shape[0]
initializeBoard(boardMatrixHeight-1,boardMatrixWidth-1,10) #10 is hardcoded outer circle radius


while(winnerDeclared==False):
    if(turn<9):
        turn = processTurn(matrix,"Black",turn)
        result = checkMoves(matrix)
        if(result=="Black Won!"):
            winnerDeclared=True
            turt.textinput("Winner!","Black Won!")
            turt.done()
        elif(result=="Red Won!"):
            winnerDeclared=True
            turt.textinput("Winner!","Black Won!")
            turt.done()
        elif(turn==0): #quit return selection
            print("Bye!")
            break
    else: #IF NO ONE WINS AFTER THIS, START MOVING PIECES
        turn = processTurn(matrix,"Black",turn)
        result = checkMoves(matrix)
        if(result=="Black Won!"):
            winnerDeclared=True
            turt.textinput("Winner!","Black Won!")
            turt.done()
        elif(result=="Red Won!"):
            winnerDeclared=True
            turt.textinput("Winner!","Black Won!")
            turt.done()
        elif(turn==0): #quit return selection
            print("Bye!")
            break

print("Done")
turt.done()