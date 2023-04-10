import piece

class Player:
    def __init__(self, uid, piece):
        self.userId = uid
        self.piece = piece
    def placePiece(self, piece):
        pieces = piece()
