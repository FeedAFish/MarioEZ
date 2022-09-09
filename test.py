import pygame
from pygame.locals import *
import ImageLoader
import os
import Data.dataloader

import MonsterClass
import ObstacleClass

pygame.init()
displayw = 800
displayh = 450
window = pygame.display.set_mode((displayw, displayh))

linkp = os.path.dirname(os.path.abspath(__file__))

bg_img = pygame.image.load(os.path.join(linkp, "Image", "background.png"))
bg_img = pygame.transform.scale(bg_img, (displayw, displayh))

a = ImageLoader.Barrel(400)
b = a.get_rect(topleft=(0, 0))

c = MonsterClass.TurtleLand(color="green", pos=(200, 0))
d = MonsterClass.TurtleFly(color="green", pos=(400, 0))
gr = pygame.sprite.Group()
gr.add(c)
gr.add(d)

e = ObstacleClass.Barrel(pos=(400, 0), height=120)
gr2 = pygame.sprite.Group()
gr2.add(e)
print(gr2.sprites())

f = Data.dataloader.level(1)
gr = pygame.sprite.Group()

for i in range(len(f.data["Pipeposx"])):
    g = ObstacleClass.Barrel(
        pos=(f.data["Pipeposx"][i], f.data["Pipeposy"][i]), height=120)
    gr.add(g)

while True:
    window.fill((0, 0, 0))
    window.blit(bg_img, (0, 0))
    window.blit(a, b)
    for i in gr2.sprites() + gr.sprites():
        i.Show(window)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
    pygame.display.flip()
