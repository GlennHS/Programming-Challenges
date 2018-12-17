from graphics import *
from random import *
import time

win = GraphWin("Game Of Life", 400, 530)

class Cell:
    
    def __init__(self, position, isAlive):
        self.position = position
        self.isAlive = isAlive
        self.img = Rectangle(Point(self.position[0] * 20, self.position[1] * 20), Point(self.position[0] * 20 + 20, self.position[1] * 20 + 20))
        self.img.draw(win)
        
    def drawSelf(self):
        self.img.undraw()
        if not self.isAlive:
            self.img.setFill("white")
        else:
            self.img.setFill("black")
        self.img.draw(win)
        
    def toggleAlive(self):
        if self.isAlive:
            self.isAlive = False
        else:
            self.isAlive = True
            
    def getNumNeighbours(self, gridArray):
        numNeighbours = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if not(i == 0 and j == 0):
                    checkPos = [0, 0]
                    checkPos[0] = self.position[0] + i
                    checkPos[1] = self.position[1] + j
                    if checkPos[0] < 20 and checkPos[1] < 20 and checkPos[0] >= 0 and checkPos[1] >= 0:
                        cellToCheck = gridArray[checkPos[0]][checkPos[1]]
                        if cellToCheck.isAlive:
                            numNeighbours += 1
        return numNeighbours
        
    def simulate(self, gridArray):
        numNeighbours = self.getNumNeighbours(gridArray)
        if (numNeighbours == 3):
            self.isAlive = True
        elif(self.isAlive == True and numNeighbours == 2):
            self.isAlive = True
        else:
            self.isAlive = False
        
        
def createNewGrid():
    finalArray = []
    for i in range(20):
        innerArray = []
        for j in range(20):
            innerArray.append(Cell([i, j], False))
        finalArray.append(innerArray)
    return finalArray
    

def drawGrid(gridArray):
    for i in range(20):
        for j in range(20):
            gridArray[i][j].drawSelf()
            
def randomLayout(gridArray):
    for i in range(20):
        for j in range(20):
            randNum = randint(0,1)
            if randNum == 0:
                gridArray[i][j].isAlive = True
            else:
                gridArray[i][j].isAlive = False
            
def drawStart():
    startButton = Rectangle(Point(140, 420), Point(260, 460))
    startText = Text(Point(200, 440), "START")
    startButton.draw(win)
    startText.draw(win)
    
def drawRandomButton():
    randButton = Rectangle(Point(140, 480), Point(260, 520))
    randText = Text(Point(200, 500), "RANDOM")
    randButton.draw(win)
    randText.draw(win)
    
def beginSimulation(gridArray):
    while True:
        time.sleep(0.5)
        for i in range(20):
            for j in range(20):
                gridArray[i][j].simulate(gridArray)
        drawGrid(gridArray)
            
    
def Main():        
    running = False
    gridArray = createNewGrid()
    drawGrid(gridArray)
    drawStart()
    drawRandomButton()
    while not running:
        mouseRaw = win.getMouse()
        mouseX = mouseRaw.getX()
        mouseY = mouseRaw.getY()
        if mouseX >= 140 and mouseX <= 260 and mouseY > 270 and mouseY < 460:
            running = True
            beginSimulation(gridArray)
        elif mouseX >= 140 and mouseX <= 260 and mouseY > 470 and mouseY < 530:
            randomLayout(gridArray)
            drawGrid(gridArray)
        else:
            cellClickedX = int(mouseX / 20)
            cellClickedY = int(mouseY / 20)
            gridArray[cellClickedX][cellClickedY].toggleAlive()
            drawGrid(gridArray)
    
    
Main()
