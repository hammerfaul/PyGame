from config import *

import pygame
import math

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
        self.holz = 1
        self.nahrung = 1
        self.menschen = 1
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
            self.x = int(self.base_breite / 2)
            self.y = int(self.base_hoehe / 2)
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
            self.x = int(screen_width - self.base_breite * 3 / 2)
            self.y = int(screen_height - breite_unten - self.base_hoehe * 3 / 2)
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
    def __init__(self, x, y, img, player, display, visible, last, dmg, hp, speed):
        self.dmg = dmg
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = hp
        self.progress = 1
        self.player = player
        self.display = display
        self.img = img
        self.visible = visible
        self.last = last
        self.speed = speed
        self.new = True

        # HP Bar
        # Icon
        self.base = pygame.image.load(img)
        self.base = pygame.transform.scale(self.base, (50, 50))
        self.base_breite = self.base.get_size()[0]
        self.base_hoehe = self.base.get_size()[1]

    def update(self):
        self.progress = self.hp / self.max_hp
        if self.hp < 0:
            self.hp = 0
        if self.visible:
            self.display.blit(self.base, (self.x, self.y))

    def move(self, target, last):
        targetx = target.x
        targety = target.y
        if target.img == "resources/castle_red.png":
            targetx -= 35
            targety += 15
        if self.x < targetx and self.y == targety:
            if targetx - self.x < self.speed:
                self.x = targetx
            else:
                self.x += self.speed
        elif self.y < targety and self.x == targetx:
            if targety - self.y < self.speed:
                self.y = targety
            else:
                self.y += self.speed
        elif self.y > targety and self.x == targetx:
            if self.y - targety < self.speed:
                self.y = targety
            else:
                self.y -= self.speed
        elif self.x > targetx and self.y == targety:
            if self.x - targetx < self.speed:
                self.x = targetx
            else:
                self.x -= self.speed

        elif self.x < targetx and self.y < targety:
            if targetx - self.x < self.speed and not (targety - self.y < self.speed):
                self.x = targetx
                self.y += math.sqrt(self.speed)
            elif targetx - self.x < self.speed and targety - self.y < self.speed:
                self.x = targetx
                self.y = targety
            elif not(targetx - self.x < self.speed) and targety - self.y < self.speed:
                self.y = targety
                self.x += math.sqrt(self.speed)
            else:
                self.x += math.sqrt(self.speed)
                self.y += math.sqrt(self.speed)
        elif self.x < targetx and self.y > targety:
            if targetx - self.x < self.speed and not (self.y - targety < self.speed):
                self.x = targetx
                self.y -= math.sqrt(self.speed)
            elif targetx - self.x < self.speed and self.y - targety < self.speed:
                self.x = targetx
                self.y = targety
            elif not (targetx - self.x < self.speed) and self.y - targety < self.speed:
                self.y = targety
                self.x -= math.sqrt(self.speed)
            else:
                self.x += math.sqrt(self.speed)
                self.y -= math.sqrt(self.speed)
        elif self.x > targetx and self.y < targety:
            if self.x - targetx < self.speed and not (targety - self.y < self.speed):
                self.x = targetx
                self.y += math.sqrt(self.speed)
            elif self.x - targetx < self.speed and targety - self.y < self.speed:
                self.x = targetx
                self.y = targety
            elif not (self.x - targetx < self.speed) and targety - self.y < self.speed:
                self.y = targety
                self.x -= math.sqrt(self.speed)
            else:
                self.x -= math.sqrt(self.speed)
                self.y += math.sqrt(self.speed)
        elif self.x > targetx and self.y > targety:
            if self.x - targetx < self.speed and not (targety - self.y < self.speed):
                self.x = targetx
                self.y -= math.sqrt(self.speed)
            elif self.x - targetx < self.speed and targety - self.y < self.speed:
                self.x = targetx
                self.y = targety
            elif not (self.x - targetx < self.speed) and targety - self.y < self.speed:
                self.y = targety
                self.x -= math.sqrt(self.speed)
            else:
                self.x -= math.sqrt(self.speed)
                self.y -= math.sqrt(self.speed)

        else:
            if self.new:
                self.last = last
                self.new = False
            if self.last != last:
                target.hp -= self.dmg
                self.last = last