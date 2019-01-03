from graphics import *
import random
from time import sleep

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

    def move(self, x, y):
        self.x += x
        self.y += y

    def drawSelf(self, colour = "green"):
        if(checkVis(self.x, self.y)):
            self.img = [Polygon(Point(self.x * 100 + 50, self.y * 100 + 20), Point(self.x * 100 + 20, self.y * 100 + 80), Point(self.x * 100 + 80, self.y * 100 + 80))]
            self.img.append(Text(Point(self.x * 100 + 50, self.y * 100 + 50), self.hp))
            self.img[0].setFill(colour)
            for img in (self.img):
                img.draw(win)
        elif(not(self.img == "")):
            self.img.undraw(win)
            self.img = ""

class Enemy(Character):

    def __init__(self, level, hp, res, dam, name, x, y):
        super().__init__(level, hp, res, dam, name, x, y)

    # @OVERRIDE
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

    def drawSelf(self):
        if(checkVis(self.x, self.y)):
            self.img = [Polygon(Point(self.x * 100 + 50, self.y * 100 + 80), Point(self.x * 100 + 20, self.y * 100 + 20), Point(self.x * 100 + 80, self.y * 100 + 20))]
            self.img.append(Text(Point(self.x * 100 + 50, self.y * 100 + 50), self.hp))
            self.img[0].setFill("red")
            for img in (self.img):
                img.draw(win)
        elif(not(self.img == "")):
            self.img.undraw(win)
            self.img = ""

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
            if(not(self.img == "")):
                self.img.undraw(win)
            self.img = ""
        else:
            self.img = Rectangle(Point(x * 100, y * 100), Point(x * 100 + 100, y * 100 + 100))
            if(self.contains == ""):
                if(self.blocking):
                    self.img.setFill("black")
                else:
                    self.img.setFill("grey")
            else:
                # TODO: issubclass check fails here so temporary try/except in place
                try:
                    self.contains.drawSelf()
                except:
                    pass
            self.img.draw(win)

class UI:

    def __init__(self):
        self.colour = "black"

    def drawSelf(self):
        

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

def updateTileContains():
    for i in range(len(tileArr)):
        for j in range(len(tileArr[i])):
            tileArr[i][j].contains = ""
    for ent in (entityArr):
        tileArr[ent.x][ent.y].contains = ent

def drawBoard():
    updateTileContains()
    for i in range(len(tileArr)):
        for j in range(len(tileArr[i])):
            tileArr[i][j].drawSelf(i, j)
            
def genBoard():
    for i in range(10):
        tileArr.append([])
        for j in range(10):
            tileArr[i].append(Tile(False, ""))
    for i in range(10):
        tileArr[i][0].blocking = True
        tileArr[i][9].blocking = True
        tileArr[0][i].blocking = True
        tileArr[9][i].blocking = True
    entityArr.append(player)
    entityArr.append(Enemy(5, 100, 4, "4d4", "BOB", 1, 2))
    updateTileContains()


win = GraphWin("Dragon Crystal Clone", 600, 600)
tileArr = []
entityArr = []
player = Character(5, 50, 2, "2d4", "PLAYER", 1, 1)

def MAIN():
    genBoard()
    drawBoard()
    sleep(3)

MAIN()