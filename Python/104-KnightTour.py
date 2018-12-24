from graphics import *

board = []
width = 4
height = 4
win = GraphWin("Knight's Tour", width * 100, height * 100)

class Cell:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.knight = False
        self.img = Rectangle(Point(self.x * 100, self.y * 100), Point(self.x * 100 + 100, self.y * 100 + 100))
        self.img.draw(win)
        self.changeImage()
        
    def changeImage(self):
        self.img.setFill("red")
        if(self.knight):
            self.img.setFill("yellow")
        elif(self.visited):
            self.img.setFill("blue")
       
def redrawBoard():
    for i in range(width):
        for j in range(height):
            board[i][j].changeImage()
            
def init():
    for i in range(width):
        board.append([])
        for j in range(height):
            board[i].append(Cell(i, j))
    board[0][0].knight = True
    redrawBoard()
    
def whereKnight():
    for i in range(width):
        for j in range(height):
            if(board[i][j].knight == True):
                return[i, j]
    return "ERROR: Knight not found!"
    
def checkValidMove(newX, newY):
    if(board[newX][newY].visited == False):
        knightPos = whereKnight()
        knightX = knightPos[0]
        knightY = knightPos[1]
        if(knightX + 1 == newX and knightY + 2 == newY):
            return True
        elif(knightX + 1 == newX and knightY - 2 == newY):
            return True
        elif(knightX - 1 == newX and knightY + 2 == newY):
            return True
        elif(knightX - 1 == newX and knightY - 2 == newY):
            return True
        elif(knightX + 2 == newX and knightY + 1 == newY):
            return True
        elif(knightX + 2 == newX and knightY - 1 == newY):
            return True
        elif(knightX - 2 == newX and knightY + 1 == newY):
            return True
        elif(knightX - 2 == newX and knightY - 1 == newY):
            return True
        else:
            return False
        
# def gameLost():
#     knightPos = whereKnight()
#     knightX = knightPos[0]
#     knightY = knightPos[1]
#     if(board[knightX + 1][knightY + 2].visited == False):
#         return False
#     elif(board[knightX - 1][knightY + 2].visited == False):
#         return False
#     elif(board[knightX + 1][knightY - 2].visited == False):
#         return False
#     elif(board[knightX - 1][knightY - 2].visited == False):
#         return False
#     elif(board[knightX + 2][knightY + 1].visited == False):
#         return False
#     elif(board[knightX - 2][knightY + 1].visited == False):
#         return False
#     elif(board[knightX + 2][knightY - 1].visited == False):
#         return False
#     elif(board[knightX - 2][knightY - 1].visited == False):
#         return False
#     else:
#         return True
        
def moveKnight(newX, newY):
    if(checkValidMove(newX, newY)):
        current = whereKnight()
        board[current[0]][current[1]].knight = False
        board[current[0]][current[1]].visited = True
        board[newX][newY].knight = True
        redrawBoard()
        
def getClick(rawX, rawY):
    for i in range(width):
        for j in range(height):
            if(rawX <= i * 100 + 100 and rawY <= j * 100 + 100):
                return [i, j]
        
def gameWon():
    for i in range(width):
        for j in range(height):
            if(board[i][j].visited == False and board[i][j].knight == False):
                return False
    return True
    
def MAIN():
    init()
    won = False
    # lost = False
    # while(not won and not lost):
    while(not won):
        loc = win.getMouse()
        pureClick = getClick(loc.getX(), loc.getY())
        moveKnight(pureClick[0], pureClick[1])
        # lost = gameLost()
        won = gameWon()
    # if(lost):
    #     print("Unlucky, have another go!")
    else:
        print("CONGRATULATIONS!!")
    
MAIN()