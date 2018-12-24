#pylint: skip-file
from graphics import *

close = False

win = GraphWin("Pixel Editor", 600, 600)
palette = []
currentColour = "black"
canvas = []

class Pixel:
    
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.img = Rectangle(Point(10 * xPos, 10 * yPos), Point(10 * xPos + 10, 10 * yPos + 10))
        self.img.draw(win)
        
    def drawSelf(self):
        try:
            self.img.undraw()
        except:
            pass
        self.img.setFill(currentColour)
        self.img.draw(win)        
        
class PaletteBtn:
    
    def __init__(self, xPos, colour):
        self.xPos = xPos
        self.colour = colour
        self.img = Rectangle(Point(50 * xPos, 550), Point(50 * xPos + 50, 600))
        self.img.setFill(self.colour)
        self.img.draw(win)
        

def handleClick(mouse):
    global currentColour
    handled = False
    if(mouse.getY() >= 550):
        for i in range(len(palette) + 1):
            if(not handled):
                if(mouse.getX() <= i * 50):
                    currentColour = palette[i - 1].colour
                    handled = True
    else:
        for x in range(len(canvas) + 1):
            for y in range(len(canvas[0]) + 1):
                if(not handled):
                    if(mouse.getX() <= x * 10 and mouse.getY() <= y * 10):
                        canvas[x - 1][y - 1].drawSelf()
                        handled = True

def initialize():
    cols = ["red", "brown", "orange", "yellow", "green", "cyan", "blue", "purple", "pink", "black", "grey", "white"]
    for i in range(12):
        palette.append(PaletteBtn(i, cols[i]))
    for i in range(60):
        canvas.append([])
        for j in range(55):
            canvas[i].append(Pixel(i, j))

def MAIN():
    initialize()
    while (not close):
        mouseLoc = win.getMouse()
        handleClick(mouseLoc)

MAIN()