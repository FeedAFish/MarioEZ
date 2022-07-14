import pygame
from pygame.locals import *
from ClassPlayer import Player
from ObstaclesClass import Land, Pipe, Wall
from MonsterClass import Mush
import os

linkp = os.path.dirname(os.path.abspath(__file__))

pygame.init()
displayw = 800
displayh = 456
window = pygame.display.set_mode((displayw, displayh))

bg_img = pygame.image.load(os.path.join(linkp, "Image", "scr1.png"))
bg_img = pygame.transform.scale(bg_img, (displayw, displayh))
buttonpr = pygame.image.load(os.path.join(linkp, "Image", "button.png"))
buttonpr = pygame.transform.scale(buttonpr, (120, 60))
button = pygame.image.load(os.path.join(linkp, "Image", "buttonpressed.png"))
button = pygame.transform.scale(button, (120, 60))


class Mario(object):
    def __init__(self, displayw, displayh):
        self.running = True
        self.height = displayh
        self.width = displayw

        # self.timer = 0
        self.iter = 0
        self.move = False
        self.test = False
        self.player = Player((100, 100))
        self.position = 500
        self.scroll = 0
        self.obstacles = []
        self.monsters = []
        # self.buff = []
        self.land = Land()
        self.turtlem = Mush(pos=(700, 326))
        self.monsters.append(self.turtlem)
        # self.Addbuff(redbuffpos=(550, 346))
        self.AddObstacle(pipepos=(900, 256))
        self.AddObstacle(wallpos=(550, 206), wallnumber=4)
        self.MainMenu()

    def MainMenu(self):
        while True:
            window.fill((0, 0, 0))
            window.blit(bg_img, (0, 0))
            mouse = pygame.mouse.get_pos()
            if (
                displayw / 2 - 60 <= mouse[0] <= displayw / 2 + 60
                and displayh / 2 - 30 <= mouse[1] <= displayh / 2 + 30
            ):
                window.blit(button, (self.width / 2 -
                            60, self.height / 2 - 30))
            else:
                window.blit(buttonpr, (self.width / 2 -
                            60, self.height / 2 - 30))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        displayw / 2 - 60 <= mouse[0] <= displayw / 2 + 60
                        and displayh / 2 - 30 <= mouse[1] <= displayh / 2 + 30
                    ):
                        self.Main()
            pygame.display.update()

    def ScrollScreen(self):
        if self.scroll == displayw:
            self.scroll = 0
        window.fill((0, 0, 0))
        window.blit(bg_img, (-self.scroll, 0))
        window.blit(bg_img, (displayw - self.scroll, 0))
        if self.move:
            self.scroll += 1
            self.position += 1
            for i in self.obstacles + self.monsters:  # + self.monsters + self.buff:
                i.Move(-1, 0)

    def AddObstacle(self, **kwargs):
        if kwargs.get("pipepos"):
            a = Pipe(kwargs.get("pipepos"))
            self.obstacles.append(a)
        if kwargs.get("wallpos"):
            a = Wall(kwargs.get("wallpos"), kwargs.get("wallnumber"))
            self.obstacles.append(a)

    def Main(self):
        while self.running:

            # Show objects

            self.ScrollScreen()
            self.player.Show(window)
            for i in self.obstacles + self.monsters:
                i.Show(window)

            # Check events -- Right now no uses

            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            # Check player movements -- UDLR

            if pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]:
                self.player.ChangeX(-1)
                if self.player.right:
                    self.player.ChangePos()
            elif pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
                self.player.ChangeX(1)
                if not self.player.right:
                    self.player.ChangePos()
            else:
                self.player.ChangeX(0)

            # Jump key check

            if pressed[pygame.K_UP]:
                self.player.Up_Pressed()

            # Scroll screen check

            if self.player.rect[0] > 400:
                if pressed[pygame.K_RIGHT]:
                    self.player.ChangeX(0)
                    self.move = True
                else:
                    self.move = False
            else:
                self.move = False

            # Move player

            self.player.Move()

            # Collision check

            check_ground = False  # Collision bottom -- onair check
            if self.player.rect.colliderect(self.land):
                self.player.On_Collide(self.land)
                check_ground = True
            for i in self.obstacles:
                if self.player.rect.colliderect(i):
                    self.player.On_Collide(i)
                    check_ground = True
            if not check_ground:
                self.player.TO_Air()

            # Monster's collision check -- alive monster check only

            for i in self.monsters:
                if self.player.rect.colliderect(i) and i.monalive:
                    self.player.On_Collide(i)

            # Monster's trajectory movement

            for i in self.monsters:
                if i.monalive and not(i.counter):
                    print(1)
                    i.Traject()
            pygame.display.flip()


Mario(displayw, displayh)
