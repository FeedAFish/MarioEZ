import pygame
from pygame.locals import *
import pathimage
import ClassMain


jumptime = 100
falltime = 130


class Player(ClassMain.Collidable):
    def __init__(
        self,
        pos,
        imager=pathimage.imager,
        imagel=pathimage.imagel,
        imagejr=pathimage.imagejr,
        imagejl=pathimage.imagejl,
    ):
        super().__init__()

        self.imager = imager
        self.imagel = imagel
        self.imagejl = imagejl
        self.imagejr = imagejr

        self.rect = self.imager.get_rect(topleft=pos)

        # Variable
        self.onair = True
        self.fall = True
        self.right = True
        self.moveable = True
        # Counter Jump On Air
        self.counter = 0
        # Level
        self.level = 0
        # Invisible
        self.invisible = False
        self.invisibleTimer = 0

    def Show(self, window):
        if self.right:
            if self.onair and not self.fall:
                window.blit(self.imagejr, self.rect)
            else:
                window.blit(self.imager, self.rect)
        else:
            if self.onair and not self.fall:
                window.blit(self.imagejl, self.rect)
            else:
                window.blit(self.imagel, self.rect)

    def Up_Pressed(self):
        if not self.onair:
            self.onair = True
            self.fall = False

    def Fall_Check(self):
        if not self.counter and self.fall:
            self.dy = 2

    def Jump_Check(self):
        if self.onair and not self.fall:
            if self.counter < jumptime:
                self.counter += 1
                self.dy = -2
            elif self.counter < falltime:
                self.counter += 1
                self.dy = -1
            else:
                self.counter = 0
                self.fall = True

    def ChangeX(self, change):
        self.dx = change

    def ChangePos(self):
        self.right = not self.right

    def Move(self):
        if self.rect[0] + self.dx < 0:
            self.dx = 0
            self.rect.left = 0
        self.Jump_Check()
        self.Fall_Check()
        self.rect.x += self.dx
        self.rect.y += self.dy

    def To_Ground(self):
        self.onair = False

    def On_Collide(self, sprite):
        if isinstance(sprite, ClassMain.Spike):
            self.Die()
        a = pygame.Rect(
            (self.rect[0], self.rect[1] - self.dy), (self.rect[2], self.rect[3])
        )
        if a.colliderect(sprite):
            if self.dx < 0:
                self.rect.left = sprite.rect.right
            else:
                self.rect.right = sprite.rect.left
        else:
            if self.dy < 0:
                self.rect.top = sprite.rect.bottom
                self.fall = True
                self.onair = True
                self.counter = 0
            else:
                self.rect.bottom = sprite.rect.top
                self.fall = True
                self.onair = False
                self.counter = 0

    def ToggleInvi(self):
        self.invisible = True
