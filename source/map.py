class Map:
    def __init__(self, width, height):
        self.w = width
        self.h = height
        self.map = [[0 for x in range(self.w)] for y in range(self.h)]
        self.plants = [[None for x in range(self.w)] for y in range(self.h)]
        self.num_z = [0 for x in range(self.h)]

    def isEmpty(self, x, y):  # 检查某个格子是否已经安放植物
        if self.map[x][y] == 0:
            return True
        else:
            return False

    def location(self, x, y):  # 返回格子的坐标
        ans_x = 0
        ans_y = 0
        space = 25
        min = 0
        max = 0
        for i in range(1, 10):
            if i != 1:
                space = 80
            min = min + space
            max = min + 80
            ans_x += 1
            if min <= x <= max:
                space1 = 80
                min1 = 0
                max1 = 0
                for j in range(1, 6):
                    if j != 1:
                        space1 = 100
                    min1 = min1 + space1
                    max1 = min1 + 100
                    ans_y += 1
                    if min1 <= y <= max1:
                        return (min + max) / 2, (min1 + max1) / 2, ans_x, ans_y

    def numzAdd(self, row):
        self.num_z[row-1] += 1

    def numzDec(self, row):
        self.num_z[row - 1] -= 1




    # def isValid(self, map_x, map_y):
    #     if (map_x < 0 or map_x >= self.width or
    #             map_y < 0 or map_y >= self.height):
    #         return False
    #     return True
    #
    # def isMovable(self, map_x, map_y):
    #     return (self.map[map_y][map_x] == c.MAP_EMPTY)
    #
    # def getMapIndex(self, x, y):
    #     x -= c.MAP_OFFSET_X
    #     y -= c.MAP_OFFSET_Y
    #     return (x // c.GRID_X_SIZE, y // c.GRID_Y_SIZE)
    #
    # def getMapGridPos(self, map_x, map_y):
    #     return (map_x * c.GRID_X_SIZE + c.GRID_X_SIZE // 2 + c.MAP_OFFSET_X,
    #             map_y * c.GRID_Y_SIZE + c.GRID_Y_SIZE // 5 * 3 + c.MAP_OFFSET_Y)
    #
    # def setMapGridType(self, map_x, map_y, type):
    #     self.map[map_y][map_x] = type
    #
    # def getRandomMapIndex(self):
    #     map_x = random.randint(0, self.width - 1)
    #     map_y = random.randint(0, self.height - 1)
    #     return (map_x, map_y)
    #
    # def showPlant(self, x, y):
    #     pos = None
    #     map_x, map_y = self.getMapIndex(x, y)
    #     if self.isValid(map_x, map_y) and self.isMovable(map_x, map_y):
    #         pos = self.getMapGridPos(map_x, map_y)
    #     return pos
