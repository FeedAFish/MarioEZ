import pygame
import ClassMain
import ImageLoader


class Spike(ClassMain.Collidable):
    def __init__(self, pos, img):
        super().__init__()

        self.image = img
        self.rect = self.image.get_rect(topleft=pos)
        self.monalive = True
        self.counter = 0

        # Speed
        self.dx = 0
        self.dy = 0
        self.speed = 1

        # Traject
        self.trajectcount = 0
        self.limittraject = 600

    # Action Function

    def Traject(self):
        pass

    def Move(self, a, b):
        self.rect.move_ip(a, b)

    def Show(self, window):
        if self.monalive:
            window.blit(self.image, self.rect)

    # Stats Change Function

    def MonaliveFalse(self):
        self.monalive = False

    # Collision Function

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
            self.image = pygame.transform.flip(
                self.image, True, False)
        else:
            if self.dy < 0:
                self.rect.top = sprite.rect.bottom
            else:
                self.rect.bottom = sprite.rect.top


class Flower(Spike):
    def __init__(self, pos, img=ImageLoader.flower):
        super().__init__(pos, img)
        self.dy = -1
        self.counter = 0

    def Trajet(self):
        if self.counter < self.rect.height:
            self.Move(self.dx, self.dy)
        elif self.counter < 2 * self.rect.height:
            pass
        elif self.counter < 3 * self.rect.height:
            self.Move(self.dx, -self.dy)
        elif self.counter == 4 * self.rect.height - 1:
            self.counter = -1
        self.counter += 1


class Hedgehog(Spike):
    def __init__(self, pos, img=ImageLoader.hedgehog):
        super().__init__(pos, img)
        self.dx = -1
        self.dy = 6
        self.speed = 2

    def Traject(self):
        if self.trajectcount < self.limittraject:
            self.trajectcount += 1
            if self.trajectcount == self.limittraject/2:
                self.FlipTraject()
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.FlipTraject()
            self.Move(self.dx, self.dy)
            self.trajectcount = 1

    def FlipTraject(self):
        self.dx = - self.dx
        self.image = pygame.transform.flip(self.image, True, False)

    def MonaliveFalse(self):
        self.monalive = False
