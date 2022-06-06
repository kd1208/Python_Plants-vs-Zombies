import pygame as pg
import random
from source import constants as c


# 普通僵尸
class Zombie(pg.sprite.Sprite):
    def __init__(self):
        super(Zombie, self).__init__()
        self.image = pg.image.load('images/Zombies/NormalZombie/Zombie/Zombie_0.png').convert_alpha()
        self.images = [pg.image.load('images/Zombies/NormalZombie/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 22)]
        self.walkingimages = [pg.image.load('images/Zombies/NormalZombie/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 22)]
        self.dieimages = [pg.image.load('images/Zombies/NormalZombie/ZombieDie/ZombieDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 10)]
        self.attackimages = [pg.image.load('images/Zombies/NormalZombie/ZombieAttack/ZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in range(0, 21)]
        self.bombdieimages = [ pg.image.load('images/Zombies/NormalZombie/BoomDie/BoomDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 20)]
        self.rect = self.images[0].get_rect()
        self.row = random.randint(1, 5)
        self.col = -1
        self.rect.top = 25 + (self.row - 1) * 100
        self.rect.left = 750
        self.speed = 2
        self.life = c.normal_life
        self.dietimes = 0
        self.bombsign = 0
        self.eattime = 0
        self.s = pg.mixer.Sound('sound/zombieAttack.ogg')

    def attacking(self, mapp):
        self.col = self.getCol()
        if self.col == 10:
            pass
        else:
            if not mapp.isEmpty(self.row-1, self.col-1):
                self.images = self.attackimages
                self.speed = 0
                if self.eattime == 0:
                    self.s = pg.mixer.Sound('sound/zombieAttack.ogg')
                    self.s.play(-1)
                mapp.plants[self.row-1][self.col-1].life -= 1
                self.eattime += 1
                if mapp.plants[self.row-1][self.col-1].life <= 0:
                    mapp.map[self.row-1][self.col-1] = 0
                    self.eattime = 0
                    self.speed = 2
                    self.s.stop()
            else:
                self.eattime = 0
                self.speed = 2
                self.s.stop()
                self.images = self.walkingimages

    def update(self, *args):
        if self.life > 0:
            self.image = self.images[args[0] % len(self.images)]
            if self.rect.left > -500:
                self.rect.left -= self.speed
        else:
            if not self.eattime == 0:
                self.s.stop()
            if self.bombsign == 0:
                if self.dietimes > 9:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.dieimages[self.dietimes]
                    self.dietimes += 1
            elif self.bombsign == 1:
                if self.dietimes > 19:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.bombdieimages[self.dietimes]
                    self.dietimes += 1

    def getCol(self):
        space = 25
        min = 0
        max = 0
        ans = 0
        for i in range(1, 10):
            if i != 1:
                space = 80
            min = min + space
            max = min + 80
            ans += 1
            if min <= self.rect.left + 80 <= max:
                return ans
        return 10


# 旗帜僵尸
class FlagZombie(pg.sprite.Sprite):
    def __init__(self):
        super(FlagZombie, self).__init__()
        self.image = pg.image.load("images/Zombies/FlagZombie/FlagZombie/FlagZombie_0.png").convert_alpha()
        self.images = [pg.image.load("images/Zombies/FlagZombie/FlagZombie/FlagZombie_{:d}.png".format(i)).convert_alpha() for i in range(0, 12)]
        self.dieimages = [pg.image.load('images/Zombies/NormalZombie/ZombieDie/ZombieDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 10)]
        self.attackimages = [pg.image.load('images/Zombies/FlagZombie/FlagZombieAttack/FlagZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in range(0, 11)]
        self.bombdieimages = [pg.image.load('images/Zombies/NormalZombie/BoomDie/BoomDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 20)]
        self.rect = self.images[0].get_rect()
        self.row = random.randint(1, 5)
        self.col = -1
        self.rect.top = 25 + (self.row - 1) * 100
        self.rect.left = 750
        self.speed = 2
        self.life = c.normal_life
        self.dietimes = 0
        self.bombsign = 0
        self.eattime = 0
        self.s = None

    def attacking(self, mapp):
        self.col = self.getCol()
        if self.col == 10:
            pass
        else:
            if not mapp.isEmpty(self.row-1, self.col-1):
                self.images = self.attackimages
                self.speed = 0
                if self.eattime == 0:
                    self.s = pg.mixer.Sound('sound/zombieAttack.ogg')
                    self.s.play(-1)
                mapp.plants[self.row-1][self.col-1].life -= 1
                self.eattime += 1
                if mapp.plants[self.row-1][self.col-1].life <= 0 or mapp.map[self.row-1][self.col-1] == 0:
                    mapp.map[self.row-1][self.col-1] = 0
                    self.eattime = 0
                    self.speed = 2
                    self.s.stop()
            else:
                self.images = [pg.image.load('images/Zombies/NormalZombie/Zombie/Zombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 22)]
                self.eattime = 0
                self.speed = 2
                self.s.stop()

    def update(self, *args):
        if self.life > 0:
            self.image = self.images[args[0] % len(self.images)]
            if self.rect.left > -500:
                self.rect.left -= self.speed
        else:
            if self.bombsign == 0:
                if self.dietimes > 9:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.dieimages[self.dietimes]
                    self.dietimes += 1
            elif self.bombsign == 1:
                if self.dietimes > 19:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.bombdieimages[self.dietimes]
                    self.dietimes += 1

    def getCol(self):
        space = 25
        min = 0
        max = 0
        ans = 0
        for i in range(1, 10):
            if i != 1:
                space = 80
            min = min + space
            max = min + 80
            ans += 1
            if min <= self.rect.left + 80 <= max:
                return ans
        return 10


class ConeheadZombie(pg.sprite.Sprite):
    def __init__(self):
        super(ConeheadZombie, self).__init__()
        self.image = pg.image.load("images/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_0.png").convert_alpha()
        self.images = [pg.image.load('images/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 21)]
        self.walkingimages = [pg.image.load('images/Zombies/ConeheadZombie/ConeheadZombie/ConeheadZombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 21)]
        self.dieimages = [pg.image.load('images/Zombies/NormalZombie/ZombieDie/ZombieDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 10)]
        self.attackimages = [pg.image.load('images/Zombies/ConeheadZombie/ConeheadZombieAttack/ConeheadZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in range(0, 11)]
        self.bombdieimages = [ pg.image.load('images/Zombies/NormalZombie/BoomDie/BoomDie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 20)]
        self.rect = self.images[0].get_rect()
        self.row = random.randint(1, 5)
        self.col = -1
        self.rect.top = 25 + (self.row - 1) * 100
        self.rect.left = 750
        self.speed = 2
        self.life = 200
        self.dietimes = 0
        self.bombsign = 0
        self.eattime = 0
        self.s = pg.mixer.Sound('sound/zombieAttack.ogg')

    def attacking(self, mapp):
        self.col = self.getCol()
        if self.col == 10:
            pass
        else:
            if not mapp.isEmpty(self.row-1, self.col-1):
                self.images = self.attackimages
                self.speed = 0
                if self.eattime == 0:
                    self.s = pg.mixer.Sound('sound/zombieAttack.ogg')
                    self.s.play(-1)
                mapp.plants[self.row-1][self.col-1].life -= 1
                self.eattime += 1
                if mapp.plants[self.row-1][self.col-1].life <= 0:
                    mapp.map[self.row-1][self.col-1] = 0
                    self.eattime = 0
                    self.speed = 2
                    self.s.stop()
            else:
                self.eattime = 0
                self.speed = 2
                self.s.stop()
                self.images = self.walkingimages

    def update(self, *args):
        if self.life > 0:
            self.image = self.images[args[0] % len(self.images)]
            if self.rect.left > -500:
                self.rect.left -= self.speed
        else:
            if not self.eattime == 0:
                self.s.stop()
            if self.bombsign == 0:
                if self.dietimes > 9:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.dieimages[self.dietimes]
                    self.dietimes += 1
            elif self.bombsign == 1:
                if self.dietimes > 19:
                    if self.dietimes > 24:
                        self.kill()
                    else:
                        self.dietimes += 1
                else:
                    self.image = self.bombdieimages[self.dietimes]
                    self.dietimes += 1

    def getCol(self):
        space = 25
        min = 0
        max = 0
        ans = 0
        for i in range(1, 10):
            if i != 1:
                space = 80
            min = min + space
            max = min + 80
            ans += 1
            if min <= self.rect.left + 80 <= max:
                return ans
        return 10


class BucketheadZombie(Zombie):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load("images/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_0.png").convert_alpha()
        self.images = [pg.image.load('images/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 15)]
        self.walkingimages = [pg.image.load('images/Zombies/BucketheadZombie/BucketheadZombie/BucketheadZombie_{:d}.png'.format(i)).convert_alpha() for i in range(0, 15)]
        self.attackimages = [pg.image.load('images/Zombies/BucketheadZombie/BucketheadZombieAttack/BucketheadZombieAttack_{:d}.png'.format(i)).convert_alpha() for i in range(0, 11)]
        self.life = 300