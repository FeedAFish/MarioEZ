import pygame
import ImageLoader
from ClassMain import Collidable


class Bonus(Collidable):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=pos)
        self.Move(0, -40)

    def Show(self, window):
        window.blit(self.image, self.rect)

    def Traject(self):
        pass

    def Move(self, a, b):
        self.rect.move_ip(a, b)


class Coin(Bonus):
    def __init__(self, pos, image=ImageLoader.coin):
        super().__init__(pos, image)
        self.counter = 1

    def Traject(self):
        if self.counter:
            self.counter += 1
            if self.counter == 15:
                self.counter = 0
            self.rect.move_ip(0, -4)

    def Show(self, window):
        if self.counter:
            super().Show(window)
        else:
            self.kill()


class Buff(Bonus):
    def __init__(self, pos, color, image=0):
        super().__init__(pos, image=ImageLoader.Buff(color=color))
        self.counter = 1
        self.picked = False
        self.dx = 1
        self.dy = 6

    def Traject(self):
        if self.counter:
            self.counter += 1
            if self.counter == 15:
                self.counter = 0
            self.rect.move_ip(0, -4)
        else:
            self.Move(self.dx, self.dy)

    def Show(self, window):
        if not self.picked:
            super().Show(window)
        else:
            self.kill()

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
