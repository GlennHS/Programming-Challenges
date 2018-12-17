from graphics import *

win = GraphWin("Connect4", 700, 700)
frame = Rectangle(Point(0, 0), Point(700, 700))
frame.setFill("blue")
frame.draw(win)

grid = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']] # Logical Side
board = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']] # Graphical side

def clearBoard():
    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j] = '-'
            board[i][j] = Circle(Point(i * 100 + 50, j * 100 + 50), 50)
            board[i][j].setFill("grey")
            board[i][j].draw(win)

def drawBoard():
    updateColours()
    for i in range(len(board)):
        for j in range(len(board[i])):
            try:
                board[i][j].undraw()
            except:
                pass
            board[i][j].draw(win)
            

def updateColours():
    for i in range(len(grid)):
        for j in range(len(grid)):
            if(grid[i][j] == 'r'):
                board[i][j].setFill('red')
            elif(grid[i][j] == 'y'):
                board[i][j].setFill('yellow')
            else:
                board[i][j].setFill('grey')

def dropCounter(col, player):
    counterDropped = False
    for i in range(len(grid), 0, -1):
        if((grid[col][i - 1] == '-') and (counterDropped == False)):
            grid[col][i - 1] = player
            counterDropped = True
    drawBoard()
    return counterDropped

def checkWin():
    for i in range (len(grid)):
        for j in range(len(grid[i])):
            colour = grid[i][j]
            if(not colour == '-'):
                try:
                    if(grid[i][j+1] == colour and grid[i][j+2] == colour and grid[i][j+3] == colour):
                        return True
                except:
                    pass
                try:
                    if(grid[i+1][j] == colour and grid[i+2][j] == colour and grid[i+3][j] == colour):
                        return True
                except:
                    pass
                try:
                    if(grid[i+1][j+1] == colour and grid[i+2][j+2] == colour and grid[i+3][j+3] == colour):
                        return True
                except:
                    pass
                try:
                    if(grid[i-1][j+1] == colour and grid[i-2][j+2] == colour and grid[i-3][j+3] == colour):
                        return True
                except:
                    pass
    return False
    
def init():
    winner = '-'
    clearBoard()
    drawBoard()
    player = 'r' # Red always starts
    indicator = Circle(Point(25, 25), 10)
    indicator.draw(win)
    while(winner == '-'):
        indicator.undraw()
        if(player == 'r'):
            indicator.setFill('red')
        else:
            indicator.setFill('yellow')
        indicator.draw(win)
        col = win.getMouse().getX()
        if(col < 100):
            col = 0
        elif(col < 200):
            col = 1
        elif(col < 300):
            col = 2
        elif(col < 400):
            col = 3
        elif(col < 500):
            col = 4
        elif(col < 600):
            col = 5
        else:
            col = 6
        counterDropped = dropCounter(col, player)
        if(checkWin()):
            winner = player
        if(counterDropped):
            if(player == 'r'):
                player = 'y'
            else:
                player = 'r'
    print(winner)
    
init()