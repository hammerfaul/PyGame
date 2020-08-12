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

            if text2.get_width() > self.width-2:
                lines[zahl] = buffer2
                buffer = text[i]
                buffer2 = ""
                zahl += 1
            if len(text)-1 == i:
                lines[zahl] = buffer

        for n in range(0, zahl+1):
            for o in range(1, self.zeilen):
                self.text[self.zeilen - o] = self.text[self.zeilen - o - 1]
                self.alfa[self.zeilen - o] = self.alfa[self.zeilen - o - 1]
            self.text[0] = lines[zahl-n]
            self.alfa[0] = 255


class Resource:
    def __init__(self, display, text, amount, pos, add, font):
        self.amount = amount
        self.name = text
        self.font = font
        self.text = str(text + ": " + str(self.amount))
        text2 = self.font.render(self.text, False, (0, 0, 0))
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


    def update(self, add):
        self.add = add
        self.text = str(self.name + ": " + str(self.amount) + "(+" + str(self.add) + ")")
        text2 = self.font.render(self.text, False, (0, 0, 0))
        self.display.blit(text2,
                          (self.x,
                           self.y))


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

    def update(self, x, y, who, amount=0):

        if who == 1:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 300, 150, 250))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 300, 150, 250), 1)

            text2 = self.font.render("Speer", False, (0, 0, 0))
            self.display.blit(text2,
                              (x + 2,
                               y - 300))

        elif who == 2:
            x = 1
        elif who == 3:
            x = 2
        elif who == 4:
            x = 2
        elif who == 5:
            x = 2
        elif who == 6:
            x = 2
        elif who == 7:
            x = 2
        elif who == 8:
            x = 2
        elif who == 9:
            pygame.draw.rect(self.display, WEISS, pygame.Rect(x, y - 100, 155, 100))
            pygame.draw.rect(self.display, self.color, pygame.Rect(x, y - 100, 155, 100), 1)

            string = ["Goldmine Stufe: " + str(amount),
                      "Verbessern zu +" + str(amount + 1) + " Gold für:",
                      str(amount * 15) + " Gold",
                      str(amount * 5) + " Holz",
                      "1 Nahrung",
                      "0 Bevölkerung",
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
                      "Verbessern zu +" + str(amount + 1) + " Holz für:",
                      str((amount + 1) * 10) + " Gold",
                      str((amount + 1) * 5) + " Holz",
                      "2 Nahrung",
                      "0 Bevölkerung",
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
                      "Verbessern zu +" + str(amount + 1) + " Nahrung für:",
                      str((amount + 1) * 15) + " Gold",
                      str((amount + 1) * 15) + " Holz",
                      "0 Nahrung",
                      "2 Bevölkerung",
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
                      "Verbessern zu +" + str(amount + 1) + " Menschen für:",
                      str((amount + 1) * 10) + " Gold",
                      str((amount + 1) * 10) + " Holz",
                      "5 Nahrung",
                      "0 Bevölkerung",
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
