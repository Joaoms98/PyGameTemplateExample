import pygame
from pygame.locals import *


class Frog(pygame.sprite.Sprite):
    def __init__(self, screen_rect, resolution):
        pygame.sprite.Sprite.__init__(self)
        self.screen_rect = screen_rect
        self.resolution = resolution

        # load sprites
        self.sprites = [pygame.image.load('assets/sprites/attack_1.png'),
                        pygame.image.load('assets/sprites/attack_2.png'),
                        pygame.image.load('assets/sprites/attack_3.png'),
                        pygame.image.load('assets/sprites/attack_4.png'),
                        pygame.image.load('assets/sprites/attack_5.png'),
                        pygame.image.load('assets/sprites/attack_6.png'),
                        pygame.image.load('assets/sprites/attack_7.png'),
                        pygame.image.load('assets/sprites/attack_8.png'),
                        pygame.image.load('assets/sprites/attack_9.png'),
                        pygame.image.load('assets/sprites/attack_10.png')]
        self.image = pygame.transform.scale(self.sprites[0], (128 * 3, 64 * 3))
        self.current_sprite = 0

        self.current_position = {'x': 240, 'y': 100}
        self.rect = self.image.get_rect()
        self.rect.center = (self.current_position['x'], self.current_position['y'])
        self.velocity = 30

    def update(self, key):
        self.current_sprite = self.current_sprite + 0.2
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
            self.atack_animation = False

        # set sprite time and scale
        self.image = self.sprites[int(self.current_sprite)]
        self.image = pygame.transform.scale(self.image, (128 * 3, 64 * 3))