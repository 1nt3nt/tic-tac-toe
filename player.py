import pygame

class Player:
    def __init__(self, uid, name, factory=None, context=None):
        self.userId = uid
        self.factory = factory
        self.context = context
        self.pieces = []
        self.clicked = False
        self.control = False
        self.name = name

    #check if player successfully place piece
    #if success, store piece location
    def placedPiece(self, success):
        self.clicked = True
        self.myRound(False if success == True else True)
        #self.pieces.append()

    def get_UserId(self):
        return self.userId
    
    def get_name(self):
        return self.name

    # input bool 
    # set this player can place piece
    def myRound(self, control):
        self.control = control
    
    def isMyRound(self):
        return self.control
    
    def setWin(self):
        print( "player: ", self.name, " win")