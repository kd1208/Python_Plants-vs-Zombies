import pygame as pg
import sys


def createMainMenu(gamechoose):
    size = 900, 600
    screen = pg.display.set_mode(size)
    MainMenu = pg.image.load("images/screen/MainMenu.png")
    adventure_0 = pg.image.load("images/screen/adventure_0.png")
    adventure_1 = pg.image.load("images/screen/adventure_1.png")
    littleGameButton_0 = pg.image.load("images/screen/littleGameButton_0.png")
    littleGameButton_1 = pg.image.load("images/screen/littleGameButton_1.png")
    exit_0 = pg.image.load("images/screen/exit_0.png")
    exit_1 = pg.image.load("images/screen/exit_1.png")
    adventure = adventure_0
    littleGameButton = littleGameButton_0
    exit = exit_0
    pg.display.set_caption("植物大战僵尸（杨佳泰出品）")
    logo = pg.image.load('images/pypvz.png').convert_alpha()
    pg.display.set_icon(logo)
    running = True
    pg.mixer.music.load("music/intro.opus")
    pg.mixer.music.play(-1)  # -1：循环播放

    while running:
        screen.blit(MainMenu, (0, 0))
        screen.blit(adventure, (475, 60))
        screen.blit(littleGameButton, (475, 180))
        screen.blit(exit, (810, 510))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.MOUSEMOTION:
                mouse = pg.mouse.get_pos()
                if (mouse[0] > 475 and mouse[0] < 475 + 331) and (mouse[1] > 60 and mouse[1] < 60 + 146):
                    adventure = adventure_1
                else:
                    adventure = adventure_0

                if (mouse[0] > 475 and mouse[0] < 475 + 331) and (mouse[1] > 180 and mouse[1] < 180 + 146):
                    littleGameButton = littleGameButton_1
                else:
                    littleGameButton = littleGameButton_0

                if (mouse[0] > 810 and mouse[0] < 810 + 47) and (mouse[1] > 510 and mouse[1] < 510 + 27):
                    exit = exit_1
                else:
                    exit = exit_0

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pos()
                if (mouse[0] > 475 and mouse[0] < 475 + 331) and (mouse[1] > 60 and mouse[1] < 60 + 146):
                    return 1

                if (mouse[0] > 475 and mouse[0] < 475 + 331) and (mouse[1] > 180 and mouse[1] < 180 + 146):
                    return 2
                if (mouse[0] > 810 and mouse[0] < 810 + 47) and (mouse[1] > 510 and mouse[1] < 510 + 27):
                    pg.quit()
                    sys.exit()

        pg.display.update()

    pg.mixer.music.stop()

class Panel():
    def __init__(self, card_list, sun_value):
        self.loadImages(sun_value)
        self.selected_cards = []
        self.selected_num = 0
        self.setupCards(card_list)

    def loadFrame(self, name):
        frame = tool.GFX[name]
        rect = frame.get_rect()
        frame_rect = (rect.x, rect.y, rect.w, rect.h)

        return tool.get_image(tool.GFX[name], *frame_rect, c.WHITE, 1)

    def loadImages(self, sun_value):
        self.menu_image = self.loadFrame(c.MENUBAR_BACKGROUND)
        self.menu_rect = self.menu_image.get_rect()
        self.menu_rect.x = 0
        self.menu_rect.y = 0

        self.panel_image = self.loadFrame(c.PANEL_BACKGROUND)
        self.panel_rect = self.panel_image.get_rect()
        self.panel_rect.x = 0
        self.panel_rect.y = c.PANEL_Y_START

        self.value_image = getSunValueImage(sun_value)
        self.value_rect = self.value_image.get_rect()
        self.value_rect.x = 21
        self.value_rect.y = self.menu_rect.bottom - 21

        self.button_image = self.loadFrame(c.START_BUTTON)
        self.button_rect = self.button_image.get_rect()
        self.button_rect.x = 155
        self.button_rect.y = 547

    def setupCards(self, card_list):
        self.card_list = []
        x = c.PANEL_X_START - c.PANEL_X_INTERNAL
        y = c.PANEL_Y_START + 43 - c.PANEL_Y_INTERNAL
        for i, index in enumerate(card_list):
            if i % 8 == 0:
                x = c.PANEL_X_START - c.PANEL_X_INTERNAL
                y += c.PANEL_Y_INTERNAL
            x += c.PANEL_X_INTERNAL
            self.card_list.append(Card(x, y, index, 0.5))

    def checkCardClick(self, mouse_pos):
        delete_card = None
        for card in self.selected_cards:
            if delete_card:  # when delete a card, move right cards to left
                card.rect.x -= c.BAR_CARD_X_INTERNAL
            elif card.checkMouseClick(mouse_pos):
                self.deleteCard(card.index)
                delete_card = card

        if delete_card:
            self.selected_cards.remove(delete_card)
            self.selected_num -= 1
            # 播放点击音效
            pg.mixer.Sound(
                os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "resources", "sound",
                             "tap.ogg")).play()

        if self.selected_num >= c.CARD_MAX_NUM:
            return

        for card in self.card_list:
            if card.checkMouseClick(mouse_pos):
                if card.canSelect():
                    self.addCard(card)
                    # 播放点击音效
                    pg.mixer.Sound(
                        os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "resources", "sound",
                                     "tap.ogg")).play()
                break

    def addCard(self, card):
        card.setSelect(False)
        y = 8
        x = 77 + self.selected_num * c.BAR_CARD_X_INTERNAL
        self.selected_cards.append(Card(x, y, card.index))
        self.selected_num += 1

    def deleteCard(self, index):
        self.card_list[index].setSelect(True)

    def checkStartButtonClick(self, mouse_pos):
        if self.selected_num < c.CARD_LIST_NUM:
            return False

        x, y = mouse_pos
        if (x >= self.button_rect.x and x <= self.button_rect.right and
                y >= self.button_rect.y and y <= self.button_rect.bottom):
            return True
        return False

    def getSelectedCards(self):
        card_index_list = []
        for card in self.selected_cards:
            card_index_list.append(card.index)
        return card_index_list

    def draw(self, surface):
        self.menu_image.blit(self.value_image, self.value_rect)
        surface.blit(self.menu_image, self.menu_rect)
        surface.blit(self.panel_image, self.panel_rect)
        for card in self.card_list:
            card.draw(surface)
        for card in self.selected_cards:
            card.draw(surface)

        if self.selected_num >= c.CARD_LIST_NUM:
            surface.blit(self.button_image, self.button_rect)