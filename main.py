import pygame
from pygame.locals import *
from BonusClass import Coin
from ClassPlayer import Player
from ObstaclesClass import Coinbox, Land, Pipe, Wall
from MonsterClass import Mush, TurtleFly, TurtleLand, TurtleMons
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
        self.turtlem = TurtleFly(pos=(340, 266))
        self.monsters.append(self.turtlem)
        self.turtlem = TurtleLand(pos=(1000, 166))
        self.monsters.append(self.turtlem)
        self.turtlem = TurtleLand(pos=(800, 166))
        self.monsters.append(self.turtlem)
        # self.Addbuff(redbuffpos=(550, 346))
        self.AddObstacle(pipepos=(900, 256))
        self.AddObstacle(pipepos=(1300, 256))
        self.AddObstacle(wallpos=(380, 306), wallnumber=4)
        self.AddObstacle(wallpos=(950, 206), wallnumber=4)
        self.AddObstacle(coinpos=(280, 206))
        self.bonus = []
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
            # + self.monsters + self.buff:
            for i in self.obstacles + self.monsters + self.bonus:
                i.Move(-1, 0)

    def AddObstacle(self, **kwargs):
        if kwargs.get("pipepos"):
            a = Pipe(kwargs.get("pipepos"))
            self.obstacles.append(a)
        if kwargs.get("wallpos"):
            a = Wall(kwargs.get("wallpos"), kwargs.get("wallnumber"))
            self.obstacles.append(a)
        if kwargs.get("coinpos"):
            a = Coinbox(kwargs.get("coinpos"), 1)
            self.obstacles.append(a)

    def Main(self):
        while self.running:

            # Show objects

            self.ScrollScreen()
            self.ShowObj()

            # Check events -- Right now no uses

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            # Check player movements -- UDLR

            self.Check_UDLR()

            # Move player

            self.player.Move()

            # Collision check

            self.Collision_Check()

            # Monster's collision check -- alive monster check only

            self.MonsCollisionCheck()

            # Monster's trajectory movement
            # Monster's collision Check

            self.MonsTrajectory()

            self.MonsCollisionCheck

            self.BonusTraject()

            pygame.display.flip()

    def ShowObj(self):
        self.player.Show(window)
        for i in self.obstacles + self.monsters+self.bonus:
            i.Show(window)

    def Check_UDLR(self):
        pressed = pygame.key.get_pressed()
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
        if pressed[pygame.K_UP]:
            self.player.Up_Pressed()
        # Check Screen scroll
        if self.player.rect[0] > 400:
            if pressed[pygame.K_RIGHT]:
                self.player.ChangeX(0)
                self.move = True
            else:
                self.move = False
        else:
            self.move = False

    def Collision_Check(self):
        check_ground = False  # Collision bottom -- onair check
        if self.player.rect.colliderect(self.land):
            self.player.On_Collide(self.land)
            check_ground = True
        for i in self.obstacles:
            if self.player.rect.colliderect(i):
                self.player.On_Collide(i)

                check_ground = True
            if isinstance(i, Coinbox):
                i.BoxJump()
                if not i.coin and i.toggle:
                    self.AddBonus(coinpos=i.rect.topleft)
                    i.ToggleFalse()
        if not check_ground:
            self.player.TO_Air()

    def MonsCollisionCheck(self):
        for i in self.monsters:
            if self.player.rect.colliderect(i) and i.monalive:
                self.player.On_Collide(i)

    def MonsTrajectory(self):
        for i in self.monsters:
            if i.monalive and not(i.counter):
                i.Traject()
            if i.rect.colliderect(self.land):
                i.On_collide(self.land)
            for j in self.obstacles:
                if i.monalive and i.rect.colliderect(j):
                    i.On_collide(j)
            if isinstance(i, TurtleMons):
                if not i.mode:
                    for j in set(self.monsters) - set([i]):
                        if j.monalive and i.rect.colliderect(j):
                            if j.mode:
                                j.MonaliveFalse()

    def BonusTraject(self):
        for i in self.bonus:
            i.Traject()

    def AddBonus(self, **kwargs):
        if kwargs.get("coinpos"):
            a = Coin(kwargs.get("coinpos"))
            self.bonus.append(a)


Mario(displayw, displayh)
