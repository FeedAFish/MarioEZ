import pygame
from pygame.locals import *
import pathimage
import ClassMain


class Monsters(ClassMain.Collidable):
    def __init__(self, pos, image, imaged):
        super().__init__()
        self.imaged = imaged
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.monalive = True
        self.speed = 4
        self.trajectcount = 0
        self.counter = 0

    def Show(self, window):
        if self.monalive:
            window.blit(self.image, self.rect)
        if self.counter:
            if self.counter == 1:
                self.monalive = False
                self.counter -= 1
            else:
                self.counter -= 1

    def Move(self, a, b):
        self.rect.move_ip(a, b)


class Mush(Monsters):
    def __init__(self, pos, image=pathimage.mushm, imaged=pathimage.mushd):
        super().__init__(pos, image, imaged)
        self.dx = -1
        self.dy = 0

    def Traject(self):
        if self.trajectcount < 1000:
            self.trajectcount += 1
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.trajectcount = 0
            self.dx = - self.dx

    def SelfKill(self):
        if not self.counter:
            self.counter = 100
        self.image = self.imaged
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
