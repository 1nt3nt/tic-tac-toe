import sys
import pygame
import views
import player

class Main():
    running = True
    screen = None
    view = None
    clock = None

    def __init__(self):
        pygame.init()
        size = width, height = 800, 600
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption("tic tac toe")
        self.view = views.StartView(self)
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[27] == 1:
                    self.running = False                
                self.view.on_event(event)
            self.view.run_ui()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Main().run()