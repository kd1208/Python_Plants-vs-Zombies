import pygame as pg
import random


class SunFlower(pg.sprite.Sprite):  # 1. 太阳花
    def __init__(self, lasttime):
        super(SunFlower, self).__init__()
        self.image = pg.image.load('images/plants/SunFlower/SunFlower_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/SunFlower/SunFlower_{:d}.png'.format(i)).convert_alpha() for i in range(0, 18)]
        self.rect = self.images[0].get_rect()
        self.lasttime = lasttime
        self.life = 50

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        self.image = self.images[args[0] % len(self.images)]


class Peashooter(pg.sprite.Sprite):  # 2. 豌豆射手
    def __init__(self, q, p):
        super(Peashooter, self).__init__()
        self.image = pg.image.load("images/plants/Peashooter/Peashooter_0.png").convert_alpha()
        self.images = [pg.image.load("images/plants/Peashooter/Peashooter_{:d}.png".format(i)).convert_alpha() for i in range(0, 13)]
        self.rect = self.images[0].get_rect()
        self.row = q
        self.col = p
        self.life = 50

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        self.image = self.images[args[0] % len(self.images)]


class CherryBomb(pg.sprite.Sprite):  # 3. 樱桃炸弹
    def __init__(self, p, q):
        super(CherryBomb, self).__init__()
        self.image = pg.image.load("images/plants/CherryBomb/CherryBomb_0.png").convert_alpha()
        self.images = [pg.image.load("images/plants/CherryBomb/CherryBomb_{:d}.png".format(i)).convert_alpha() for i in range(0, 7)]
        self.rect = self.images[0].get_rect()
        self.row = q
        self.col = p
        self.time = 0

    def update(self, *args):
        if self.time < 7:
            self.image = self.images[args[0] % len(self.images)]
            self.time += 1
        else:
            if self.time == 7:
                self.image = pg.image.load("images/screen/Boom.png")
                self.rect.top -= 80
                self.rect.left -= 80
                sound = pg.mixer.Sound('sound/bomb.ogg')
                sound.play()
            elif self.time >= 14:
                self.kill()
            self.time += 1

    def bomb(self, zombieList, flagZombieList, mapp):
        for zombie in zombieList:
            zombie.col = zombie.getCol()
            if self.col - 1 <= zombie.col <= self.col + 1 and self.row - 1 <= zombie.row < self.row + 2:
                zombie.bombsign = 1
                zombie.life = 0
                if zombie.life <= 0 and zombie.dietimes == 0:
                    mapp.numzDec(zombie.row)
        for zombie in flagZombieList:
            zombie.col = zombie.getCol()
            if self.col - 1 <= zombie.col <= self.col + 1 and self.row - 1 <= zombie.row < self.row + 2:
                zombie.bombsign = 1
                zombie.life -= 100
                if zombie.life <= 0 and zombie.dietimes == 0:
                    mapp.numzDec(zombie.row)


class WallNut(pg.sprite.Sprite):  # 4. 坚果
    def __init__(self):
        super(WallNut, self).__init__()
        self.image = pg.image.load('images/plants/WallNut/WallNut/WallNut_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/WallNut/WallNut/WallNut_{:d}.png'.format(i)).convert_alpha() for i in range(0, 13)]
        self.crackedImgs1 = [pg.image.load('images/plants/WallNut/WallNut_cracked1/WallNut_cracked1_{:d}.png'.format(i)).convert_alpha() for i in range(0, 11)]
        self.crackedImgs2 = [pg.image.load('images/plants/WallNut/WallNut_cracked2/WallNut_cracked2_{:d}.png'.format(i)).convert_alpha() for i in range(0, 15)]
        self.rect = self.images[0].get_rect()
        self.life = 300

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        if self.life >= 200:
            pass
        elif 100 <= self.life < 200:
            self.images = self.crackedImgs1
        else:
            self.images = self.crackedImgs2
        self.image = self.images[args[0] % len(self.images)]


