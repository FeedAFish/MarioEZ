from tkinter import CENTER
import pygame
import pathimage
from ClassMain import Collidable


class Bonus(Collidable):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.Move(0, -40)
        # self.counter = 1

    def Show(self, window):
        window.blit(self.image, self.rect)


class Coin(Bonus):
    def __init__(self, pos, image=pathimage.coin):
        super().__init__(pos, image)
        self.counter = 1

    def Traject(self):
        if self.counter:
            self.counter += 1
            if self.counter == 15:
                self.counter = 0
            self.rect.move_ip(0, -4)

    def Move(self, a, b):
        self.rect.move_ip(a, b)

    def Show(self, window):
        if self.counter:
            super().Show(window)


class Buff(Bonus):
    def __init__(self, pos, image=pathimage.redbuff):
        super().__init__(pos, image)
        self.counter = 1
        self.picked = False
        self.dx = 1
        self.dy = 4

    def Traject(self):
        if self.counter:
            self.counter += 1
            if self.counter == 15:
                self.counter = 0
            self.rect.move_ip(0, -4)
        else:
            self.Move(self.dx, self.dy)

    def Move(self, a, b):
        self.rect.move_ip(a, b)

    def Show(self, window):
        if not self.picked:
            super().Show(window)

    def On_collide(self, sprite):
        if self.counter:
            pass
        else:
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

    def Picked(self):
        self.picked = True
