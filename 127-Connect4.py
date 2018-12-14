from graphics import *

grid = [[],[],[],[],[],[],[]];
turn = "r";
win = GraphWin("Connect 4", 700, 700)
winner = "-"

def clearGrid():
    for i in range(len(grid)):
        for i in range(7):
            grid[i] += ("-")

def dropCounter(colour, col):
    counterPlaced = False;
    for i in range(6, -1, -1):
        if(grid[i][col] == "-" and not(counterPlaced)):
            grid[i][col] = colour;
            counterPlaced = True;
      
def drawGrid(player):
    gridGFX = Rectangle(Point(0, 0), Point(700, 700))
    gridGFX.setFill("blue")
    gridGFX.draw(win)
    for i in range (len(grid)):
        for j in range (len(grid[i])):
            c = Circle(Point(i * 100 + 50, j * 100 + 50), 50)
            color = "grey"
            if(grid[j][i] == "r"):
                color = "red"
            elif(grid[j][i] == "y"):
                color = "yellow"
            c.setFill(color)
            c.draw(win)
    indic = Circle(Point(30, 30), 15)
    if(player == 'r'):
        colour = 'red'
    else:
        colour = 'yellow'
    indic.setFill(colour)
    indic.draw(win)
            
def playTurn(player):
    clickLoc = win.getMouse()
    if(clickLoc.getX() < 100):
        col = 0
    elif(clickLoc.getX() < 200):
        col = 1
    elif(clickLoc.getX() < 300):
        col = 2
    elif(clickLoc.getX() < 400):
        col = 3
    elif(clickLoc.getX() < 500):
        col = 4
    elif(clickLoc.getX() < 600):
        col = 5
    else:
        col = 6
    dropCounter(player, col)

 # def checkWin():
 #     for i in range(len(grid)):
 #         for j in range(len(grid[i])):
 #             
    

def MAIN():
    clearGrid()
    player = 'r'
    drawGrid(player)
    while(winner == "-"):
        drawGrid(player)
        playTurn(player)
        if(player == 'r'):
            player = 'y'
        else:
            player = 'r'

MAIN()