class PotatoMine(pg.sprite.Sprite):  # 5. 土豆地雷
    def __init__(self, q, p):
        super(PotatoMine, self).__init__()
        self.image = pg.image.load('images/plants/PotatoMine/PotatoMineInit/PotatoMineInit_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/PotatoMine/PotatoMine/PotatoMine_{:d}.png'.format(i)).convert_alpha() for i in range(0, 8)]
        self.explode = pg.image.load("images/plants/PotatoMine/PotatoMineExplode/PotatoMineExplode_0.png").convert_alpha()
        self.rect = self.images[0].get_rect()
        self.life = 100
        self.time = pg.time.get_ticks()
        self.bombtime = 0
        self.row = q
        self.col = p

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        if pg.time.get_ticks() - self.time >= 10 * 10**3 and self.bombtime == 0:
            self.image = self.images[args[0] % len(self.images)]
        if self.bombtime == 1:
            self.life -= 10

    def bomb(self, zombieList, flagZombieList, mapp):
        for zombie in zombieList:
            zombie.col = zombie.getCol()
            if self.col == zombie.col and self.row == zombie.row:
                self.bombtime = 1
                self.image = self.explode
                mapp.map[self.row-1][self.col-1] = 0
                zombie.bombsign = 1
                zombie.life = 0
                if zombie.life <= 0 and zombie.dietimes == 0:
                    sound = pg.mixer.Sound('sound/bomb.ogg')
                    sound.play()
                    mapp.numzDec(zombie.row)
        for zombie in flagZombieList:
            zombie.col = zombie.getCol()
            if self.col == zombie.col and self.row == zombie.row:
                self.bombtime += 1
                self.image = self.explode
                mapp.map[self.row - 1][self.col - 1] = 0
                zombie.bombsign = 1
                zombie.life -= 100
                if zombie.life <= 0 and zombie.dietimes == 0:
                    sound = pg.mixer.Sound('sound/bomb.ogg')
                    sound.play()
                    mapp.numzDec(zombie.row)


class SnowPea(pg.sprite.Sprite):  # 6. 寒冰豌豆射手
    def __init__(self, p):
        super(SnowPea, self).__init__()
        self.image = pg.image.load("images/plants/SnowPea/SnowPea_0.png").convert_alpha()
        self.images = [pg.image.load("images/plants/SnowPea/SnowPea_{:d}.png".format(i)).convert_alpha() for i in range(0, 15)]
        self.rect = self.images[0].get_rect()
        self.row = p
        self.life = 50


    def update(self, *args):
        if self.life <= 0:
            self.kill()
        self.image = self.images[args[0] % len(self.images)]


class Jalapeno(pg.sprite.Sprite):  # 7. 火爆辣椒
    def __init__(self, q):
        super(Jalapeno, self).__init__()
        self.image = pg.image.load("images/plants/Jalapeno/Jalapeno/Jalapeno_0.png").convert_alpha()
        self.images = [pg.image.load("images/plants/Jalapeno/Jalapeno/Jalapeno_{:d}.png".format(i)).convert_alpha() for i in range(0, 8)]
        self.fireimages = [pg.image.load("images/plants/Jalapeno/JalapenoExplode/JalapenoExplode_{:d}.png".format(i)).convert_alpha() for i in range(0, 3)]
        self.rect = self.images[0].get_rect()
        self.row = q
        self.time = 0

    def update(self, *args):
        if self.time < 7:
            self.image = self.images[args[0] % len(self.images)]
            self.time += 1
        else:
            if self.time == 7:
                self.images = self.fireimages
                self.rect.left = 25
                self.rect.top -= 60
                sound = pg.mixer.Sound('sound/bomb.ogg')
                sound.play()
            elif self.time >= 14:
                self.kill()
            self.image = self.images[args[0] % len(self.images)]
            self.time += 1

    def bomb(self, zombieList, flagZombieList, mapp):
        for zombie in zombieList:
            if zombie.row == self.row:
                zombie.bombsign = 1
                zombie.life = 0
                if zombie.life <= 0 and zombie.dietimes == 0:
                    mapp.numzDec(zombie.row)
        for zombie in flagZombieList:
            zombie.col = zombie.getCol()
            if zombie.row == self.row:
                zombie.bombsign = 1
                zombie.life -= 100
                if zombie.life <= 0 and zombie.dietimes == 0:
                    mapp.numzDec(zombie.row)


