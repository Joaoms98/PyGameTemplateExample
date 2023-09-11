import pygame
from pygame.locals import *


class Projectil(pygame.sprite.Sprite): 
    def __init__(self, screen, projectil_position_x, projectil_position_y):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen

        # load sprite
        self.sprite = pygame.image.load('assets/sprites/plane.png')
        self.image = pygame.transform.scale(self.sprite, (10, 7))


        self.current_position = {'x': projectil_position_x - 50, 'y': projectil_position_y}
        self.rect = self.image.get_rect()
        self.rect.center = (self.current_position['x'], self.current_position['y'])
        self.velocity = 4

    def update(self):
        self.current_position['x'] -= self.velocity
        self.rect.center = (self.current_position['x'], self.current_position['y'])
        