#pygame.draw.rect(self.context.screen, (255,255,255), pygame.Rect(self.p1[0],self.p1[1], col1, row1), 2)

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
                for vertex in self.vertices:
                    grids.append(object.Grid(vertex[0],vertex[1],w,h))
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