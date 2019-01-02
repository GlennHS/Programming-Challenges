from graphics import *
import random
from time import sleep

win = GraphWin("Dragon Crystal Clone", 600, 600)
gridArr = []

class Character:
    
    def __init__(self, level, hp, res, dam, name, x, y):
        self.level = level
        self.hp = hp
        self.res = res
        self.dam = dam
        self.name = name
        self.x = x
        self.y = y
        self.img = ""

    def atk(self):
        dice = self.dam.split("d")
        out = 0
        for i in range(dice[0]):
            out += random.randint(1, dice[1])
        return out

    def drawSelf():
        if(checkVis(self.x, self.y)):
            if(self.name == "PLAYER"):
                self.img = Polygon(Point(self.x * 100 + 50, self.y * 100 + 20), Point(self.x * 100 + 20, self.y * 100 + 80), Point(self.x * 100 + 80, self.y * 100 + 80))
                self.img.setFill("green")
            else:
                self.img = Polygon(Point(self.x * 100 + 50, self.y * 100 + 80), Point(self.x * 100 + 20, self.y * 100 + 20), Point(self.x * 100 + 80, self.y * 100 + 20))
                self.img.setFill("red")
        else:
            self.img = ""
        if(not(self.img == "")):
            self.img.draw(win)

class Enemy(Character):

    def __init__(self, level, hp, res, dam, name, x, y):
        super().__init__(level, hp, res, dam, name, x, y)

    def move(self, steps):
        numMoves = steps
        for i in range(steps):
            if(checkVis(self.x, self.y)):
                while(numMoves > 0):
                    if(player.x < self.x):
                        self.x += 1
                        numMoves -= 1
                    if(player.x > self.x and numMoves > 0):
                        self.x -= 1
                        numMoves -= 1
                    if(player.y < self.y and numMoves > 0):
                        self.y += 1
                        numMoves -= 1
                    if(player.y > self.y and numMoves > 0):
                        self.y -= 1
                        numMoves -= 1
            else:
                for i in range(numMoves):
                    rand = random.random()
                    if(rand < 0.25):
                        x -= 1
                    elif(rand < 0.5):
                        x += 1
                    elif(rand < 0.75):
                        y += 1
                    else:
                        y -= 1

class Item():

    def __init__(self, category, colour):
        self.category = category
        self.colour = colour

class Tile:
    
    def __init__(self, blocking, contains):
        self.blocking = blocking
        self.contains = contains
        self.img = ""
        
    def drawSelf(self, x, y):
        if(not(checkVis(x, y))):
            try:
                self.img.undraw(win)
            except:
                pass
            self.img = ""
        else:
            self.img = Rectangle(Point(x * 100, y * 100), Point(x * 100 + 100, y * 100 + 100))
            if(self.contains == ""):
                if(self.blocking):
                    self.img.setFill("black")
                else:
                    self.img.setFill("grey")
            self.img.draw(win)

def combat(enemy):
    pDam = player.atk()
    enemy.hp -= pDam - enemy.res
    eDam = enemy.atk()
    player.hp -= eDam - player.res
    print("PLAYER dealt ", pDam, " damage")
    print(enemy.name, " dealt ", eDam, " damage")

def checkVis(x, y):
    if(x > 5 or y > 5 or x < 0 or y < 0):
        return False
    else:
        return True

def drawBoard():
    for i in range(len(gridArr)):
        for j in range(len(gridArr[i])):
            gridArr[i][j].drawSelf(i, j)
            
def genBoard():
    for i in range(10):
        gridArr.append([])
        for j in range(10):
            gridArr[i].append(Tile(False, ""))
    for i in range(10):
        gridArr[i][0].blocking = True
        gridArr[i][9].blocking = True
        gridArr[0][i].blocking = True
        gridArr[9][i].blocking = True
    gridArr[1][1].contains = player
    gridArr[1][2].contains = Enemy(5, 100, 4, "4d4", "BOB", 1, 2)
            
def MAIN():
    genBoard()
    drawBoard()
    sleep(3)

player = Character(5, 50, 2, "2d4", "PLAYER", 1, 1)

MAIN()