class RepeaterPea(pg.sprite.Sprite):  # 8. 双发豌豆射手
    def __init__(self, p):
        super(RepeaterPea, self).__init__()
        self.image = pg.image.load("images/plants/RepeaterPea/RepeaterPea_0.png").convert_alpha()
        self.images = [pg.image.load("images/plants/RepeaterPea/RepeaterPea_{:d}.png".format(i)).convert_alpha() for i in range(0, 15)]
        self.rect = self.images[0].get_rect()
        self.row = p
        self.sign = 0
        self.ctime = 0
        self.life = 50

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        self.image = self.images[args[0] % len(self.images)]

    def doubleBullets(self, bulletList, size):  # 发射第二个子弹
        if self.sign == 0:
            pass
        elif self.sign == 1:
            if pg.time.get_ticks() - self.ctime > 100:
                bullet = Bullet(self.rect, size, 0)
                bulletList.add(bullet)
                self.sign = 0


class TallNut(pg.sprite.Sprite):  # 9. 高坚果
    def __init__(self):
        super(TallNut, self).__init__()
        self.image = pg.image.load('images/plants/TallNut/TallNut/TallNut_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/TallNut/TallNut/TallNut_{:d}.png'.format(i)).convert_alpha() for i in range(0, 14)]
        self.crackedImgs1 = [pg.image.load('images/plants/TallNut/TallNut_cracked1/TallNut_cracked1_{:d}.png'.format(i)).convert_alpha() for i in range(0, 17)]
        self.crackedImgs2 = [pg.image.load('images/plants/TallNut/TallNut_cracked2/TallNut_cracked2_{:d}.png'.format(i)).convert_alpha() for i in range(0, 15)]
        self.rect = self.images[0].get_rect()
        self.life = 600

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        if self.life >= 400:
            pass
        elif 100 <= self.life < 400:
            self.images = self.crackedImgs1
        else:
            self.images = self.crackedImgs2
        self.image = self.images[args[0] % len(self.images)]


class TorchWood(pg.sprite.Sprite):  # 10. 火炬树桩
    def __init__(self):
        super(TorchWood, self).__init__()
        self.image = pg.image.load('images/plants/TorchWood/TorchWood_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/TorchWood/TorchWood_{:d}.png'.format(i)).convert_alpha() for i in range(0, 9)]
        self.rect = self.images[0].get_rect()
        self.life = 100

    def update(self, *args):
        if self.life <= 0:
            self.kill()
        self.image = self.images[args[0] % len(self.images)]


# 阳光
class Sun(pg.sprite.Sprite):
    def __init__(self, rect):
        super(Sun, self).__init__()
        self.image = pg.image.load('images/plants/Sun/Sun_0.png').convert_alpha()
        self.images = [pg.image.load('images/plants/Sun/Sun_{:d}.png'.format(i)).convert_alpha() for i in range(1, 18)]
        self.rect = self.images[0].get_rect()
        offsetTop = random.randint(-50, 50)
        offsetLeft = random.randint(-50, 50)

        self.rect.top = rect.top + offsetTop
        self.rect.left = rect.left + offsetLeft

    # 更新精灵的位置
    def update(self, *args):
        self.image = self.images[args[0] % len(self.images)]


# 子弹
class Bullet(pg.sprite.Sprite):
    def __init__(self, rect, bg_size, sign):
        super(Bullet, self).__init__()
        self.image = pg.image.load("images/Bullets/PeaNormal/PeaNormal_0.png")
        self.fire = [pg.image.load("images/Bullets/Fireball/Fireball_{:d}.png".format(i)).convert_alpha() for i in range(2)]
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size
        # 定义子弹的初始化位置
        self.rect.top = rect.top
        self.rect.left = rect.left + 50
        self.speed = 20
        self.ctime = pg.time.get_ticks()
        self.sign = sign  # 0:普通豌豆 1：冰豌豆 2：火豌豆

    def update(self, *args):
        if self.sign == 2:
            self.image = self.fire[args[0] % len(self.fire)]
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.kill()


class Car(pg.sprite.Sprite):
    def __init__(self, x, y, row):
        super(Car, self).__init__()
        self.image = pg.image.load("images/screen/car.png")
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.row = row
        self.speed = 0
        self.time = 0
        self.s = pg.mixer.Sound('sound/carWalking.ogg')

    def update(self, *args):
        if self.rect.left < 1200:
            self.rect.left += self.speed
            if self.time == 0 and not self.speed == 0:
                self.s.play()
                self.time += 1
        else:
            self.kill()
