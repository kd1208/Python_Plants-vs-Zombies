import pygame as pg
from pygame.locals import *
from source import menu
from source import plants
from source import zombies
from source import constants as c
from source import map
import sys
import time


# 绘制卡片槽中的已经选择的植物
def drawPlantsCards(screen, plantsCards):
    x = 78
    for p in plantsCards:
        screen.blit(p, (x, 7))
        x += 51


# 选择植物界面
def selectPlants():
    size = 800, 600
    screen = pg.display.set_mode(size)
    running = True

    background = pg.image.load("images/background/Background_0.jpg")
    ChooserBackground = pg.image.load("images/screen/ChooserBackground.png")
    choosePlants = pg.image.load("images/screen/PanelBackground.png")
    plantsCards = []

    num = 0
    numMax = 10
    pg.mixer.music.load("music/chooseYourSeeds.opus")
    pg.mixer.music.play(-1)  # -1：循环播放
    clock = pg.time.Clock()

    text = "50"
    myfont = pg.font.SysFont("freesansbold.ttf", 30)
    sunNum = myfont.render(text, True, (0, 0, 0))

    while running:
        clock.tick(10)
        # 绘制各种背景元素
        screen.blit(background, (-220, 0))
        screen.blit(ChooserBackground, (0, 0))
        screen.blit(choosePlants, (0, 86))

        # 绘制下方选择植物卡片的区域
        screen.blit(sunNum, (30, 65))  # 阳光总数
        screen.blit(c.card_peashooter, (25, 130))
        screen.blit(c.card_sunFlower, (25 + 52, 130))
        screen.blit(c.card_cherrybomb, (25 + 52 * 2, 130))
        screen.blit(c.card_wallnut, (25 + 52 * 3, 130))
        screen.blit(c.card_potatomine, (25 + 52 * 4, 130))
        screen.blit(c.card_snowpea, (25 + 52 * 5, 130))
        screen.blit(c.card_jalapeno, (25 + 52 * 6, 130))
        screen.blit(c.card_repeaterpea, (25 + 52 * 7, 130))
        screen.blit(c.card_tallnut, (25, 130 + 72))
        screen.blit(c.card_torchwood, (25 + 52, 130 + 72))

        if num == numMax:
            screen.blit(c.StartButton, (155, 545))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                pressed_array = pg.mouse.get_pressed()
                if pressed_array[0]:
                    pos = pg.mouse.get_pos()

                    # 删除已选择的植物
                    space = 78
                    min = 0
                    max = 0
                    for index, card in enumerate(plantsCards):
                        if index != 0:
                            space = 51
                        min = min + space
                        max = min + 50
                        if min <= pos[0] <= max and 14 <= pos[1] <= 72:
                            del plantsCards[index]
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                            num -= 1

                    # 鼠标点击卡片槽， 选择植物
                    if 25 <= pos[0] <= 25 + 50 and 130 <= pos[1] <= 130 + 70:
                        if c.card_peashooter not in plantsCards:
                            plantsCards.append(c.card_peashooter)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 <= pos[0] <= 25 + 50 * 2 and 130 <= pos[1] <= 130 + 70:
                        if c.card_sunFlower not in plantsCards:
                            plantsCards.append(c.card_sunFlower)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 2 <= pos[0] <= 25 + 50 * 3 and 130 <= pos[1] <= 130 + 70:
                        if c.card_cherrybomb not in plantsCards:
                            plantsCards.append(c.card_cherrybomb)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 3 <= pos[0] <= 25 + 50 * 4 and 130 <= pos[1] <= 130 + 70:
                        if c.card_wallnut not in plantsCards:
                            plantsCards.append(c.card_wallnut)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 4 <= pos[0] <= 25 + 50 * 5 and 130 <= pos[1] <= 130 + 70:
                        if c.card_potatomine not in plantsCards:
                            plantsCards.append(c.card_potatomine)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 5 <= pos[0] <= 25 + 50 * 6 and 130 <= pos[1] <= 130 + 70:
                        if c.card_snowpea not in plantsCards:
                            plantsCards.append(c.card_snowpea)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 6 <= pos[0] <= 25 + 50 * 7 and 130 <= pos[1] <= 130 + 70:
                        if c.card_jalapeno not in plantsCards:
                            plantsCards.append(c.card_jalapeno)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 * 7 <= pos[0] <= 25 + 50 * 8 and 130 <= pos[1] <= 130 + 70:
                        if c.card_repeaterpea not in plantsCards:
                            plantsCards.append(c.card_repeaterpea)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 <= pos[0] <= 25 + 50 and 130 + 70 <= pos[1] <= 130 + 70 * 2:
                        if c.card_tallnut not in plantsCards:
                            plantsCards.append(c.card_tallnut)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()
                    elif 25 + 50 <= pos[0] <= 25 + 50 * 2 and 130 + 70 <= pos[1] <= 130 + 70 * 2:
                        if c.card_torchwood not in plantsCards:
                            plantsCards.append(c.card_torchwood)
                            num += 1
                            sound = pg.mixer.Sound('sound/tap.ogg')
                            sound.play()

                    # 选择完毕 开始游戏
                    elif 155 <= pos[0] <= 305 and 545 <= pos[1] <= 580:
                        if num == numMax:
                            running = False

        drawPlantsCards(screen, plantsCards)
        pg.display.update()
    pg.mixer.music.stop()
    return plantsCards


