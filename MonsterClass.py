import pygame
from pygame.locals import *
import ImageLoader
import ClassMain


class Monsters(ClassMain.Collidable):
    def __init__(self, pos, image, imaged):
        super().__init__()

        # Image Load
        self.imaged = imaged
        self.image = image
        self.image = pygame.transform.flip(self.image, True, False)
        # Rect Get
        self.rect = self.image.get_rect(topleft=pos)

        # Speed
        self.dx = 0
        self.dy = 0
        self.speed = 3

        # Variable
        self.monalive = True
        self.counter = 0  # Counter for death

        # Traject
        self.trajectcount = 0
        self.limittraject = 600

        # Flying Object
        self.fly = False

        self.test = 0

    # Stats Change Function

    def MonaliveFalse(self):
        self.monalive = False

    # Action Function

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

    def Pl_Collide(self, sprite):
        self.SelfKill(sprite)

    def SelfKill(self, sprite):
        pass

    # Trajectory Function

    def Traject(self):
        if self.trajectcount < self.limittraject:
            self.trajectcount += 1
            self.TrajectCheck()
            if self.trajectcount == self.limittraject/2:
                self.FlipTraject()
            if self.trajectcount % self.speed == 0:
                self.Move(self.dx, self.dy)
        else:
            self.FlipTraject()
            self.Move(self.dx, self.dy)
            self.trajectcount = 1

    def TrajectCheck(self):
        pass

    def FlipTraject(self):
        self.dx = - self.dx
        self.image = pygame.transform.flip(self.image, True, False)


class Mushroom(Monsters):
    def __init__(self, pos, image=ImageLoader.mushm, imaged=ImageLoader.mushd):
        super().__init__(pos, image, imaged)
        self.dx = -1
        self.dy = 6

    def SelfKill(self, sprite):
        if not self.counter:
            self.counter = 100
        self.image = self.imaged
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)


class Turtle(Monsters):
    def __init__(self, pos, color, fly, image=0, imaged=0):
        super().__init__(pos, image=ImageLoader.Turtle(
            color, fly), imaged=ImageLoader.TurtleShell(color))
        # Kill Mode - Turtle
        self.mode = True

        # Flying turtle
        self.fly = fly

    # Turtle into Shell

    def SelfKill(self, sprite):
        if self.mode:
            self.Shell()
            self.fly = False
        else:
            self.ShellAction(sprite)

    def Shell(self):
        self.image = self.imaged
        self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        self.mode = False
        self.dx = 0
        self.dy = 6

    def ShellAction(self, sprite):
        if not self.dx:
            if self.rect.left > sprite.rect.left:
                self.dx = 4
            else:
                self.dx = -4
        else:
            self.dx = 0

    def Traject(self):
        if self.mode:
            super().Traject()
        else:
            self.Move(self.dx, self.dy)


class TurtleLand(Turtle):
    def __init__(self, pos, color, fly=False, image=0, imaged=0):
        super().__init__(pos, color, fly, image, imaged)
        self.dx = -1
        self.dy = 6


class TurtleFly(Turtle):
    def __init__(self, pos, color, fly=True, image=0, imaged=0):
        super().__init__(pos, color, fly, image, imaged)
        self.dx = -1
        self.dy = 3

    def TrajectCheck(self):
        if self.mode and not self.trajectcount % 150:
            self.dy = - self.dy
