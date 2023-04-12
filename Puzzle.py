#global variables
from gettext import find
import copy

rows, cols = (3,3)
gameBox = [[0]*cols]*rows

#gameBox = [[1,2,3],[4,5,0],[7,8,6]] # - Working
#gameBox = [[1,2,3],[4,0,5],[7,8,6]] # - Working
#gameBox = [[1,0,3],[4,2,5],[7,8,6]] # - Working
gameBox = [[2,0,8],[1,3,4],[7,6,5]]
#gameBox = [[1,0,3],[4,8,5],[7,2,6]]# initial state
goal = [[1,2,3],[4,5,6],[7,0,8]]# goal state
signs = [] # List to store signatures of gameBox states after movements of tiles

# ---Function to find misplaced tiles
def misplaced(goal, tgameBox):
    miscount = 0
    for x in range(3):
        for y in range(3):
            if goal[x][y] != tgameBox[x][y]:
                miscount += 1
    return miscount
# ---End function

# Function to find free tile index
def freeTile(tgameBox):
    for x in tgameBox:
        if 0 in x:
            return  [tgameBox.index(x),x.index(0)]
# ---End function

# ---Function to create signature of gameBox current form
def signature(tgameBox):
    sign = ""
    for x in range(rows):
        for y in range(cols): 
            sign = sign + str(tgameBox[x][y])
    return sign
# ---End function

# ---Function to find minimum heuristic value index
def minHeuristic(heuristicsList):
    min = 0
    for x in range(len(heuristicsList)-1):
        if heuristicsList[x] > heuristicsList[x+1]:
            min = x+1
    return min
# ---End function

# ---Move Functions
def left(tgameBox, row, col):
    temp = gameBox[row][col]
    tgameBox[row][col] = tgameBox[row][col-1]
    tgameBox[row][col-1] = temp

def right(tgameBox, row, col):
    temp = tgameBox[row][col]
    tgameBox[row][col] = tgameBox[row][col+1]
    tgameBox[row][col+1] = temp

def up(tgameBox, row, col):
    temp = tgameBox[row][col]
    tgameBox[row][col] = tgameBox[row-1][col]
    tgameBox[row-1][col] = temp

def down(tgameBox, row, col):
    print(row, col)
    temp = tgameBox[row][col]
    tgameBox[row][col] = tgameBox[row+1][col]
    tgameBox[row+1][col] = temp
# ---End move functions
        
# ---Function to find movements of free tile
def startGame(gameBox):
    tgameBox = copy.deepcopy(gameBox)
    signs.append(signature(gameBox))
    #print(tgameBox)
    print(gameBox)
    #misCount = misplaced(goal, gameBox)
    while misplaced(goal, gameBox) != 0:
        print("loop")
        tgameBox = copy.deepcopy(gameBox)
        heuristics = [10,10,10,10]# -- list to store Heuristic values of different states of gameBox
        fIndex = freeTile(gameBox)# -- Get index of free tile
        if fIndex[0] in range(0,rows-1):
            down(tgameBox, fIndex[0], fIndex[1])
            # -- Now generate signature of current state
            if signature(tgameBox) not in signs:
                #signs.append(signature(tgameBox))
                heuristics[0] = misplaced(goal,tgameBox)
            tgameBox = copy.deepcopy(gameBox)
        if fIndex[0] in range(1,rows):
            up(tgameBox, fIndex[0], fIndex[1])
            # -- Now generate signature of current state
            if signature(tgameBox) not in signs:
                #signs.append(signature(tgameBox))
                heuristics[1] = misplaced(goal,tgameBox)
            tgameBox = copy.deepcopy(gameBox)
        if fIndex[1] in range(0, cols-1):
            right(tgameBox, fIndex[0], fIndex[1])
            # -- Now generate signature of current state
            if signature(tgameBox) not in signs:
                #signs.append(signature(tgameBox))
                heuristics[2] = misplaced(goal,tgameBox)
            tgameBox = copy.deepcopy(gameBox)
        if fIndex[1] in range(1, cols+1):
            left(tgameBox, fIndex[0], fIndex[1])
            # -- Now generate signature of current state
            if signature(tgameBox) not in signs:
                #signs.append(signature(tgameBox))
                heuristics[3] = misplaced(goal,tgameBox)
            tgameBox = copy.deepcopy(gameBox)
        
        # -- Now find the minimum heurirsc cost and make changes in actual gameBox
        minIndex = heuristics.index(min(heuristics))
        if minIndex == 0:
            down(gameBox, fIndex[0], fIndex[1])
            signs.append(signature(gameBox))
            for x in gameBox:
                print(x)
            print("-------------------")
        if minIndex == 1:
            up(gameBox, fIndex[0], fIndex[1])
            signs.append(signature(gameBox))
            for x in gameBox:
                print(x)
            print("-------------------")
        if minIndex == 2:
            right(gameBox, fIndex[0], fIndex[1])
            signs.append(signature(gameBox))
            for x in gameBox:
                print(x)
            print("-------------------")
        if minIndex == 3:
            left(gameBox, fIndex[0], fIndex[1])
            signs.append(signature(gameBox))
            for x in gameBox:
                print(x)
            print("-------------------")
    print("Hurran ... We made it!!")
# ---End function

#MAIN
#print(misplaced(goal, gameBox))
#print(freeTile(gameBox))
startGame(gameBox)
#print(gameBox)