# 在游戏中 点击卡片槽的某个位置 判断选中的是什么植物
def choosePlant(plantsCards, x, y, choose, text):  # 游戏中选择植物
    space = 78
    min = 0
    max = 0
    if 613 <= x <= 650:  # 选中铲子
        return 999
    for index, card in enumerate(plantsCards):
        if index != 0:
            space = 51
        min = min + space
        max = min + 50
        if min <= x <= max and 7 <= y <= 77:
            if plantsCards[index] == c.card_sunFlower:  # 点中太阳花卡片
                if int(text) - 50 >= 0:
                    choose = 1
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_peashooter:  # 点中豌豆射手卡片
                if int(text) - 100 >= 0:
                    choose = 2
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_cherrybomb:  # 点中樱桃炸弹卡片
                if int(text) - 150 >= 0:
                    choose = 3
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_wallnut:  # 点中坚果卡片
                if int(text) - 50 >= 0:
                    choose = 4
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_potatomine:  # 点中坚果卡片
                if int(text) - 25 >= 0:
                    choose = 5
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_snowpea:  # 点中寒冰豌豆射手卡片
                if int(text) - 175 >= 0:
                    choose = 6
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_jalapeno:  # 点中火爆辣椒卡片
                if int(text) - 125 >= 0:
                    choose = 7
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_repeaterpea:  # 点中双发豌豆射手卡片
                if int(text) - 200 >= 0:
                    choose = 8
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_tallnut:  # 点中高坚果卡片
                if int(text) - 125 >= 0:
                    choose = 9
                    return choose
                else:
                    return 0
            elif plantsCards[index] == c.card_torchwood:  # 点中火炬树桩卡片
                if int(text) - 125 >= 0:
                    choose = 10
                    return choose
                else:
                    return 0


# 在游戏中 被选中的植物跟随鼠标移动 等待种植
def cardMove(choose, screen):
    pos = pg.mouse.get_pos()
    if choose == 1:
        screen.blit(c.sunFlowerImg, (pos[0] - 25, pos[1] - 35))
    if choose == 2:
        screen.blit(c.peashooterImg, (pos[0] - 25, pos[1] - 35))
    if choose == 3:
        screen.blit(c.cherrybombImg, (pos[0] - 25, pos[1] - 35))
    if choose == 4:
        screen.blit(c.wallnutImg, (pos[0] - 25, pos[1] - 35))
    if choose == 5:
        screen.blit(c.potatomineImg, (pos[0] - 25, pos[1] - 35))
    if choose == 6:
        screen.blit(c.snowpeaImg, (pos[0] - 25, pos[1] - 35))
    if choose == 7:
        screen.blit(c.jalapenoImg, (pos[0] - 25, pos[1] - 35))
    if choose == 8:
        screen.blit(c.repeaterpeaImg, (pos[0] - 25, pos[1] - 35))
    if choose == 9:
        screen.blit(c.card_tallnutImg, (pos[0] - 25, pos[1] - 35))
    if choose == 10:
        screen.blit(c.card_torchwoodImg, (pos[0] - 25, pos[1] - 35))
    if choose == 999:
        screen.blit(c.shovel, (pos[0] - 25, pos[1] - 35))


# 使用铲子挖掘种植在地图上的植物
def useShovel(mapp, q, p):
    if mapp.map[q-1][p-1] == 1:
        mapp.map[q-1][p-1] = 0
        mapp.plants[q-1][p-1].kill()
        sound = pg.mixer.Sound('sound/tangleKelpDrag.ogg')
        sound.play()


