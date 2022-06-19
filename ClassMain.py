import pygame
from pygame.locals import *


class Collidable(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.collision_groups = []
        self.dx = 0
        self.dy = 0


class Spike(Collidable):
    def __init__(self):
        super().__init__()
