from importlib.resources import path
import os
import pygame

linkp = os.path.dirname(os.path.abspath(__file__))

barrel = pygame.image.load(os.path.join(linkp, "Image", "Barrel.png"))
barrel = pygame.transform.scale(barrel, (100, 150))

wall = pygame.image.load(os.path.join(linkp, "Image", "wall.png"))
wall = pygame.transform.scale(wall, (40, 40))

imager = pygame.image.load(os.path.join(linkp, "Image", "marior.png"))
imager = pygame.transform.scale(imager, (40, 65))

imagel = pygame.image.load(os.path.join(linkp, "Image", "mariol.png"))
imagel = pygame.transform.scale(imagel, (40, 65))

imagejr = pygame.image.load(os.path.join(linkp, "Image", "mariojr.png"))
imagejr = pygame.transform.scale(imagejr, (40, 65))

imagejl = pygame.image.load(os.path.join(linkp, "Image", "mariojl.png"))
imagejl = pygame.transform.scale(imagejl, (40, 65))

land = pygame.image.load(os.path.join(linkp, "Image", "scr1.png"))
land = pygame.transform.scale(land, (1800, 856))

mushm = pygame.image.load(os.path.join(linkp, "Image", "mushmonsco.png"))
mushm = pygame.transform.scale(mushm, (40, 35))

mushd = pygame.image.load(os.path.join(linkp, "Image", "dmushmons.png"))
mushd = pygame.transform.scale(mushd, (40, 35))

redbuff = pygame.image.load(os.path.join(linkp, "Image", "redbuff.png"))
redbuff = pygame.transform.scale(redbuff, (40, 40))

greenbuff = pygame.image.load(os.path.join(linkp, "Image", "greenbuff.png"))
greenbuff = pygame.transform.scale(greenbuff, (40, 40))

bonusbox = pygame.image.load(os.path.join(linkp, "Image", "bonusbox.png"))
bonusbox = pygame.transform.scale(bonusbox, (40, 40))
