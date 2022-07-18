import pygame
import pathimage
from ClassMain import Collidable


class Bonus(Collidable):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)
        # self.counter = 1

    def Show(self, window):
        window.blit(self.image, self.rect)


class Coin(Bonus):
    def __init__(self, pos, image=pathimage.redbuff):
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
