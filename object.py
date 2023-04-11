import pygame
import player

clicked_obj = None
class Objects:
    def __init__(self,x,y):
        self.u = x
        self.v = y
        self.name = 'object'
    def draw(self, screen):
        pass
    def on_event(self,event):
        pass
    def get_name(self):
        return self.name

class Grid(Objects):
    def __init__(self, x, y, width, height, order):
        self.u = x
        self.v = y
        self.w = width
        self.h = height
        self.rect = None
        self.name = 'grid'
        self.status = False # indicate if it is placed by a piece
        self.clicked = False
        self.order = order

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.u,self.v, self.w, self.h), 2)

    # give grid click function
    # Click function can mark if a grid is available to place piece
    def on_event(self, event, surface, player):
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            pos = pygame.mouse.get_pos()
            if pygame.Rect.collidepoint(self.rect,pos[0],pos[1]) and self.status == False:
                self.status = True
                center = self.get_middle(pos)
                if player.get_UserId() == 1:
                    circle = Circle(center[0],center[1])
                    circle.draw(surface, min(self.w//2,self.h//2)-4)
                elif player.get_UserId() == 2:
                    cross = Cross((self.u,self.v), (self.u+self.w, self.v),
                                  (self.u+self.w, self.v+self.h),
                                  (self.u, self.v+self.h))
                    cross.draw(surface)
                player.placedPiece(True)
                #pygame.draw.circle(surface, (255,0,0), center, min(self.w//2,self.h//2)-4)
            elif pygame.Rect.collidepoint(self.rect,pos[0],pos[1]) and self.status == True:
                player.placedPiece(False)
                print('player: ',player.get_UserId())
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            

    # check if grid is available to place piece
    def get_status(self):
        return self.status

    def get_order(self):
        return self.order
    
    # return middle point of each grid
    def get_middle(self, pos):
        if (self.u <= pos[0] 
            and self.u+self.w >= pos[0] 
            and self.v <= pos[1] 
            and self.v+self.h >= pos[1] ):
            midpoint = (self.u+self.w//2, self.v+self.h//2)
            return midpoint

class Button(Objects):
    def __init__(self,x,y,img,scale):
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img,(int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.name = 'button'

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
    
    def on_event(self,event):
        action = False
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            if self.rect.collidepoint(pos):
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action  
    
class Piece(Grid):
    def __init__(self, x=0, y=0):
        self.name = 'piece'
        self.rect = None
        self.clicked = False
        self.u = x
        self.v = y

    def draw(self, surface):
        pass
    
class Circle(Piece):
    def __init__(self, x=0, y=0):
        super().__init__(x, y)
    def draw(self, surface, radius):
        pygame.draw.circle(surface, (255,0,0), (self.u,self.v), radius)

class Cross(Piece):
    def __init__(self, point1, point2, point3, point4):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.p4 = point4
    def draw(self, surface):
        pygame.draw.line(surface, (0,128,0), self.p1, self.p3, 5)
        pygame.draw.line(surface, (0,128,0), self.p2, self.p4, 5)

    