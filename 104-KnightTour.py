from graphics import *

board = []
boardIMG = []
letters = []
width = 4
height = 4
win = GraphWin("Knight's Tour", width * 100, height * 100)

class Cell:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False

def initBoard():
    for i in range(width):
        board.append([])
        boardIMG.append([])
        letters.append([])
        for j in range(height):
            board[i].append("-")
            boardIMG.append(Rectangle(Point(i * 100, j * 100), Point(i * 100 + 100, j * 100 + 100)))
            letters.append(Text(Point(i * 100 + 50, j * 100 + 50), "-")
    board[0][0] = "K"
    
    boardIMG[i][j].draw(win)
    letters[i][j].draw(win)
    
def findKnight():
    for i in range(width):
        for j in range(height):
            if(board[i][j] == "K"):
                return [i, j]
    return "Knight not found"
    
def checkValid(x, y):
    knightLoc = findKnight()
    oldX = knightLoc[0]
    oldY = knightLoc[0]
    if(oldY + 2 == y and oldX + 1 == x):
        return True
    elif(oldY + 2 == y and oldX - 1 == x):
        return True
    elif(oldY - 2 == y and oldX + 1 == x):
        return True
    elif(oldY - 2 == y and oldX - 1 == x):
        return True
    elif(oldY + 1 == y and oldX + 2 == x):
        return True
    elif(oldY + 1 == y and oldX - 2 == x):
        return True
    elif(oldY - 1 == y and oldX + 2 == x):
        return True
    elif(oldY - 1 == y and oldX - 2 == x):
        return True
    else:
        return False
    
def moveKnight(newX, newY):
    if(board[newX][newY] == "-" and checkValid(newX, newY)):
        knightLoc = findKnight()
        board[knightLoc[0]][knightLoc[1]] = "V"
        board[newX][newY] = "K"
        
def displayBoard():
    for i in range(width):
        for j in range(height):
            boardIMG[i][j].undraw()
            boardIMG[i][j].draw(win)
            
        
def MAIN():
    initBoard()
    print(findKnight())
    
MAIN()