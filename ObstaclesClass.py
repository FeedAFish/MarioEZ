import pygame
from pygame.locals import *
import pathimage
import ClassMain


class Obstacles(ClassMain.Collidable):
    def __init__(self, image, pos):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def Show(self, window):
        window.blit(self.image, self.rect)

    def Move(self, a, b):
        self.rect.move_ip(a, b)


class Pipe(Obstacles):
    def __init__(self, pos, image=pathimage.barrel):
        super().__init__(image, pos)


class Wall(Obstacles):
    def __init__(self, pos, number, image=pathimage.wall):
        super().__init__(image, pos)
        self.number = number
        self.rect.width = self.rect.width * self.number

    def Show(self, window):
        for i in range(self.number):
            window.blit(
                self.image, (self.rect.left + i * self.rect.height, self.rect.top)
            )


class Land(Obstacles):
    def __init__(self, pos=(0, 705), image=pathimage.land):
        super().__init__(image, pos)
