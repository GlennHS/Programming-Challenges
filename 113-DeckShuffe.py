from graphics import *
import random
import time

deck = []
win = GraphWin("ShuffleSim", 900, 540)

class Card:
    
    def __init__(self, xOrigin, yOrigin, value, suit):
        self.img = [Rectangle(Point(xOrigin, yOrigin), Point(xOrigin + 60, yOrigin + 90)), Text(Point(xOrigin + 30, yOrigin + 45), str(value) + str(suit))]
        self.suit = suit
        self.value = value
        self.xOrigin = xOrigin
        self.yOrigin = yOrigin
        
    def drawSelf(self):
        try:
            self.img[0].undraw()
            self.img[1].undraw()
        except:
            pass
        self.img = [Rectangle(Point(self.xOrigin, self.yOrigin), Point(self.xOrigin + 60, self.yOrigin + 90)), Text(Point(self.xOrigin + 30, self.yOrigin + 45), str(self.suit) + str(self.value))]
        if(self.suit == "C" or self.suit == "S"):
            self.img[1].setFill("black")
        elif(self.suit == "H" or self.suit == "D"):
            self.img[1].setFill("red")
        if(self.xOrigin <= 900 and self.yOrigin <= 540):
            self.img[0].draw(win)
            self.img[1].draw(win)

def initDeck():
    suits = ["S","H","D","C"]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    for value in range(len(values)):
        for suit in range(len(suits)):
            deck.append(Card(0, 0, values[value], suits[suit]))
    return deck
    
def randomize():
    for i in range(len(deck)):
        deck[i].xOrigin = random.randint(0, 900)
        deck[i].yOrigin = random.randint(0, 540)
        deck[i].drawSelf()

def display():
    card = 0
    for x in range(15):
        for y in range(6):
            if(card <= 51):
                deck[card].xOrigin = x * 60
                deck[card].yOrigin = y * 90
                card += 1
    for i in range(len(deck)):
        time.sleep(0.03)
        deck[i].drawSelf()
        
def MAIN():
    deck = initDeck()
    for i in range(3):
        randomize()
        time.sleep(1)
    display()
    
MAIN()