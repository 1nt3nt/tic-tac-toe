import pygame

class Player:
    def __init__(self, uid, factory=None, surface=None):
        self.userId = uid
        self.factory = factory
        self.screen = surface

    def placePiece(self, event):
        self.factory
        piece = self.factory.make_obj('piece')
        if (piece.get_object(event)):
            piece.draw(self.screen, self.userId)
            return True
        return False
