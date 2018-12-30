from graphics import *

win = GraphWin("Chess", 400, 400)
board = []
player = "w"
gameOver = False

class Piece:
    
    def __init__(self, x, y, colour, type):
        self.x = x
        self.y = y
        self.type = type
        self.colour = colour
        self.isAlive = True
        self.img = Text(Point(self.x * 50 + 25, self.y * 50 + 25), type)
        self.drawSelf()
            
    def drawSelf(self):
        if(self.isAlive):
            self.img.undraw()
            self.img = Text(Point(self.x * 50 + 25, self.y * 50 + 25), self.type)
            self.img.setSize(24)
            self.img.draw(win)
            if(self.colour == "w"):
                self.img.setFill("white")
            else:
                self.img.setFill("black")
                
    def setDead(self):
        self.img.undraw()
        self.isAlive = False
            
class Rook(Piece):
    
    def __init__(self, x, y, colour):
        super().__init__(x, y, colour, "r")
        
    def checkValid(self, newX, newY):
        # Check moving in a cardinal direction
        if(not((self.x == newX) ^ (self.y == newY))):
            return False
        # Check not jumping over things
        else:
            if(self.y == newY):
                for i in range(min(self.x, newX) + 1, max(self.x, newX), 1):
                    if(not (board[i][self.y] == "empty")):
                        return False
            else:
                print("MOVING ON Y AXIS")
                for i in range(min(self.y, newY) + 1, max(self.y, newY), 1):
                    if(not (board[self.x][i] == "empty")):
                        return False
        # Check target square not got a same colour piece in it, also handle capture
        if(type(board[newX][newY]) == Piece):
            if(board[newX][newY].colour == self.colour):
                return False
            else:
                return True
        return True
        
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

def mousePos(clickLoc):
    for i in range(8):
        for j in range(8):
            if(clickLoc.getX() < i * 50 + 50 and clickLoc.getY() < j * 50 + 50):
                return [i, j]

def boardInit():
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append("empty")
    # Rooks
    board[0][0] = Rook(0, 0, "b")
    board[7][0] = Rook(7, 0, "b")
    board[0][7] = Rook(0, 7, "w")
    board[7][7] = Rook(7, 7, "w")
    # Knights
    board[1][0] = Piece(1, 0, "b", "n")
    board[6][0] = Piece(6, 0, "b", "n")
    board[1][7] = Piece(1, 7, "w", "n")
    board[6][7] = Piece(6, 7, "w", "n")
    # Bishops
    board[2][0] = Piece(2, 0, "b", "b")
    board[5][0] = Piece(5, 0, "b", "b")
    board[2][7] = Piece(2, 7, "w", "b")
    board[5][7] = Piece(5, 7, "w", "b")
    # Queens
    board[3][0] = Piece(3, 0, "b", "q")
    board[4][7] = Piece(4, 7, "w", "q")
    # Kings
    board[4][0] = Piece(4, 0, "b", "k")
    board[3][7] = Piece(3, 7, "w", "k")
    # Pawns
    # for i in range(8):
    #     board[i][1] = Piece(i, 1, "b", "p")
    #     board[i][6] = Piece(i, 6, "w", "p")

def movePiece(x, y, newX, newY):
    print(type(board[newX][newY]))
    moving = board[x][y]
    if(type(board[newX][newY] == Piece)):
        board[newX][newY].setDead()
    board[x][y] = "empty"
    board[newX][newY] = moving
    board[newX][newY].x = newX
    board[newX][newY].y = newY
    board[newX][newY].drawSelf()

def MAIN():
    genBackground()            
    boardInit()
    while(not gameOver):
        chosenPiece = "empty"
        while(chosenPiece == "empty"):
            loc = win.getMouse()
            cleanLoc = mousePos(loc)
            chosenPiece = board[cleanLoc[0]][cleanLoc[1]]
        chosenPiece.img.setFill("yellow")
        moveLoc = win.getMouse()
        cleanMoveLoc = mousePos(moveLoc)
        chosenPiece.drawSelf()
        isValid = chosenPiece.checkValid(cleanMoveLoc[0], cleanMoveLoc[1])
        if(isValid):
            movePiece(cleanLoc[0], cleanLoc[1], cleanMoveLoc[0], cleanMoveLoc[1])
MAIN()