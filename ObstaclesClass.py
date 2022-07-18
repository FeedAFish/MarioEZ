from re import A
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
                self.image, (self.rect.left + i *
                             self.rect.height, self.rect.top)
            )


class Land(Obstacles):
    def __init__(self, pos=(0, 378), image=pathimage.land):
        super().__init__(image, pos)


class Coinbox(Wall):
    def __init__(self, pos, number, image=pathimage.coinbox):
        super().__init__(pos, number, image)
        self.impactcount = 0
        self.coin = 1
        self.toggle = 1

    def On_collide(self, sprite):
        if not self.impactcount:
            self.impactcount = 14

    def BoxJump(self):
        if self.impactcount:
            self.impactcount -= 1
            if self.impactcount < 8:
                self.Move(0, 1)
            else:
                self.Move(0, -1)

    def Coinleave(self):
        self.coin = 0

    def ToggleFalse(self):
        self.toggle = False
