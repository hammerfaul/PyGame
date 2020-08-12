from config import *

import pygame

class Base:
    def __init__(self, display, player, img, color):
        self.display = display
        self.img = img
        self.max_hp = base_hp
        self.hp = base_hp
        self.progress = 1
        self.color = color
        self.dmg = base_dmg
        self.gold = 1
        self.holz = 0
        self.nahrung = 0
        self.menschen = 0
        self.player = player

        # base
        self.base = pygame.image.load(img)
        self.base_breite = self.base.get_size()[0]
        self.base_hoehe = self.base.get_size()[1]

    def update(self):
        self.progress = self.hp / self.max_hp
        if self.hp < 0:
            self.hp = 0
        text = myfont.render(str(self.hp), False, (0, 0, 0))
        text_width = text.get_width()
        if self.player == 1:
            self.display.blit(self.base, (int(self.base_breite / 2), int(self.base_hoehe / 2)))
            if self.hp != 0:
                pygame.draw.rect(self.display, self.color,
                                 pygame.Rect(int(self.base_breite / 2), int(self.base_hoehe / 2),
                                             int(self.base_breite * self.progress),
                                             hpbar_height))
            pygame.draw.rect(self.display, (128, 128, 128),
                             pygame.Rect(int(self.base_breite / 2), int(self.base_hoehe / 2),
                                         int(self.base_breite),
                                         hpbar_height), 1)
            self.display.blit(text,
                              (int(self.base_breite / 2 + self.base_breite / 2 - text_width / 2),
                               int(self.base_hoehe / 2 - 1)))
        else:
            self.display.blit(self.base, (
                int(screen_width - self.base_breite * 3 / 2),
                int(screen_height - breite_unten - self.base_hoehe * 3 / 2)))
            if self.hp != 0:
                pygame.draw.rect(self.display, self.color,
                                 pygame.Rect(int(screen_width - self.base_breite * 3 / 2),
                                             int(screen_height - breite_unten - self.base_hoehe * 3 / 2),
                                             int(self.base_breite * self.progress),
                                             hpbar_height))
            pygame.draw.rect(self.display, (128, 128, 128), pygame.Rect(int(screen_width - self.base_breite * 3 / 2),
                                                                        int(
                                                                            screen_height - breite_unten - self.base_hoehe * 3 / 2),
                                                                        int(self.base_breite), hpbar_height), 1)
            self.display.blit(text,
                              (int(screen_width - self.base_breite * 3 / 2 + self.base_breite / 2 - text_width / 2),
                               int(screen_height - self.base_hoehe * 3 / 2 - 1 - breite_unten)))


class Spawn:
    def __init__(self, x, y, img, player, display, visible):
        self.schaden = 1
        self.x = x
        self.y = y
        self.hp = 5
        self.max_hp = 5
        self.progress = 1
        self.player = player
        self.display = display
        self.img = img
        self.visible = visible

        # HP Bar
        # Icon
        self.base = pygame.image.load(img)
        self.base = pygame.transform.scale(self.base, (50, 50))
        self.base_breite = self.base.get_size()[0]
        self.base_hoehe = self.base.get_size()[1]

    def update(self, x, y):
        self.progress = self.hp / self.max_hp
        if self.hp < 0:
            self.hp = 0
        if self.visible:
            self.display.blit(self.base, (int(x), int(y)))

    def visible(self, visible):
        self.visible = visible

