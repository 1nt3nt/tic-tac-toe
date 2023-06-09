import pygame
import factory
import player

factory = factory.Factory()


class Views:
    screen = None
    def __init__(self, context):
        self.screen = context

    def run_ui(self):
        pass

    def on_event(self, event):
        pass

# This is a main view for this game. Also known as game interface
class GameView(Views):
    '''
     game interface
    '''
    # parameter:
    # left top point and right point point, 
    # left bottom point and right bottom point
    def __init__(self, l_t_p, r_t_p, l_b_p, r_b_p, context):
        self.p1 = l_t_p
        self.p2 = r_t_p
        self.p3 = l_b_p
        self.p4 = r_b_p
        self.clicked = False
        self.round = 1

        # col
        self.col1 = (self.p2[0] - self.p1[0]) // 3
        self.col2 = 2 * self.col1
        # row
        self.row1 = (self.p4[1] - self.p1[1]) // 3
        self.row2 = 2 * self.row1
        self.vertices = [self.p1, (self.p1[0]+self.col1, self.p1[1]), (self.p1[0]+self.col2, self.p1[1]),
                    (self.p1[0],self.p1[1]+self.row1), (self.p1[0]+self.col1,self.p1[1]+self.row1), (self.p1[0]+self.col2,self.p1[1]+self.row1),
                    (self.p1[0],self.p1[1]+self.row2), (self.p1[0]+self.col1,self.p1[1]+self.row2), (self.p1[0]+self.col2,self.p1[1]+self.row2)]
        factory.setVertices(self.vertices)
        self.grids = factory.make_obj('grid',w=self.col1,h=self.row1)
        self.context = context
        Views.__init__(self, context.screen)
        self.context.screen = pygame.display.set_mode((800, 600))

        #loading players
        self.player1 = player.Player(1,'player1',factory,self.context)
        self.player2 = player.Player(-1,'player2',factory,self.context)
        #player 1 place first
        self.player1.myRound(True)
        self.controller = self.player1.get_UserId()

        #initialize recorder
        self.recorder = [[0,0,0],[0,0,0],[0,0]]

    def run_ui(self):
        pygame.draw.aalines(self.context.screen, (255,255,255), True, [self.p1, self.p2, self.p3, self.p4])      
        # col
        pygame.draw.aaline(self.context.screen, (255,255,255), (self.col1 + self.p1[0] , self.p1[1]), (self.col1 + self.p1[0], self.p4[1]))
        pygame.draw.aaline(self.context.screen, (255,255,255), (self.col2 + self.p1[0], self.p2[1]), (self.col2 + self.p1[0], self.p3[1]))

        #row
        pygame.draw.aaline(self.context.screen, (255,255,255), (self.p1[0], self.row1 + self.p1[1]), (self.p2[0], self.row1 + self.p1[1]))
        pygame.draw.aaline(self.context.screen, (255,255,255), (self.p1[0], self.row2 + self.p1[1]), (self.p2[0],self.row2 + self.p1[1]))
        for grid in self.grids:
            grid.draw(self.context.screen)
        
    def on_event(self, event):
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if pygame.key.get_pressed()[pygame.K_ESCAPE] == 1:
                self.context.running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.controller == 1:             
                self.update_view(event, self.player1)
            elif self.controller == 2:
                self.update_view(event, self.player2)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.controller == 1:
                if self.player1.isMyRound() == False:
                    self.controller = 2
                    print('round: ', self.round)
                    self.round += 1
                    print('switch to player2')
                self.update_view(event, self.player1)
            elif self.controller == 2:
                if self.player2.isMyRound() == False:
                    self.controller = 1
                    print('switch to player1')
                self.update_view(event, self.player2)

    # update screen each time when player place piece / click mouse
    def update_view(self, event, player):
        self.grids[0].on_event(event,self.context.screen, player, self.recorder)
        self.grids[1].on_event(event,self.context.screen, player, self.recorder)
        self.grids[2].on_event(event,self.context.screen, player, self.recorder)
        self.grids[3].on_event(event,self.context.screen, player, self.recorder)
        self.grids[4].on_event(event,self.context.screen, player, self.recorder)
        self.grids[5].on_event(event,self.context.screen, player, self.recorder)
        self.grids[6].on_event(event,self.context.screen, player, self.recorder)
        self.grids[7].on_event(event,self.context.screen, player, self.recorder)
        self.grids[8].on_event(event,self.context.screen, player, self.recorder)

        #check win:
        if self.checkWin(self.recorder, player):
            self.context.view= ResultView(self.context, True, player.get_name())
        if self.round == 6:
            print("game is a draw")
            self.context.view = ResultView(self.context,False)

    # find who is win or game is tie based on recorder
    def checkWin(self, recorder, player):
        for i in recorder:
            for val in i:
                #print(val)
                if val == 3 or val == -3:
                    player.setWin()
                    return True
        return False
        
# When game over, this view will appear
class ResultView(Views):
    '''
    When game over, this view will appear
    '''
    def __init__(self, context, result, winner=''):
        self.res = result
        self.context = context
        self.winner = winner  
     
        self.start_img = pygame.image.load('./img/start_btn.png').convert_alpha()
        self.quit_img = pygame.image.load('./img/exit_btn.png').convert_alpha()
        self.bg = pygame.image.load('./img/background.png')
        pygame.mouse.set_pos(400, 300)

        factory.setLocation(100, 450)
        self.start_button = factory.make_obj('button', self.start_img)
        factory.setLocation(450, 450)
        self.quit_button = factory.make_obj('button', self.quit_img)
        Views.__init__(self, context.screen)
        self.context.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font('freesansbold.ttf', 32)

    def run_ui(self):
        self.context.screen.blit(self.bg,(0,0))
        self.start_button.draw(self.context.screen)
        self.quit_button.draw(self.context.screen)
        if self.res == True:
            text = self.font.render(self.winner + ' WIN!', True, (0,0,128),(255,255,255))
        else:
            text = self.font.render('A Draw', True, (0,0,128),(255,255,255))
        textRect = text.get_rect()
        textRect.center = (400, 300)
        self.context.screen.blit(text,textRect)

    def on_event(self, event):
        if self.start_button.on_event(event) == True:
            self.start_game()
        if self.quit_button.on_event(event) == True:
            self.exit_game()

    def exit_game(self):
        self.context.running = False
    
    def start_game(self):
        self.context.view = GameView((62, 70), (746, 70), (746, 580), (62, 580), self.context)
        pygame.mouse.set_pos(342, 35)


class StartView(Views):
    """ 
    THIS IS START MENU
    """
    def __init__(self, context):
        #loading images
        self.start_img = pygame.image.load('./img/start_btn.png').convert_alpha()
        self.quit_img = pygame.image.load('./img/exit_btn.png').convert_alpha()

        # modify factory
        factory.setLocation(100, 200)
        self.start_button = factory.make_obj('button', self.start_img)
        #object.Button(100, 200, self.start_img, 0.7)
        factory.setLocation(440, 200)
        self.quit_button = factory.make_obj('button', self.quit_img)
        self.context = context  
        self.clicked = False
        Views.__init__(self, context.screen)

    def run_ui(self):
        self.start_button.draw(self.context.screen)
        self.quit_button.draw(self.context.screen)
    
    def on_event(self, event):
        if self.start_button.on_event(event) == True:
            self.start_game()
        if self.quit_button.on_event(event) == True:
            self.exit_game()

    def exit_game(self):
        self.context.running = False
    
    def start_game(self):
        self.context.view = GameView((62, 70), (746, 70), (746, 580), (62, 580), self.context)
        pygame.mouse.set_pos(342, 35)
        