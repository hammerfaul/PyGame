from config import *
import pygame
import math


class Chat:
    def __init__(self, display, width, height, color, zeilen):
        self.display = display
        self.width = width
        self.height = height
        self.color = color
        self.x = 2
        self.y = screen_height - breite_unten - self.height + 1
        self.zeilen = zeilen
        self.font = pygame.font.SysFont('arial', int(height / (self.zeilen * 1.1)))
        self.text = ["" for x in range(self.zeilen)]
        self.alfa = [0 for x in range(self.zeilen)]

    def update(self):
        pygame.draw.rect(self.display, WEISS, pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.rect(self.display, self.color, pygame.Rect(self.x, self.y, self.width, self.height), 1)

        for i in range(0, self.zeilen - 1):
            self.alfa[i] -= 1
            text2 = self.font.render(str(self.text[i]), False, (0, 0, 0))
            text2.set_alpha(self.alfa[i])
            text2_height = text2.get_height()
            self.display.blit(text2,
                              (self.x + 2,
                               self.y + text2_height * i))

    def newmessage(self, text):
        buffer = ""
        buffer2 = ""
        lines = ["" for x in range(self.zeilen)]
        zahl = 0

        for i in range(0, len(text)):
            buffer2 = buffer
            buffer += text[i]

            text2 = self.font.render(str(buffer), False, (0, 0, 0))

            if text2.get_width() > self.width - 2:
                lines[zahl] = buffer2
                buffer = text[i]
                buffer2 = ""
                zahl += 1
            if len(text) - 1 == i:
                lines[zahl] = buffer

        for n in range(0, zahl + 1):
            for o in range(1, self.zeilen):
                self.text[self.zeilen - o] = self.text[self.zeilen - o - 1]
                self.alfa[self.zeilen - o] = self.alfa[self.zeilen - o - 1]
            self.text[0] = lines[zahl - n]
            self.alfa[0] = 255


class Resource:
    def __init__(self, display, amount, pos, add, font, img):
        self.amount = amount
        self.font = font
        text = str("   : " + str(self.amount) + "(+0)")
        text2 = self.font.render(text, False, (0, 0, 0))
        text2_height = text2.get_height()
        self.display = display
        self.add = add

        if pos == 1:
            self.y = int(screen_height - breite_unten)
            self.x = int(screen_width - r_abstand - 120)
        elif pos == 2:
            self.y = int(screen_height - text2_height)
            self.x = int(screen_width - r_abstand - 120)
        elif pos == 3:
            self.y = int(screen_height - breite_unten)
            self.x = int(screen_width - r_abstand - 280)
        elif pos == 4:
            self.y = int(screen_height - text2_height)
            self.x = int(screen_width - r_abstand - 280)

        self.icon = pygame.image.load(img)
        self.icon = pygame.transform.scale(self.icon, (int(breite_unten / 2), int(breite_unten / 2)))

    def update(self, add):
        self.add = add
        text = str("     : " + str(self.amount) + "(+" + str(self.add) + ")")
        text2 = self.font.render(text, False, (0, 0, 0))
        self.display.blit(text2,
                          (self.x,
                           self.y))
        self.display.blit(self.icon, (self.x, self.y))


class Button:
    def __init__(self, text, color, display, pos, font, color_blink):
        self.text = text
        self.color = color
        self.display = display
        self.width = breite_unten - abstand * 2
        self.height = breite_unten - abstand * 2
        self.pos = pos
        self.x = abstand + breite_unten * (pos - 1)
        self.y = screen_height - abstand - self.height
        self.font = font
        self.blink = False
        self.border_size = 2
        self.border_color = color_blink

    def update(self):
        if self.blink:
            self.blink = False
            pygame.draw.rect(self.display, self.border_color, [self.x - self.border_size, self.y - self.border_size,
                                                               self.width + self.border_size * 2,
                                                               self.height + self.border_size * 2])

        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])
        text = self.font.render(str(self.text), False, (0, 0, 0))
        self.display.blit(text,
                          (int(self.x + 1),
                           int(self.y)))

    def collide(self, mx, my):
        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            return True

    def highlight(self):
        self.blink = True