# 游戏中的小菜单
def littleMenuChoose(screen):
    running = True
    bigMenu = pg.image.load("images/screen/bigMenu.png")
    returnButton = pg.image.load("images/screen/returnButton.png")
    mainMenuButton = pg.image.load("images/screen/mainMenuButton.png")
    runsign = True
    while runsign:
        screen.blit(bigMenu, (150, 40))
        screen.blit(returnButton, (220, 440))
        screen.blit(mainMenuButton, (280, 370))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                pressed_array = pg.mouse.get_pressed()
                if pressed_array[0]:
                    pos = pg.mouse.get_pos()
                    print(pos)

                    if 220 <= pos[0] <= 220 + 340 and 440 <= pos[1] <= 440 + 90:
                        runsign = False
                        return True
                    elif 280 <= pos[0] <= 280 + 200 and 370 <= pos[1] <= 370 + 40:
                        running = False
                        runsign = False
                        return running

        pg.display.update()


# 判断植物所在行是否存在僵尸
def ifHaveZombie(row, zombieList):
    for zombie in zombieList:
        if zombie.row == row:
            return True
    return False


# Map_1 ： 白天-草地
def Map_1():
    plantsCards = selectPlants()
    map1 = map.Map(9, 5)

    size = 800, 600
    screen = pg.display.set_mode(size)
    background = pg.image.load("images/background/Background_0.jpg")

    victory = pg.image.load("images/screen/GameVictory.png")
    lose = pg.image.load("images/screen/GameLoose.png")
    ChooserBackground = pg.image.load("images/screen/ChooserBackground.png")
    littleMenu = pg.image.load("images/screen/littleMenu.png")
    shovelBox = pg.image.load("images/screen/shovelBox.png")
    LevelProgressBar = pg.image.load("images/screen/LevelProgressBar.png")

    text = "5000"
    myfont = pg.font.SysFont("freesansbold.ttf", 30)
    sunNum = myfont.render(text, True, (0, 0, 0))

    # 各类元素列表
    sunList = pg.sprite.Group()           # 阳光列表
    sunFlowerList = pg.sprite.Group()     # 太阳花列表
    peashooterList = pg.sprite.Group()    # 豌豆射手列表
    wallnutList = pg.sprite.Group()       # 坚果列表
    repeaterpeaList = pg.sprite.Group()   # 双发豌豆射手列表
    snowpeaList = pg.sprite.Group()       # 寒冰豌豆射手列表
    jalapenoList = pg.sprite.Group()      # 火爆辣椒列表
    cherrybombList = pg.sprite.Group()    # 樱桃炸弹列表
    tallnutList = pg.sprite.Group()       # 高坚果列表
    potatomineList = pg.sprite.Group()    # 土豆地雷列表
    torchwoodList = pg.sprite.Group()    # 火炬树桩列表

    bulletList = pg.sprite.Group()          # 植物子弹列表
    zombieList = pg.sprite.Group()          # 僵尸列表
    flagZombieList = pg.sprite.Group()      # 旗帜僵尸列表
    coneheadzombieList = pg.sprite.Group()  # 路障僵尸列表

    carList = pg.sprite.Group()
    carList.add(plants.Car(-30, 110, 1))
    carList.add(plants.Car(-30, 210, 2))
    carList.add(plants.Car(-30, 310, 3))
    carList.add(plants.Car(-30, 410, 4))
    carList.add(plants.Car(-30, 510, 5))

    GENERATOR_SUN_EVENT = pg.USEREVENT + 1
    pg.time.set_timer(GENERATOR_SUN_EVENT, 1 * 10**3)

    GENERATOR_ZOMBIE1_EVENT = pg.USEREVENT + 2
    pg.time.set_timer(GENERATOR_ZOMBIE1_EVENT, 10 * 10**3)

    GENERATOR_PEASHOOTER_EVENT = pg.USEREVENT + 3
    pg.time.set_timer(GENERATOR_PEASHOOTER_EVENT, 2 * 10**3)

    GENERATOR_FLAGZOMBIE_EVENT = pg.USEREVENT + 4
    pg.time.set_timer(GENERATOR_FLAGZOMBIE_EVENT, 120 * 10**3)

    GENERATOR_ZOMBIE2_EVENT = pg.USEREVENT + 5
    pg.time.set_timer(GENERATOR_ZOMBIE2_EVENT, 5 * 10**3)

    GENERATOR_ConeheadZombie_EVENT = pg.USEREVENT + 6
    pg.time.set_timer(GENERATOR_ConeheadZombie_EVENT, 5 * 10 ** 3)

    GENERATOR_BucketheadZombie_EVENT = pg.USEREVENT + 7
    pg.time.set_timer(GENERATOR_BucketheadZombie_EVENT, 8 * 10 ** 3)


    index = 0
    choose = 0
    clock = pg.time.Clock()

    pg.mixer.music.load("music/dayLevel.opus")
    pg.mixer.music.play(-1)  # -1：循环播放
    running = True
    gametime = pg.time.get_ticks()
    gamestate = 1
    while running:
        if index > 100:
            index = 0
        clock.tick(15)

        # 绘制场景
        screen.blit(background, (-220, 0))          # 草坪
        screen.blit(ChooserBackground, (0, 0))     # 卡片槽
        screen.blit(sunNum, (25, 65))               # 阳光总数
        screen.blit(shovelBox, (613, 0))            # 铲子收纳盒
        screen.blit(c.shovel, (613, 0))               # 铲子
        screen.blit(littleMenu, (690, 0))           # 小菜单

        # 绘制进度条
        screen.blit(LevelProgressBar, (600, 575))

        # 绘制顶部植物卡片
        drawPlantsCards(screen, plantsCards)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            # 太阳花生成阳光
            elif event.type == GENERATOR_SUN_EVENT:
                if len(sunFlowerList) > 0:
                    timeNow = time.time()
                    for sunFlower in sunFlowerList:
                        if timeNow - sunFlower.lasttime >= 5:
                            sun = plants.Sun(sunFlower.rect)
                            sunList.add(sun)
                            sunFlower.lasttime = timeNow

            # 豌豆类的植物发射子弹
            elif event.type == GENERATOR_PEASHOOTER_EVENT:
                if len(peashooterList) + len(repeaterpeaList) + len(snowpeaList) > 0:
                    for peashooter in peashooterList:  # 豌豆射手发射子弹
                        if map1.num_z[peashooter.row - 1] > 0 or ifHaveZombie(peashooter.row, zombieList):
                            bullet = plants.Bullet(peashooter.rect, size, 0)
                            bulletList.add(bullet)
                    for repeaterpea in repeaterpeaList:  # 双发豌豆射手发射子弹
                        if map1.num_z[repeaterpea.row - 1] > 0 or ifHaveZombie(repeaterpea.row, zombieList):
                            bullet = plants.Bullet(repeaterpea.rect, size, 0)
                            bulletList.add(bullet)
                            repeaterpea.sign = 1
                            repeaterpea.ctime = pg.time.get_ticks()
                            repeaterpea.doubleBullets(bulletList, size)
                    for snowpea in snowpeaList:  # 豌豆射手发射子弹
                        if map1.num_z[snowpea.row - 1] > 0 or ifHaveZombie(snowpea.row, zombieList):
                            bullet = plants.Bullet(snowpea.rect, size, 1)
                            bullet.image = pg.image.load('images/Bullets/PeaIce/PeaIce_0.png').convert_alpha()
                            bulletList.add(bullet)

            # 生成僵尸
            if event.type == GENERATOR_ZOMBIE1_EVENT and gamestate == 1:
                zombie = zombies.Zombie()
                zombieList.add(zombie)
                map1.numzAdd(zombie.row)
                if gametimenow <= 11 * 10**3:
                    sound = pg.mixer.Sound('sound/zombieComing.ogg')
                    sound.play()

            if event.type == GENERATOR_ZOMBIE2_EVENT and 2 <= gamestate <= 4:
                zombie = zombies.Zombie()
                zombieList.add(zombie)
                map1.numzAdd(zombie.row)

            if event.type == GENERATOR_ConeheadZombie_EVENT and 3 <= gamestate <= 4:
                coneheadzombie = zombies.ConeheadZombie()
                zombieList.add(coneheadzombie)
                map1.numzAdd(coneheadzombie.row)

            if event.type == GENERATOR_BucketheadZombie_EVENT and gamestate == 4:
                coneheadzombie = zombies.BucketheadZombie()
                zombieList.add(coneheadzombie)
                map1.numzAdd(coneheadzombie.row)

            # 生成旗帜僵尸
            if event.type == GENERATOR_FLAGZOMBIE_EVENT:
                gamestate = 5
                sound = pg.mixer.Sound('sound/hugeWaveApproching.ogg')
                sound.play()
                flagZombie = zombies.FlagZombie()
                flagZombieList.add(flagZombie)
                map1.numzAdd(flagZombie.row)
                for i in range(7):
                    zombie = zombies.Zombie()
                    zombieList.add(zombie)
                    map1.numzAdd(zombie.row)
                for i in range(6):
                    zombie = zombies.ConeheadZombie()
                    zombieList.add(zombie)
                    map1.numzAdd(zombie.row)
                for i in range(3):
                    zombie = zombies.BucketheadZombie()
                    zombieList.add(zombie)
                    map1.numzAdd(zombie.row)

            # 处理各类鼠标点击事件
            elif event.type == pg.MOUSEBUTTONDOWN:
                pressed_array = pg.mouse.get_pressed()
                if pressed_array[0]:
                    pos = pg.mouse.get_pos()
                    print(pos)

                    # 点击小菜单
                    if 690 < pos[0] < 800 and 0 < pos[1] < 30:
                        running = littleMenuChoose(screen)

                    # 鼠标点击卡片槽，选择植物，给choose赋值
                    if (78 < pos[0] < 590 or 613 < pos[0] < 650) and 0 < pos[1] < 75:
                        choose = choosePlant(plantsCards, pos[0], pos[1], choose, text)
                        if not choose == 0:
                            sound = pg.mixer.Sound('sound/clickCard.ogg')
                            sound.play()

                    # 将植物种植到草坪上
                    if 0 < pos[0] < 1200 and 70 < pos[1] < 600:
                        if not choose == 0:
                            x, y, p, q = map1.location(pos[0], pos[1])
                            if map1.map[q - 1][p - 1] == 0:
                                sound = pg.mixer.Sound('sound/plant.ogg')
                                sound.play()
                                if choose == 1:  # 种植太阳花
                                    sunFlower = plants.SunFlower(time.time())
                                    sunFlower.rect.top = y - 35
                                    sunFlower.rect.left = x - 25
                                    sunFlowerList.add(sunFlower)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = sunFlower
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 50)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 2:  # 种植豌豆射手
                                    peashooter = plants.Peashooter(q, p)
                                    peashooter.rect.top = y - 35
                                    peashooter.rect.left = x - 25
                                    peashooterList.add(peashooter)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = peashooter
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 100)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 3:  # 种植樱桃炸弹
                                    cherrybomb = plants.CherryBomb(p, q)
                                    cherrybomb.rect.top = y - 35
                                    cherrybomb.rect.left = x - 25
                                    cherrybombList.add(cherrybomb)
                                    # map1.map[q - 1][p - 1] = 1
                                    # map1.plants[q - 1][p - 1] = cherrybomb
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 150)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 4:  # 种植坚果
                                    wallnut = plants.WallNut()
                                    wallnut.rect.top = y - 35
                                    wallnut.rect.left = x - 25
                                    wallnutList.add(wallnut)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = wallnut
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 50)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 5:  # 种植土豆地雷
                                    potatomine = plants.PotatoMine(q, p)
                                    potatomine.rect.top = y - 35
                                    potatomine.rect.left = x - 25
                                    potatomineList.add(potatomine)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = potatomine
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 25)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 6:  # 种植寒冰豌豆射手
                                    snowpea = plants.SnowPea(q)
                                    snowpea.rect.top = y - 35
                                    snowpea.rect.left = x - 25
                                    snowpeaList.add(snowpea)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = snowpea
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 175)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 7:  # 种植火爆辣椒
                                    jalapeno = plants.Jalapeno(q)
                                    jalapeno.rect.top = y - 35
                                    jalapeno.rect.left = x - 25
                                    jalapenoList.add(jalapeno)
                                    # map1.map[q - 1][p - 1] = 1
                                    # map1.plants[q - 1][p - 1] = jalapeno
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 125)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 8:  # 种植双发豌豆射手
                                    repeaterpea = plants.RepeaterPea(q)
                                    repeaterpea.rect.top = y - 35
                                    repeaterpea.rect.left = x - 25
                                    repeaterpeaList.add(repeaterpea)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = repeaterpea
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 200)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 9:  # 种植高坚果
                                    tallnut = plants.TallNut()
                                    tallnut.rect.top = y - 70
                                    tallnut.rect.left = x - 25
                                    tallnutList.add(tallnut)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = tallnut
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 200)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                                if choose == 10:  # 种植火炬树桩
                                    torchwood = plants.TorchWood()
                                    torchwood.rect.top = y - 40
                                    torchwood.rect.left = x - 25
                                    torchwoodList.add(torchwood)
                                    map1.map[q - 1][p - 1] = 1
                                    map1.plants[q - 1][p - 1] = torchwood
                                    choose = 0

                                    # 扣去对应的阳光
                                    text = str(int(text) - 125)
                                    myfont = pg.font.SysFont("freesansbold.ttf", 30)
                                    sunNum = myfont.render(text, True, (0, 0, 0))

                            else:
                                if choose == 999:  # 使用铲子
                                    print(q, p)
                                    useShovel(map1, q, p)
                                choose = 0

                    # 鼠标点击阳光
                    for sun in sunList:
                        if sun.rect.collidepoint((pos[0], pos[1])):
                            sound = pg.mixer.Sound('sound/collectSun.ogg')
                            sound.play()
                            sunList.remove(sun)
                            sun.is_click = True
                            text = str(int(text) + 25)
                            myfont = pg.font.SysFont("freesansbold.ttf", 30)
                            sunNum = myfont.render(text, True, (0, 0, 0))

        # 点击顶部植物卡槽后 植物跟随鼠标移动
        cardMove(choose, screen)

        # 子弹碰到火炬树桩变成火焰子弹
        for bullet in bulletList:
            for torchwood in torchwoodList:
                if pg.sprite.collide_mask(bullet, torchwood):
                    bullet.sign = 2

        # 子弹击中普通僵尸
        for bullet in bulletList:
            for zombie in zombieList:
                if pg.sprite.collide_mask(bullet, zombie):
                    peaBoom = pg.image.load("images/Bullets/PeaNormalExplode/PeaNormalExplode_0.png")
                    screen.blit(peaBoom, (zombie.rect.left + 80, zombie.rect.top + 70))
                    if bullet.sign == 2:
                        sound = pg.mixer.Sound('sound/firepea.ogg')
                        sound.play()
                        zombie.life -= 20
                    else:
                        sound = pg.mixer.Sound('sound/bulletExplode.ogg')
                        sound.play()
                        zombie.life -= 10
                    if bullet.sign == 1:
                        zombie.speed = 0.1
                    bulletList.remove(bullet)
                    if zombie.life <= 0 and zombie.dietimes == 0:
                        map1.numzDec(zombie.row)

        # 子弹击中旗帜僵尸
        for bullet in bulletList:
            for flagZombie in flagZombieList:
                if pg.sprite.collide_mask(bullet, flagZombie):
                    peaBoom = pg.image.load("images/Bullets/PeaNormalExplode/PeaNormalExplode_0.png")
                    screen.blit(peaBoom, (flagZombie.rect.left + 80, flagZombie.rect.top + 70))
                    sound = pg.mixer.Sound('sound/bulletExplode.ogg')
                    sound.play()
                    flagZombie.life -= 10
                    if bullet.sign == 1:
                        flagZombie.speed = 0.1
                    bulletList.remove(bullet)
                    if flagZombie.life <= 0 and flagZombie.dietimes == 0:
                        map1.numzDec(flagZombie.row)

        # 双发豌豆射手发射第二课子弹
        for repeaterpea in repeaterpeaList:
            repeaterpea.doubleBullets(bulletList, size)

        # 樱桃炸弹爆炸
        for cherrybomb in cherrybombList:
            if cherrybomb.time == 7:
                cherrybomb.bomb(zombieList, flagZombieList, map1)

        # 火爆辣椒爆炸
        for jalapeno in jalapenoList:
            if jalapeno.time == 7:
                jalapeno.bomb(zombieList, flagZombieList, map1)

        # 土豆地雷爆炸
        for potatomine in potatomineList:
            potatomine.bomb(zombieList, flagZombieList, map1)

        # 僵尸吃植物
        for zombie in zombieList:
            zombie.attacking(map1)

        # 小推车碾压僵尸
        for car in carList:
            for zombie in zombieList:
                if car.row == zombie.row and pg.sprite.collide_rect(car, zombie):
                    car.speed = 15
                    zombie.life -= 100
                    if zombie.life <= 0 and zombie.dietimes == 0:
                        map1.numzDec(zombie.row)
            for zombie in flagZombieList:
                if car.row == zombie.row and pg.sprite.collide_rect(car, zombie):
                    car.speed = 15
                    zombie.life -= 100
                    if zombie.life <= 0 and zombie.dietimes == 0:
                        map1.numzDec(zombie.row)

        # 更新
        sunFlowerList.update(index)
        sunFlowerList.draw(screen)
        sunList.update(index)
        sunList.draw(screen)
        zombieList.update(index)
        zombieList.draw(screen)
        peashooterList.update(index)
        peashooterList.draw(screen)
        repeaterpeaList.update(index)
        repeaterpeaList.draw(screen)
        snowpeaList.update(index)
        snowpeaList.draw(screen)
        wallnutList.update(index)
        wallnutList.draw(screen)
        cherrybombList.update(index)
        cherrybombList.draw(screen)
        tallnutList.update(index)
        tallnutList.draw(screen)
        jalapenoList.update(index)
        jalapenoList.draw(screen)
        potatomineList.update(index)
        potatomineList.draw(screen)
        torchwoodList.update(index)
        torchwoodList.draw(screen)

        bulletList.update(index)
        bulletList.draw(screen)
        flagZombieList.update(index)
        flagZombieList.draw(screen)

        carList.update(index)
        carList.draw(screen)

        gametimenow = pg.time.get_ticks() - gametime
        if gamestate == 5:
            if map1.num_z[0] + map1.num_z[1] + map1.num_z[2] + map1.num_z[3] + map1.num_z[4] <= 0:
                size = 750, 550
                screen = pg.display.set_mode(size)
                pg.mixer.music.stop()
                sound = pg.mixer.Sound('sound/win.ogg')
                sound.play()
                screen.blit(victory, (-10, -10))
                pg.display.update()
                time.sleep(4)
                running = False
        else:
            if gametimenow >= 20 * 10 ** 3:
                gamestate = 2
                if gametimenow >= 40 * 10 ** 3:
                    gamestate = 3
                    if gametimenow >= 85 * 10 ** 3:
                        gamestate = 4

        for zombie in zombieList:
            if zombie.rect.left == -30:
                size = 750, 550
                screen = pg.display.set_mode(size)
                pg.mixer.music.stop()
                s = pg.mixer.Sound('sound/scream.ogg')
                s.play()
                sound = pg.mixer.Sound('sound/lose.ogg')
                sound.play()
                screen.blit(lose, (-10, -10))
                pg.display.update()
                time.sleep(4)
                running = False

        index += 1
        print(map1.num_z[0] + map1.num_z[1] + map1.num_z[2] + map1.num_z[3] + map1.num_z[4], gamestate)
        pg.display.update()
    pg.mixer.music.stop()


