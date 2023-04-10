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
        # introduce two players
        self.player_1 = player.Player(0, surface=self.screen)
        self.player_2 = player.Player(1, surface=self.screen)

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.view.on_event(event)
                if event.type == pygame.QUIT:
                    self.running = False
            self.view.run_ui()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    Main().run()