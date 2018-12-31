from graphics import *
import random

win = GraphWin("Dragon Crystal Clone", 600, 600)
gridArr = []

class Character:
    
    def __init__(self, level, hp, res, dam):
        self.level = level
        self.hp = hp
        self.res = res
        self.dam = dam
        
    def atk(self):
        dice = self.dam.split("d")
        out = 0
        for i in range(dice[0]):
            out += random.randint(1, dice[1])
        return out

    def drawSelf():
        pass

class Tile:
    
    def __init__(self, blocking, contains):
        self.blocking = blocking
        self.contains = contains
        self.img = ""
        self.visible = False
        
    def drawSelf(self, x, y):
        if(x > 5 or y > 5 or x < 0 or y < 0):
            if(self.visible):
                self.img.undraw(win)
                self.img = ""
                self.visible = False
        else:
            self.img = Rectangle(Point(x * 100, y * 100), Point(x * 100 + 100, y * 100 + 100))
            self.img.draw(win)
            self.visible = True

def drawBoard():
    for i in range(len(gridArr)):
        for j in range(len(gridArr[i])):
            gridArr[i][j].drawSelf(i, j)
            
def genBoard():
    for i in range(10):
        gridArr.append([])
        for j in range(10):
            gridArr[i].append(Tile(True, ""))
            
def MAIN():
    genBoard()
    drawBoard()

MAIN()