import pygame

class Player:
    def __init__(self, uid, factory=None, context=None):
        self.userId = uid
        self.factory = factory
        self.context = context
        self.pieces = []

    def placedPiece(self, obj):
        self.pieces.append(obj.get_order())

    def get_UserId(self):
        return self.userId
    
    def check_win(self):
        pass
    