def createGrave(mapp):
    pass


def createLittleGame():
    map2 = map.Map(9, 5)
    size = 800, 600
    screen = pg.display.set_mode(size)
    background = pg.image.load("images/background/Background_1.jpg")
    littleMenu = pg.image.load("images/screen/littleMenu.png")

    carList = pg.sprite.Group()
    carList.add(plants.Car(-30, 110, 1))
    carList.add(plants.Car(-30, 210, 2))
    carList.add(plants.Car(-30, 310, 3))
    carList.add(plants.Car(-30, 410, 4))
    carList.add(plants.Car(-30, 510, 5))

    index = 0
    clock = pg.time.Clock()

    pg.mixer.music.load("music/dayLevel.opus")
    pg.mixer.music.play(-1)  # -1：循环播放

    createGrave(map2)
    running = True
    while running:
        if index > 100:
            index = 0
        clock.tick(15)

        # 绘制场景
        screen.blit(background, (-220, 0))  # 草坪
        # screen.blit(sunNum, (30, 65))  # 阳光总数
        # screen.blit(shovelBox, (613, 0))  # 铲子收纳盒
        # screen.blit(shovel, (613, 0))  # 铲子
        screen.blit(littleMenu, (690, 0))  # 小菜单

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        carList.update(index)
        carList.draw(screen)

        pg.display.update()
    pg.mixer.music.stop()


# 主函数 包含游戏菜单逻辑
def main():
    gamechoose = 0
    pg.init()
    while True:
        gamechoose = menu.createMainMenu(gamechoose)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

        if gamechoose == 1:
            Map_1()
        elif gamechoose == 2:
            createLittleGame()


if __name__ == '__main__':
    main()
