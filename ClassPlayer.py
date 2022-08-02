import pygame
import ObstaclesClass
from pygame.locals import *
from MonsterClass import Monsters
from ObstaclesClass import Obstacles
import pathimage
import ClassMain


jumptime = 60
falltime = 75


class Player(ClassMain.Collidable):
    def __init__(
        self,
        pos,
    ):
        super().__init__()
        self.level = 1
        self.imager, self.imagel, self.imagejr, self.imagejl = pathimage.PlayerImage(
            self.level)

        self.rect = self.imager.get_rect(topleft=pos)

        # Variable
        self.onair = True
        self.fall = True
        self.right = True
        self.moveable = True
        # Counter Jump On Air
        self.counter = 0
        # Level

        self.life = 2
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
        if self.invisibleTimer:
            self.invisibleTimer -= 1
        else:
            self.invisible = False

    def To_Ground(self):
        self.onair = False

    def TO_Air(self):
        self.onair = True

    def On_Collide(self, sprite):
        if isinstance(sprite, ClassMain.Spike):
            self.Die()
        a = pygame.Rect(
            (self.rect[0], self.rect[1] -
             self.dy), (self.rect[2], self.rect[3])
        )
        if isinstance(sprite, Obstacles):
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
                    # Collision coin box
                    if isinstance(sprite, ObstaclesClass.Wall):
                        sprite.On_collide(self)
                        if sprite.coin:
                            sprite.Coinleave()
                else:
                    self.rect.bottom = sprite.rect.top
                    self.fall = True
                    self.onair = False
                    self.counter = 0
        else:
            if a.colliderect(sprite) or self.dy < 0:
                self.Die()
            else:
                self.fall = False
                self.onair = True
                self.counter = 0
                sprite.Pl_Collide(self)

    def ToggleInvi(self):
        self.invisible = True
        self.invisibleTimer = 100

    def Die(self):
        if self.level and not self.invisible:
            self.level -= 1
            self.imager, self.imagel, self.imagejr, self.imagejl = pathimage.PlayerImage(
                self.level)
            self.rect = self.imagel.get_rect(bottomleft=self.rect.bottomleft)
            self.ToggleInvi()
        elif not self.invisible:
            if self.life:
                print("RIP")
                self.rect.topleft = (100, 100)
                self.life -= 1
            else:
                pygame.quit()
        else:
            pass

    def LevelChange(self, x):
        self.level = x
        self.imager, self.imagel, self.imagejr, self.imagejl = pathimage.PlayerImage(
            self.level)
        self.rect = self.imagel.get_rect(bottomleft=self.rect.bottomleft)
