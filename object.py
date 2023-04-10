import pygame

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
    def __init__(self, x, y, width, height):
        self.u = x
        self.v = y
        self.w = width
        self.h = height
        self.rect = None
        self.name = 'grid'
        self.status = False # indicate if it is placed by a piece
        self.clicked = False

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.u,self.v, self.w, self.h), 2)

    def on_event(self, event,surface):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            if pygame.Rect.collidepoint(self.rect,pos[0],pos[1]) and self.status == False:
                self.status = True
                center = self.get_middle(pos)
                pygame.draw.circle(surface, (255,0,0), center, min(self.w//2,self.h//2)-4)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
    
    def get_status(self):
        return self.status
    
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

    def draw(self, surface, uid):
        if uid == 0:
            pygame.draw.aaline(surface, (255,0,0), (20, 20), (40,40))
            pygame.draw.aaline(surface, (255,0,0), (40,20),(20,40))

        if uid == 1:
            pygame.draw.circle(surface, (255,255,255), (self.u,self.v), 35)
    
    # return the status that if piece is placed.
    def on_event(self, event, surface):
        return super().get_object(event, surface)