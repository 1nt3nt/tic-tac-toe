import object

class Factory:
    def __init__(self, vertices=[], x=0, y=0):
        self.vertices = vertices
        self.x = x
        self.y = y

    def make_obj(self, obj_name, img = None, w=0, h=0):
        match obj_name:
            case 'button':
                return object.Button(self.x, self.y, img, 0.7)
            case 'piece':
                return object.Piece(self.x, self.y)
            case 'grid':
                grids = []
                row = 0
                col = 0
                for vertex in self.vertices:
                    if col == 3:
                        col = 0
                    if row == 3:
                        row = 0
                    grids.append(object.Grid(vertex[0],vertex[1],w,h, (row, col)))
                    col+= 1
                    row += col // 3
                return grids
            case _:
                return "Unable to make " + obj_name
        
    def setLocation(self,x,y):
        self.x = x
        self.y = y
    
    def setVertices(self, vertices):
        self.vertices = vertices

    def get_objs(self):
        pass