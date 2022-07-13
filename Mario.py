import pygame
from pygame.locals import *
from ClassPlayer import Player
# from MonsterClass import Mush
# from SpritesClass import Mush, Player, Pipe, Land, Wall, RedBuff, GreenBuff

import os

linkp = os.path.dirname(os.path.abspath(__file__))

pygame.init()
displayw = 1800
displayh = 856
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
        self.buff = []
        self.land = Land()
        self.turtlem = Mush((800, 671))
        self.monsters.append(self.turtlem)
        self.Addbuff(redbuffpos=(550, 346))
        self.AddObstacle(pipepos=(900, 556))
        self.AddObstacle(wallpos=(550, 446), wallnumber=4)
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
                window.blit(button, (self.width / 2 - 60, self.height / 2 - 30))
            else:
                window.blit(buttonpr, (self.width / 2 - 60, self.height / 2 - 30))
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

    def Main(self):
        while self.running:
            self.ScrollScreen()
            self.player.Show(window)
            for i in self.obstacles:
                i.Show(window)
            for i in self.monsters:
                if not i.delete:
                    i.Show(window)
            for i in self.buff:
                if i.aliveb:
                    i.Show(window)

            pressed = pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            if pressed[pygame.K_LEFT] and not pressed[pygame.K_RIGHT]:
                self.player.ChangeX(-1)
                if self.player.right:
                    self.player.ChangePos()
            elif pressed[pygame.K_RIGHT] and not pressed[pygame.K_LEFT]:
                self.player.ChangeX(1)
                if not self.player.right:
                    self.player.ChangePos()
            else:
                self.player.ChangeX()
            if pressed[pygame.K_UP]:
                self.player.Keyup()
            if self.player.rect[0] > 700:
                if pressed[pygame.K_RIGHT]:
                    self.player.ChangeX(0)
                    self.move = True
                else:
                    self.move = False
            else:
                self.move = False
            self.player.Move()
            leave = True
            if self.player.rect.colliderect(self.land):
                self.player.On_Collide(self.land)
                leave = False
            for i in self.obstacles:
                if self.player.rect.colliderect(i):
                    self.player.On_Collide(i)
                    leave = False
            if leave:
                self.player.OAToTrue()
            for i in range(len(self.monsters)):
                if self.player.rect.colliderect(self.monsters[i]):
                    if self.monsters[i].alivem:
                        self.player.On_Collide_Mon(self.monsters[i])
                        self.monsters[i].Die()
            for i in range(len(self.monsters)):
                self.monsters[i].Trajet()
            for i in self.buff:
                i.Trajet()
            for i in self.buff:
                if i.aliveb:
                    if i.rect.colliderect(self.land.rect):
                        i.Collide(self.land)
                    for j in self.obstacles:
                        if i.rect.colliderect(j.rect):
                            print(2)
                            i.Collide(j)
                    if self.player.rect.colliderect(i):
                        i.Collide(self.player)
            # self.timer += 1
            pygame.display.flip()

    def ScrollScreen(self):
        if self.scroll == 1650:
            self.scroll = 0
        window.fill((0, 0, 0))
        window.blit(bg_img, (-self.scroll, 0))
        window.blit(bg_img, (1650 - self.scroll + 1, 0))
        if self.move:
            self.scroll += 1
            self.position += 1
            for i in self.obstacles + self.monsters + self.buff:
                i.Move(-1, 0)

    def AddObstacle(self, **kwargs):
        if kwargs.get("pipepos"):
            a = Pipe(kwargs.get("pipepos"))
            self.obstacles.append(a)
        if kwargs.get("wallpos"):
            a = Wall(kwargs.get("wallpos"), kwargs.get("wallnumber"))
            self.obstacles.append(a)

    def Addbuff(self, **kwargs):
        if kwargs.get("redbuffpos"):
            a = RedBuff(kwargs.get("redbuffpos"))
            self.buff.append(a)
        elif kwargs.get("greenbuffpos"):
            a = GreenBuff(kwargs.get("greenbuffposs"))
            self.buff.append(a)


Mario(displayw, displayh)
