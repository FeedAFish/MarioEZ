from re import S
import pygame
from pygame import *

import Data.dataloader
import ImageLoader
import ObstacleClass
import MonsterClass
import BonusClass
import SpikeClass
import ClassPlayer

import os

linkp = os.path.dirname(os.path.abspath(__file__))

pygame.init()
displayw = 800
displayh = 450
window = pygame.display.set_mode((displayw, displayh))

bg_img = pygame.image.load(os.path.join(linkp, "Image", "background.png"))
bg_img = pygame.transform.scale(bg_img, (displayw, displayh))
buttonpr = pygame.image.load(os.path.join(linkp, "Image", "button.png"))
buttonpr = pygame.transform.scale(buttonpr, (120, 60))
button = pygame.image.load(os.path.join(linkp, "Image", "buttonpressed.png"))
button = pygame.transform.scale(button, (120, 60))

clock = pygame.time.Clock()


class Mario(object):
    def __init__(self, displayw, displayh):

        # Window variable
        self.running = True
        self.height = displayh
        self.width = displayw

        # Counting variable
        self.move = False
        self.position = 400

        # Screen scroll variable
        self.scroll = 0

        # Player Create
        self.player = ClassPlayer.Player((100, 100))

        # Sprite groups
        self.obstacle = pygame.sprite.Group()
        self.monster = pygame.sprite.Group()
        self.spike = pygame.sprite.Group()
        self.bonus = pygame.sprite.Group()

        # Land Temporary
        self.land = ObstacleClass.Land()

        # Launch Menu
        self.MainMenu()

    # Feature Functions

        # Scroll Screen

    def ScrollScreen(self):
        if self.scroll == displayw:
            self.scroll = 0
        window.fill((0, 0, 0))
        window.blit(bg_img, (-self.scroll, 0))
        window.blit(bg_img, (displayw - self.scroll, 0))
        if self.move:
            self.scroll += 1
            self.position += 1
            for i in self.monster.sprites() + self.bonus.sprites() + self.obstacle.sprites() + self.spike.sprites():
                i.Move(-1, 0)

        # Show Object

    def ShowObj(self):
        self.player.Show(window)
        for i in self.monster.sprites() + self.bonus.sprites() + self.spike.sprites() + self.obstacle.sprites():
            i.Show(window)
            if i.rect[0] < -200:
                i.kill()

        # Moving Functions

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

        self.ScreenScrollCheck(pressed)

        # Check Screen scroll

    def ScreenScrollCheck(self, pressed):
        if self.player.rect[0] > 400:
            if pressed[pygame.K_RIGHT]:
                self.player.ChangeX(0)
                self.move = True
            else:
                self.move = False
        else:
            self.move = False

        # Sub-Feature

            # Turtle shell hit

    def TurtleHit(self, i):
        if isinstance(i, MonsterClass.Turtle):
            if not i.mode:
                for j in set(self.monster) - set([i]):
                    if j.monalive and i.rect.colliderect(j):
                        if i.dx:
                            j.MonaliveFalse()

            # Buff x Player

    def Buff_Player(self, i):
        if i.rect.colliderect(self.player) and not i.picked:
            i.Picked()
            self.player.LevelChange(1)

    # Collision Obstacles x Player Check

    def Collision_Check(self):
        check_ground = False  # Collision bottom -- onair check
        if self.player.rect.colliderect(self.land):
            self.player.On_Collide(self.land)
            check_ground = True
        for i in self.obstacle.sprites():
            if self.player.rect.colliderect(i):
                self.player.On_Collide(i)
                check_ground = True
            if isinstance(i, ObstacleClass.Wall):
                i.BoxJump()
                if i.toggle and not i.coin:
                    self.AddBonus(buffpos=i.rect.center)
                    i.ToggleFalse()
        if not check_ground:
            self.player.TO_Air()

    # Collision Monster and Spike x Player check

    def MonsCollisionCheck(self):
        for i in self.monster.sprites():
            if self.player.rect.colliderect(i) and i.monalive:
                self.player.On_Collide(i)
        for i in self.spike.sprites():
            if self.player.rect.colliderect(i):
                self.player.Die()

    # Collision Monster x Obstacle check

    def Obstacles_Monster(self, i):
        if i.rect.colliderect(self.land):
            i.On_collide(self.land)
        for j in self.obstacle.sprites():
            if i.monalive and i.rect.colliderect(j):
                if isinstance(j, ObstacleClass.Wall) and j.impactcount:
                    i.kill()
                else:
                    i.On_collide(j)

    # Monster + Spike Trajectory

    def MonsTrajectory(self):
        for i in self.monster.sprites():
            if i.monalive and not(i.counter):
                i.Traject()
            # Obstacle x Monster
            self.Obstacles_Monster(i)
            # Turtle Hitbox check
            self.TurtleHit(i)
        for i in self.spike.sprites():
            i.Trajet()

    # Bonus Trajectory

    def BonusTraject(self):
        for i in self.bonus.sprites():
            i.Traject()
            for j in self.obstacle.sprites():
                if i.rect.colliderect(j):
                    i.On_collide(j)
            if i.rect.colliderect(self.land):
                i.On_collide(self.land)
            self.Buff_Player(i)

    # Adding Functions

        # Obstacles

    def AddObstacle(self, **kwargs):
        if kwargs.get("pipepos"):
            a = ObstacleClass.Barrel(pos=kwargs.get(
                "pipepos"), height=kwargs.get("pipeheight"))
            self.obstacle.add(a)
        if kwargs.get("wallpos"):
            a = ObstacleClass.Wall(kwargs.get("wallpos"))
            self.obstacle.add(a)
        if kwargs.get("markpos"):
            a = ObstacleClass.CoinBox(kwargs.get("markpos"))
            self.obstacle.add(a)

        # Bonus

    def AddBonus(self, **kwargs):
        if kwargs.get("buffpos"):
            a = BonusClass.Buff(color="red", pos=kwargs.get("buffpos"))
            self.bonus.add(a)

    # Showing Stats Functions:

    def ShowLife(self):
        window.blit(ImageLoader.PlayerImage(0)[2], (10, 10))
        window.blit(ImageLoader.Number("x"), (45, 25))
        window.blit(ImageLoader.Number(self.player.life), (70, 20))

    # Window Showing Functions

        # Main game

    def Main(self):
        self.LoadData()
        while self.running:
            clock.tick(90)

            # Show objects

            self.ScrollScreen()
            self.ShowObj()
            self.ShowLife()
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

            self.BonusTraject()

            pygame.display.flip()

        # Menu

    def MainMenu(self):
        while True:
            window.blit(bg_img, (0, 0))

            mouse = pygame.mouse.get_pos()

            # Mouse position check for button
            if (
                displayw / 2 - 60 <= mouse[0] <= displayw / 2 + 60
                and displayh / 2 - 30 <= mouse[1] <= displayh / 2 + 30
            ):
                window.blit(button, (self.width / 2 -
                            60, self.height / 2 - 30))
            else:
                window.blit(buttonpr, (self.width / 2 -
                            60, self.height / 2 - 30))

            # Check window close
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

                # Click on button
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (
                        displayw / 2 - 60 <= mouse[0] <= displayw / 2 + 60
                        and displayh / 2 - 30 <= mouse[1] <= displayh / 2 + 30
                    ):
                        self.Main()
            pygame.display.update()

    # Temporary

    def LoadData(self):
        self.Load()
        # a = SpikeClass.Flower(pos=(915, 250))
        # self.spike.add(a)

        # self.turtlem = MonsterClass.TurtleFly(color='green', pos=(340, 166))
        # self.monster.add(self.turtlem)

        # self.turtlem = MonsterClass.Mushroom(pos=(540, 166))
        # self.monster.add(self.turtlem)

        # self.turtlem = SpikeClass.Hedgehog(pos=(540, 166))
        # self.monster.add(self.turtlem)

    def Load(self):
        f = Data.dataloader.level(1)
        self.LoadWall(f)
        self.LoadPipe(f)
        self.LoadTurtle(f)
        self.LoadFlower(f)

    def LoadPipe(self, f):
        for i in range(len(f.data["Pipeposx"])):
            if f.data["Pipeposx"][i]:
                g = ObstacleClass.Barrel(
                    pos=(f.data["Pipeposx"][i], f.data["Pipeposy"][i]), height=f.data["Pipeheight"][i])
            else:
                break
            self.obstacle.add(g)

    def LoadTurtle(self, f):
        for i in range(len(f.data["Turtlex"])):
            if f.data["Turtlex"][i]:
                g = MonsterClass.TurtleLand(
                    pos=(f.data["Turtlex"][i], f.data["Turtley"][i]), color=f.data["TColor"][i])
            else:
                break
            self.monster.add(g)

    def LoadWall(self, f):
        for i in range(len(f.data["Wallx"])):
            if f.data["Wallx"][i]:
                for j in range(int(f.data["WallNo"][i])):
                    g = ObstacleClass.Wall(
                        pos=(f.data["Wallx"][i]+40*j, f.data["Wally"][i]))
                    self.obstacle.add(g)
            else:
                break

    def LoadFlower(self, f):
        for i in range(len(f.data["Flowerx"])):
            if f.data["Flowerx"][i]:
                g = SpikeClass.Flower(
                    pos=(f.data["Flowerx"][i], f.data["Flowery"][i]))
            else:
                break
            self.spike.add(g)


Mario(displayw, displayh)
