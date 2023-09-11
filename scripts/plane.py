import pygame
from pygame.locals import *
from scripts.projectil import Projectil

class Plane(pygame.sprite.Sprite):
    def __init__(self, screen, screen_rect, resolution):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen_rect
        self.resolution = resolution

        # load sprite
        self.sprite = pygame.image.load('assets/sprites/plane.png')
        self.image = pygame.transform.scale(self.sprite, (100, 64))

        self.current_position = {'x': self.screen_rect.right - 50, 'y': self.screen_rect.centery}
        self.rect = self.image.get_rect()
        self.rect.center = (self.current_position['x'], self.current_position['y'])
        self.velocity = 2
        
        self.projects = pygame.sprite.Group()

    # method to control sprite behavior
    def update(self, key):
        if key:
            self.movement(key)

        self.projects.draw(self.screen)
        self.projects.update()

    def attack(self):
        project = Projectil(self.screen, self.current_position['x'], self.current_position['y'])
        self.projects.add(project)

    def movement(self, key):
        if key[pygame.K_LEFT] and self.rect.left > 0:
            self.current_position['x'] -= self.velocity

        if key[pygame.K_RIGHT] and self.rect.right < self.resolution[0]:
            self.current_position['x'] += self.velocity

        if key[pygame.K_UP] and self.rect.top > 0:
            self.current_position['y'] -= self.velocity

        if key[pygame.K_DOWN] and self.rect.bottom < self.resolution[1]:
            self.current_position['y'] += self.velocity

        self.rect.center = self.current_position['x'], self.current_position['y']

