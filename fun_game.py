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
    """Draws the vertical gridlines. Takes in board height."""
    for i in range(boardHeight+1):
        turt.up()
        turt.setpos(0,-i*(totalBoardHeight/boardHeight))
        turt.down()
        turt.forward(totalBoardWidth)
    turt.up()
    turt.setpos(0,0)
    turt.down()
def drawYMatrix(boardWidth):
    """Draws the horizontal gridlines. Takes in board width."""
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
    """Draws the diagonal board gridlines. Takes in board height, width, and the direction (down left, down right)"""
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
    """Draws the tile frames on the board for pieces to go on. Takes in board height, width, and radius of the frame outlines."""
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
    """Draws the intitial board. Takes in board height,width, and radius for tiles"""
    turt.speed(10.5)
    turt.setpos(0,0)
    turt.fillcolor("white")
    turt.pencolor("black") #the board can be drawn with an adaptable height/width.
    drawXMatrix(boardHeight)
    drawYMatrix(boardWidth)
    drawDiagonal(boardHeight,boardWidth,45)
    drawDiagonal(boardHeight,boardWidth,45+90)
    drawCircleFrames(boardHeight,boardWidth,circleRadius)

def askInputs():
    """Asks the user for the filename of the .csv file containing the board 
    width/height. returns a string list containing the board contents."""
    print("Hello. Welcome to Python Teeko!")
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
#PATH
#C:\Users\Jacks\Desktop\ENGR102\ENGR-pyLabs\sounds\boom.mp3


def createMatrix(boardList):
    """Creates the numpy array with the board height/width. Takes in a 
    list of strings containing the board contents. Returns a numpy matrix."""
    if(boardList==None):
        junk = np.array([-1])
        return junk
    boardWidth = boardList[0].strip().split(" ")
    theBoard = np.zeros((len(boardWidth),len(boardList)))
    return theBoard

def drawUserCircles(boardMatrix,boardHeight,boardWidth,circleRadius):
    """Draws the player pieces and plays a sound when each is drawn. Takes in a numpy matrix
    height, width of the board, and the radius for the player piece circles."""
    for i in range(boardHeight+1):
        for j in range(boardWidth+1):
            noCircle=False
            turt.up()
            turt.setpos((j*(totalBoardWidth/boardWidth)),(-i*(totalBoardHeight/boardHeight))-circleRadius)
            turt.down()
            if(boardMatrix[j,i]==1):
                turt.fillcolor("black")
                try: #sound module is buggy, so this try/except is used so the game can still be played in sound not working.
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
    """Asks for the user move input, including menu options. Returns the currentTurn + 1 or 
    the varius menu options. Takes in the matrix, which player color starts first, and current turn number."""
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
    if(turnNumber<9):    #---THIS section runs for the first 8 turns
        userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result==True):
                placeMove=True
            else:
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nEnter a Valid Coordinate!\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
        nums = userInput.split(",")
        xCord=int(nums[0])-1
        yCord=int(nums[1])-1
        matrix[xCord,yCord] = colorNumber
        drawUserCircles(matrix,matrixHeight-1,matrixWidth-1,6) #6 is hardcoded circle radius
        return turnNumber+1
    else: #--THIS section runs for the rest of the game until someone wins.
        userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput,turnColor)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhich Piece Do You Want To Move?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result==True):
                nums = userInput.split(",")
                xCord=int(nums[0])-1
                yCord=int(nums[1])-1
                if(checkSurroundings(matrix,xCord,yCord)):
                    placeMove=True
                else:
                    userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nThat Piece Can't Move Anywhere. Try Again!\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            else:
                userInput = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nPlease Choose a Tile With Your Color To Move From!\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
        placeMove=False
        userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
        while(placeMove==False):
            result = isValidMove(matrix,userInput2)
            if(result=="quit"):
                return 0
            elif(result=="instructions"):
                print("these are the instructions")
                userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
            elif(result=="turns"):
                print(f"Turn: {turnNumber}")
                userInput2 = turt.textinput(f"{turnColor}'s Move", f"{menuList}\n\nWhere To?\nCoordinates: (columns,rows)\nCoordinate Range: (1,1) - ({matrixWidth},{matrixHeight})")
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
    """Checks if a horizontal four-in-a-row has occured. Returns 0 if False, 1 if black, 2 if red.
    Takes in the matrix, and the number of rows and columns."""
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
    """Checks if a vertical four-in-a-row has occured. Returns 0 if False, 1 if black, 2 if red.
    Takes in the matrix, and the number of rows and columns."""
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
    """Checks if a diagonal four-in-a-row has occured. Returns 0 if False, 1 if black, 2 if red.
    Takes in the matrix, and the number of rows and columns."""
    translateH=0
    translateV=1
    for l in range(2): #runs twice for down left and down right
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
    """Checks if a square has been formed, which is also a win condition. Returns 0 if False, 1 if black, 2 if red.
    Takes in the matrix, and the number of rows and columns."""
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
    """Moves a piece on the board to an adjacent spot by deleting the old spot and adding the piece to
    the new spot. Takes in the matrix, strings containing the move To and move From inputs,
    and the color of the player piece moving."""
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
    """This function checks to make sure that the spot being moved to is valid. 
    It takes in the numpy matrix for the board, a string containing
    the move to input, and an optional string containing the move from input. The move from
    input additionally checks if the position being moved from contains
    a player piece and that it's the same color as current turn's player. Returns True/False
    if the move is valid or not. Returns a string contaning the menu option if a menu
    option was inputted."""
    matrixWidth = matrix.shape[1]
    matrixHeight = matrix.shape[0]
    if(moveToInput=="quit"): #-- this part checks for menu options
        return "quit"
    elif(moveToInput=="instructions"):
        return "instructions"
    elif(moveToInput=="turns"):
        return "turns" #--
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
if(matrix.ndim!=1):
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
    turt.done()            
print("Done")
