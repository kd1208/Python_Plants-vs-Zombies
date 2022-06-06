# 游戏常量文件
import pygame as pg
import os

# 铲子
shovel = pg.image.load("images/screen/shovel.png")

# 地图相关像素数据
MAP_OFFSET_X = 35
MAP_OFFSET_Y = 100
MAP_EMPTY = 0
MAP_EXIST = 1
# 方格数据
GRID_X_LEN = 9
GRID_Y_LEN = 5
GRID_X_SIZE = 80
GRID_Y_SIZE = 100

# 植物卡片 + 植物图片
# 1. 豌豆射手 peashooter
card_peashooter = pg.image.load("images/Cards/card_peashooter.png")
card_peashooter = pg.transform.smoothscale(card_peashooter, (50, 70))
sunFlowerImg = pg.image.load('images/plants/SunFlower/SunFlower_0.png')

# 2. 太阳花 sunFlower
card_sunFlower = pg.image.load("images/Cards/card_sunflower.png")
card_sunFlower = pg.transform.smoothscale(card_sunFlower, (50, 70))
peashooterImg = pg.image.load('images/plants/Peashooter/Peashooter_0.png')

# 3. 樱桃炸弹 cherrybomb
card_cherrybomb = pg.image.load("images/Cards/card_cherrybomb.png")
card_cherrybomb = pg.transform.smoothscale(card_cherrybomb, (50, 70))
cherrybombImg = pg.image.load('images/plants/CherryBomb/CherryBomb_0.png')

# 4. 坚果墙 wallnut
card_wallnut = pg.image.load("images/Cards/card_wallnut.png")
card_wallnut = pg.transform.smoothscale(card_wallnut, (50, 70))
wallnutImg = pg.image.load('images/plants/WallNut/WallNut/WallNut_0.png')

# 5. 土豆雷 potatomine
card_potatomine = pg.image.load("images/Cards/card_potatomine.png")
card_potatomine = pg.transform.smoothscale(card_potatomine, (50, 70))
potatomineImg = pg.image.load('images/plants/PotatoMine/PotatoMineInit/PotatoMineInit_0.png')

# 6. 寒冰射手 snowpea
card_snowpea = pg.image.load("images/Cards/card_snowpea.png")
card_snowpea = pg.transform.smoothscale(card_snowpea, (50, 70))
snowpeaImg = pg.image.load('images/plants/SnowPea/SnowPea_0.png')

# 7. 火爆辣椒
card_jalapeno = pg.image.load("images/Cards/card_jalapeno.png")
card_jalapeno = pg.transform.smoothscale(card_jalapeno, (50, 70))
jalapenoImg = pg.image.load('images/plants/Jalapeno/Jalapeno/Jalapeno_0.png')

# 8. 双发射手 repeaterpea
card_repeaterpea = pg.image.load("images/Cards/card_repeaterpea.png")
card_repeaterpea = pg.transform.smoothscale(card_repeaterpea, (50, 70))
repeaterpeaImg = pg.image.load('images/plants/RepeaterPea/RepeaterPea_0.png')

# 9. 高坚果
card_tallnut = pg.image.load("images/Cards/card_tallnut.png")
card_tallnut = pg.transform.smoothscale(card_tallnut, (50, 70))
card_tallnutImg = pg.image.load('images/plants/TallNut/TallNut/TallNut_0.png')

# 10. 火炬树桩
card_torchwood = pg.image.load("images/Cards/card_torchwood.png")
card_torchwood = pg.transform.smoothscale(card_torchwood, (50, 70))
card_torchwoodImg = pg.image.load('images/plants/TorchWood/TorchWood_0.png')

# 其它
# 窝瓜 squash
card_squash = pg.image.load("images/Cards/card_squash.png")
card_squash = pg.transform.smoothscale(card_squash, (50, 70))
# 食人花 chomper
card_chomper = pg.image.load("images/Cards/card_chomper.png")
card_chomper = pg.transform.smoothscale(card_chomper, (50, 70))

# 选植物界面的开始游戏按钮
StartButton = pg.image.load("images/Screen/StartButton.png")


# 僵尸生命值
normal_life = 100

# 僵尸防具
armor_0 = 0
armor_1 = 50
armor_2 = 100

# 无穷大常量
INF = float('inf')


