from graphics import *

win = GraphWin("Chess", 400, 400)
board = []

class Piece:
    
    def __init__(self, x, y, colour, type):
        self.x = x
        self.y = y
        self.type = type
        self.colour = colour
        self.isAlive = True
        self.img = [Rectangle(Point(self.x * 50, self.y * 50), Point(self.x * 50 + 50, self.y * 50 + 50)), Text(Point(self.x * 50 + 25, self.y * 50 + 25), type)]
        for i in range(len(self.img)):
            self.img[i].draw(win)
        self.img[1].setSize(24)
        self.drawSelf()
            
    def drawSelf(self):
        if(self.isAlive):
            for i in range(len(self.img)):
                self.img[i].undraw()
                self.img[i].draw(win)
            if(self.colour == "w"):
                self.img[1].setFill("white")
            else:
                self.img[1].setFill("black")
                
    def setDead(self):
        self.isAlive = False
        for i in range(len(self.img)):
            self.img[i].undraw()
            
def genBackground():
    for i in range(8):
        for j in range(8):
            if((i + j) % 2 == 0):
                col = "grey"
            else:
                col = "red"
            sqr = Rectangle(Point(i * 50, j * 50), Point(i * 50 + 50, j * 50 + 50))
            sqr.setFill(col)
            sqr.draw(win)

def boardInit():
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("empty")
    # Rooks
    board[0][0] = Piece(0, 0, "b", "r")
    board[7][0] = Piece(7, 0, "b", "r")
    board[0][7] = Piece(0, 7, "w", "r")
    board[7][7] = Piece(7, 7, "w", "r")
    # Knights
    board[0][0] = Piece(1, 0, "b", "n")
    board[7][0] = Piece(6, 0, "b", "n")
    board[0][7] = Piece(1, 7, "w", "n")
    board[7][7] = Piece(6, 7, "w", "n")
    # Bishops
    board[0][0] = Piece(2, 0, "b", "b")
    board[7][0] = Piece(5, 0, "b", "b")
    board[0][7] = Piece(2, 7, "w", "b")
    board[7][7] = Piece(5, 7, "w", "b")
    # Queens
    board[0][0] = Piece(3, 0, "b", "q")
    board[7][0] = Piece(4, 7, "w", "q")
    # Kings
    board[0][7] = Piece(4, 0, "b", "k")
    board[7][7] = Piece(3, 7, "w", "k")

genBackground()            
boardInit()