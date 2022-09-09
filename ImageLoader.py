from importlib.resources import path
import os
import pygame

linkp = os.path.dirname(os.path.abspath(__file__))

# Image Load Functions


def Number(i):
    if i == "x":
        return pygame.transform.scale(pygame.image.load(os.path.join(linkp, "Image", "Number", str(i)+".png")), (20, 20))
    return pygame.transform.scale(pygame.image.load(os.path.join(linkp, "Image", "Number", str(i)+".png")), (20, 30))


def PlayerImage(level):
    a = (40, 60) if level else (30, 45)
    return pygame.transform.scale(
        pygame.image.load(os.path.join(linkp, "Image", "marior.png")),
        a), pygame.transform.scale(
        pygame.image.load(os.path.join(linkp, "Image", "mariol.png")),
        a), pygame.transform.scale(
        pygame.image.load(os.path.join(linkp, "Image", "mariojr.png")),
        a), pygame.transform.scale(
        pygame.image.load(os.path.join(linkp, "Image", "mariojl.png")),
        a)


def Barrel(height):
    return pygame.transform.scale(
        pygame.image.load(os.path.join(
            linkp, "Image", "pipe.png")).convert_alpha(),
        (80, int(height)))


def Buff(color):
    return pygame.transform.scale(
        pygame.image.load(os.path.join(
            linkp, "Image", str(color) + "buff.png")),
        (40, 40))


def Turtle(color, fly):
    if fly:
        return pygame.transform.scale(
            pygame.image.load(os.path.join(
                linkp, "Image", str(color) + "turtlefly.png")),
            (40, 50))
    else:
        return pygame.transform.scale(
            pygame.image.load(os.path.join(
                linkp, "Image", str(color) + "turtle.png")),
            (40, 50))


def TurtleShell(color):
    return pygame.transform.scale(
        pygame.image.load(os.path.join(
            linkp, "Image", str(color) + "shellturtle.png")),
        (40, 30))


# Wall
wall = pygame.image.load(
    os.path.join(linkp, "Image", "wall.png"))
wall = pygame.transform.scale(wall, (40, 40))

# Mushroom Monsters
mushm = pygame.image.load(
    os.path.join(linkp, "Image", "mushmonsco.png"))
mushm = pygame.transform.scale(mushm, (40, 35))

mushd = pygame.image.load(
    os.path.join(linkp, "Image", "dmushmons.png"))
mushd = pygame.transform.scale(mushd, (40, 15))

# Bonus Box
bonusbox = pygame.image.load(
    os.path.join(linkp, "Image", "markbox.png"))
bonusbox = pygame.transform.scale(bonusbox, (40, 40))

# Coin
coin = pygame.image.load(
    os.path.join(linkp, "Image", "coin.png"))
coin = pygame.transform.scale(coin, (30, 40))

# Coin Box
coinbox = pygame.image.load(
    os.path.join(linkp, "Image", "coinbox.png"))
coinbox = pygame.transform.scale(coinbox, (40, 40))

# Empty Box

emptybox = pygame.image.load(
    os.path.join(linkp, "Image", "emptybox.png"))
emptybox = pygame.transform.scale(emptybox, (40, 40))

# Flower Spike
flower = pygame.image.load(
    os.path.join(linkp, "Image", "flower.png"))
flower = pygame.transform.scale(flower, (50, 60))

# Temporary land
land = pygame.image.load(
    os.path.join(linkp, "Image", "scr1.png"))
land = pygame.transform.scale(land, (1800, 856))

# Head barrel
headbarrel = pygame.transform.scale(
    pygame.image.load(os.path.join(linkp, "Image", "headpipe.png")),
    (80, 20))

# Hedgehog
hedgehog = pygame.image.load(
    os.path.join(linkp, "Image", "hedgehog.png"))
hedgehog = pygame.transform.scale(hedgehog, (40, 30))