class Tooltip:
    def __init__(self, width, height, color, display):
        self.width = width
        self.height = height
        self.color = color
        self.display = display
        self.who = 0
        self.font = pygame.font.SysFont('arial', 15)

    def update(self, x, y, who, wer=0, amount=0):

        if who == 1:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Speerträger",
                      "Schaden: " + str(Speer.dmg) + ", Leben: " + str(Speer.hp),
                      str(Speer.gold) + " Gold",
                      str(Speer.wood) + " Holz",
                      str(Speer.food) + " Nahrung",
                      str(Speer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))

        elif who == 2:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Beserker",
                      "Schaden: " + str(Berserk.dmg) + ", Leben: " + str(Berserk.hp),
                      str(Berserk.gold) + " Gold",
                      str(Berserk.wood) + " Holz",
                      str(Berserk.food) + " Nahrung",
                      str(Berserk.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 3:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Bogenschütze",
                      "Schaden: " + str(Archer.dmg) + ", Leben: " + str(Archer.hp),
                      str(Archer.gold) + " Gold",
                      str(Archer.wood) + " Holz",
                      str(Archer.food) + " Nahrung",
                      str(Archer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 4:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Reiter",
                      "Schaden: " + str(Horse.dmg) + ", Leben: " + str(Horse.hp),
                      str(Horse.gold) + " Gold",
                      str(Horse.wood) + " Holz",
                      str(Horse.food) + " Nahrung",
                      str(Horse.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 5:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Ritter",
                      "Schaden: " + str(Knight.dmg) + ", Leben: " + str(Knight.hp),
                      str(Knight.gold) + " Gold",
                      str(Knight.wood) + " Holz",
                      str(Knight.food) + " Nahrung",
                      str(Knight.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 6:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Magier",
                      "Schaden: " + str(Mage.dmg) + ", Leben: " + str(Mage.hp),
                      str(Mage.gold) + " Gold",
                      str(Mage.wood) + " Holz",
                      str(Mage.food) + " Nahrung",
                      str(Mage.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 7:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Priester",
                      "AOE-Heilung: " + str(Priest.dmg) + ", Leben: " + str(Priest.hp),
                      str(Priest.gold) + " Gold",
                      str(Priest.wood) + " Holz",
                      str(Priest.food) + " Nahrung",
                      str(Priest.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 8:
            x = 2
        elif who == 9:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 155, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 155, 100), 1)

            string = ["Goldmine Stufe: " + str(amount),
                      "Verbessern zu +" + str(amount+1) + " Gold für:",
                      str(wer.gold) + " Gold",
                      str(wer.wood) + " Holz",
                      str(wer.food) + " Nahrung",
                      str(wer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))

        elif who == 10:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 150, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 150, 100), 1)

            string = ["Holzfällerhütte Stufe: " + str(amount),
                      "Verbessern zu +" + str(amount+1) + " Holz für:",
                      str(wer.gold) + " Gold",
                      str(wer.wood) + " Holz",
                      str(wer.food) + " Nahrung",
                      str(wer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 11:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 175, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 175, 100), 1)

            string = ["Farm Stufe: " + str(amount),
                      "Verbessern zu +" + str(amount+1) + " Nahrung für:",
                      str(wer.gold) + " Gold",
                      str(wer.wood) + " Holz",
                      str(wer.food) + " Nahrung",
                      str(wer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))
        elif who == 12:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 185, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 185, 100), 1)

            string = ["Wohnhaus Stufe: " + str(amount),
                      "Verbessern zu +" + str(amount+1) + " Menschen für:",
                      str(wer.gold) + " Gold",
                      str(wer.wood) + " Holz",
                      str(wer.food) + " Nahrung",
                      str(wer.human) + " Bevölkerung",
                      ]

            for i in range(0, 6):
                text2 = self.font.render(string[i], False, (0, 0, 0))
                self.display.blit(text2,
                                  (x + 2,
                                   y - 100 + 15 * i))


class Text:
    def __init__(self, text, x, y, font, display, color):
        self.text = text
        self.x = x
        self.y = y
        self.display = display
        self.color = color
        self.font = font

    def update(self):
        text2 = self.font.render(self.text, False, (0, 0, 0))
        self.display.blit(text2,
                          (self.x,
                           self.y))
