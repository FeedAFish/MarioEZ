from turtle import Turtle
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

    def On_collide(self, sprite):
        a = pygame.Rect(
            (self.rect[0], self.rect[1] -
             self.dy), (self.rect[2], self.rect[3])
        )
        if a.colliderect(sprite):
            if self.dx < 0:
                self.rect.left = sprite.rect.right
            else:
                self.rect.right = sprite.rect.left
            self.dx = - self.dx
        else:
            if self.dy < 0:
                self.rect.top = sprite.rect.bottom
            else:
                self.rect.bottom = sprite.rect.top

    def MonaliveFalse(self):
        self.monalive = False


class Mush(Monsters):
    def __init__(self, pos, image=pathimage.mushm, imaged=pathimage.mushd):
        super().__init__(pos, image, imaged)
        self.dx = -1
        self.dy = 12

    def Traject(self):
        if self.trajectcount < 600:
            self.trajectcount += 1
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.trajectcount = 0
            self.dx = - self.dx

    def Pl_Collide(self, sprite):
        self.SelfKill()

    def SelfKill(self):
        if not self.counter:
            self.counter = 100
        self.image = self.imaged
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)


class TurtleMons(Monsters):
    def __init__(self, pos, image, imaged):
        super().__init__(pos, image, imaged)
        self.mode = True

    def Pl_Collide(self, sprite):
        if self.mode:
            self.image = self.imaged
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
            self.mode = False
            self.dx = 0
            self.dy = 3
        else:
            if not self.dx:
                if self.rect.left > sprite.rect.left:
                    self.dx = 4
                else:
                    self.dx = -4
            else:
                self.dx = 0

    def Traject(self):
        if self.mode:
            self.RunTraject()
        else:
            self.Move(self.dx, self.dy)

    def RunTraject(self):
        pass


class TurtleLand(TurtleMons):
    def __init__(self, pos, image=pathimage.landturtlered, imaged=pathimage.turtleshell):
        super().__init__(pos, image, imaged)
        self.dx = -1
        self.dy = 3

    def RunTraject(self):
        if self.trajectcount < 600:
            self.trajectcount += 1
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.trajectcount = 0
            self.dx = - self.dx


class TurtleFly(TurtleMons):
    def __init__(self, pos, image=pathimage.landturtlered, imaged=pathimage.turtleshell):
        super().__init__(pos, image, imaged)
        self.dx = -1
        self.dy = -3

    def RunTraject(self):
        if self.trajectcount < 1200:
            self.trajectcount += 1
            if self.trajectcount % 100 == 0:
                self.dy = -self.dy
            if self.trajectcount == 600:
                self.dx = -self.dx
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.trajectcount = 0
            self.dx = - self.dx
