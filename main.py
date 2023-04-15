import sys
import pygame
import views

class Main():
    running = True
    screen = None
    view = None
    clock = None

    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        size = width, height = 800, 600
        bg = pygame.image.load('./img/background.png')
        self.screen = pygame.display.set_mode(size)
        self.screen.blit(bg,(0,0))
        pygame.display.set_caption("tic tac toe")
        mixer = pygame.mixer.Sound('./music/03 - P.T. Adamczyk - The Rebel Path.mp3')
        mixer.play(-1)
        mixer.set_volume(0.7)
        self.view = views.StartView(self)
        self.clock = pygame.time.Clock()

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