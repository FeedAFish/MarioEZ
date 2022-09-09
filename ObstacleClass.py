import ClassMain
import ImageLoader


class Obstacles(ClassMain.Collidable):
    def __init__(self, pos, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=pos)

    def Show(self, window):
        window.blit(self.image, self.rect)

    def Move(self, a, b):
        self.rect.move_ip(a, b)

    def Pl_Collide(self, sprite):
        pass

# Barrel


class Barrel(Obstacles):
    def __init__(self, pos, height):
        super().__init__(pos, image=ImageLoader.Barrel(height))
        self.image.blit(ImageLoader.headbarrel, (0, 0))


# Wall


class Wall(Obstacles):
    def __init__(self, pos, image=ImageLoader.wall):
        super().__init__(pos, image)
        self.impactcount = 0
        self.toggle = False
        self.coin = 0

    def On_collide(self, sprite):
        if not self.impactcount:
            self.impactcount = 14

    def BoxJump(self):
        if self.impactcount:
            self.impactcount -= 1
            if self.impactcount < 7:
                self.Move(0, 1)
            else:
                self.Move(0, -1)

    def Coinleave(self):
        self.coin = 0

    def ToggleFalse(self):
        self.toggle = False

# Box


class Box(Wall):
    def __init__(self, pos, image, imaged=ImageLoader.emptybox):
        super().__init__(pos, image)
        self.imaged = imaged
        self.coin = 1

    def Show(self, window):
        if self.toggle:
            window.blit(self.image, self.rect)
        else:
            window.blit(self.imaged, self.rect)


class CoinBox(Box):
    def __init__(self, pos, image=ImageLoader.coinbox):
        super().__init__(pos, image)
        self.toggle = True
        self.coin = 1


# Temporary

class Land(Obstacles):
    def __init__(self, pos=(0, 370), image=ImageLoader.land):
        super().__init__(pos, image)
