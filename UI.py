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

        for i in range(1, 50):
            breitentest = ""
            for o in range(1, i):
                breitentest += "9"

            text2 = self.font.render(str(breitentest), False, (0, 0, 0))
            text2_width = text2.get_width()
            if text2_width > self.width:
                print("Max_Breite: " + str(i - 1))
                self.max_length = i - 1
                break

        # TODO: maximale Chatlänge, für jede Nachricht, ermitteln

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
        if len(text) > self.max_length:
            i = len(text) / self.max_length
            i = math.ceil(i)

            lines = ["" for x in range(i)]
            for n in range(0, i):
                lines[n] = text[self.max_length * n:self.max_length * (n + 1)]
                for o in range(1, self.zeilen):
                    self.text[self.zeilen - o] = self.text[self.zeilen - o - 1]
                    self.alfa[self.zeilen - o] = self.alfa[self.zeilen - o - 1]
            for n in range(0, i):
                self.text[n] = lines[n]
                self.alfa[n] = 255
        else:
            for i in range(1, self.zeilen):
                self.text[self.zeilen - i] = self.text[self.zeilen - i - 1]
                self.alfa[self.zeilen - i] = self.alfa[self.zeilen - i - 1]
            self.text[0] = text
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

    # TODO: Doppelpunkt auf gleicher höhe
    # TODO: Resourcen Icons

    def update(self):
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
        self.x = abstand * pos + breite_unten * (pos - 1)
        self.y = screen_height - abstand - self.height
        self.font = font
        self.blink = False
        self.border_size = 2
        self.border_color = color_blink

    def update(self):
        if self.blink:
            self.blink = False
            pygame.draw.rect(self.display, self.border_color, [self.x - self.border_size, self.y - self.border_size,
                                                               self.width + self.border_size*2, self.height + self.border_size*2])

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
