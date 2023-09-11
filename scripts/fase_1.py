import pygame
from pygame.locals import *
from scripts.plane import Plane
from scripts.frog import Frog

class Fase_1:
    def __init__(self, fps, screen, screen_rect, resolution):
        self.fps = fps
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.screen_rect = screen_rect
        self.resolution = resolution

    def fase_1(self):
        # objects instances
        plane = Plane(self.screen, self.screen_rect, self.resolution)
        frog = Frog(self.screen_rect, self.resolution)

        #  load sprites
        load_sprites = pygame.sprite.Group()
        load_sprites.add(plane)
        load_sprites.add(frog)

        background = pygame.transform.scale(
            pygame.image.load('assets/background/background_nuvens.jpg').convert(),
            self.resolution
        )

        while True:
            # set frames
            self.clock.tick(self.fps)

            # draw background
            self.screen.blit(background, (0, 0))

            # events
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        plane.attack()

            key = pygame.key.get_pressed()

            # sprites update
            load_sprites.draw(self.screen)
            load_sprites.update(key)

            pygame.display.flip()