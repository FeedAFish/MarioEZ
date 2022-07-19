from importlib.resources import path
import os
import turtle
import pygame

linkp = os.path.dirname(os.path.abspath(__file__))

barrel = pygame.image.load(os.path.join(linkp, "Image", "Barrel.png"))
barrel = pygame.transform.scale(barrel, (80, 120))

wall = pygame.image.load(os.path.join(linkp, "Image", "wall.png"))
wall = pygame.transform.scale(wall, (40, 40))

imager = pygame.image.load(os.path.join(linkp, "Image", "marior.png"))
imager = pygame.transform.scale(imager, (30, 45))

imagel = pygame.image.load(os.path.join(linkp, "Image", "mariol.png"))
imagel = pygame.transform.scale(imagel, (30, 45))

imagejr = pygame.image.load(os.path.join(linkp, "Image", "mariojr.png"))
imagejr = pygame.transform.scale(imagejr, (30, 45))

imagejl = pygame.image.load(os.path.join(linkp, "Image", "mariojl.png"))
imagejl = pygame.transform.scale(imagejl, (30, 45))

land = pygame.image.load(os.path.join(linkp, "Image", "scr1.png"))
land = pygame.transform.scale(land, (1800, 856))

mushm = pygame.image.load(os.path.join(linkp, "Image", "mushmonsco.png"))
mushm = pygame.transform.scale(mushm, (40, 35))

mushd = pygame.image.load(os.path.join(linkp, "Image", "dmushmons.png"))
mushd = pygame.transform.scale(mushd, (40, 15))

redbuff = pygame.image.load(os.path.join(linkp, "Image", "redbuff.png"))
redbuff = pygame.transform.scale(redbuff, (40, 40))

greenbuff = pygame.image.load(os.path.join(linkp, "Image", "greenbuff.png"))
greenbuff = pygame.transform.scale(greenbuff, (40, 40))

bonusbox = pygame.image.load(os.path.join(linkp, "Image", "bonusbox.png"))
bonusbox = pygame.transform.scale(bonusbox, (40, 40))

landturtlered = pygame.image.load(
    os.path.join(linkp, "Image", "turtlered.png"))
landturtlered = pygame.transform.scale(landturtlered, (40, 50))

turtleshell = pygame.image.load(
    os.path.join(linkp, "Image", "shellturtle.png"))
turtleshell = pygame.transform.scale(turtleshell, (40, 30))

flyturtlered = pygame.image.load(
    os.path.join(linkp, "Image", "turtleflyred.png"))
flyturtlered = pygame.transform.scale(flyturtlered, (40, 50))

coinbox = pygame.image.load(
    os.path.join(linkp, "Image", "coinbox.png"))
coinbox = pygame.transform.scale(coinbox, (40, 40))

coin = pygame.image.load(
    os.path.join(linkp, "Image", "coin.png"))
coin = pygame.transform.scale(coin, (30, 40))


def Number(i):
    if i == "x":
        return pygame.transform.scale(pygame.image.load(os.path.join(linkp, "Image", "Number", str(i)+".png")), (20, 20))
    return pygame.transform.scale(pygame.image.load(os.path.join(linkp, "Image", "Number", str(i)+".png")), (20, 30))


def LoadLandTurtle(color):
    return pygame.transform.scale(pygame.image.load(os.path.join(linkp, "Image", "turtle" + str(color) + ".png")), (40, 50))
