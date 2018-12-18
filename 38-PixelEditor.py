from graphics import *

win = GraphWin("Pixel Editor", 600, 600)
palette = []

class Pixel:
    
    def __init__(self, xPos, yPos, colour):
        self.xPos = xPos
        self.yPos = yPos
        self.colour = colour
        self.img = Rectangle(Point(10 * xPos, 10 * yPos), Point(10 * xPos + 10, 10 * yPos + 10))
        self.drawSelf()
        
    def deleteSelf(self):
        self.colour = "white"
        self.drawSelf()
        
    def drawSelf(self):
        self.img.setFill(self.colour)
        try:
            self.img.undraw()
        except:
            pass
        self.img.draw(win)
        
class PaletteBtn:
    
    def __init__(self, xPos, yPos, colour):
        self.xPos = xPos
        self.yPos = yPos
        self.img = Rectangle(Point(10 * xPos, 10 * yPos), Point(10 * xPos + 10, 10 * yPos + 10))
        self.img.setFill(colour)
        self.img.draw(win)
        
def initialize():
    cols = ["red", "blue", "black", "white", "yellow", "green", "pink", "purple", "green", "grey"]
    for i in range(10):
        palette.append(PaletteBtn(i * 10 + 250, 500, cols[i]))