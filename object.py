import pygame

class Objects:
    def __init__(self,x,y):
        self.u = x
        self.v = y
    def draw(self):
        pass
    def get_object(self,event):
        pass
        

class Grid(Objects):
    def __init__(self, x, y, width, height):
        self.u = x
        self.v = y
        self.w = width
        self.h = height
        self.rect = None
        self.name = 'grid'
        self.clicked = False

    def draw(self, screen):
        self.rect = pygame.draw.rect(screen, (255,255,255), pygame.Rect(self.u,self.v, self.w, self.h), 2)

    def get_object(self, event):
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            if pygame.Rect.collidepoint(self.rect,pos[0],pos[1]):
                print(self.name)
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

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
    

class Piece(Objects):
    def __init__(self, x, y):
        self.name = 'piece'

    def draw(self, surface, uid):
        if uid == 0:
            pygame.draw.aaline(surface, (255,0,0), (20, 20), (40,40))
            pygame.draw.aaline(surface, (255,0,0), (40,20),(20,40))

        if uid == 1:
            pygame.draw.circle(surface, (255,255,255), (self.u,self.v), 35)