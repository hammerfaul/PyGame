import pygame

from UI import *
from sys import exit


def mainscreen(display, mainscreen_height, mainscreen_width):
    warten = True

    mitte = mainscreen_width * (2 / 5)
    breite = mainscreen_width * (1 / 5)
    hoehe = 50
    abstand_y = 50
    pos_y = mainscreen_height / 8

    start = Menu(display=display, x=mitte, y=pos_y * 2, text="Start",
                 color=WEISS, font=myfont_menu, height=hoehe, width=breite, color_blink=ROT)
    option = Menu(display=display, x=mitte, y=pos_y * 3 + abstand_y, text="Option",
                  color=WEISS, font=myfont_menu, height=hoehe, width=breite, color_blink=ROT)
    end = Menu(display=display, x=mitte, y=pos_y * 4 + abstand_y * 2, text="Quit",
               color=WEISS, font=myfont_menu, height=hoehe, width=breite, color_blink=ROT)

    while warten:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if start.collide(mx, my):
                    warten = False
                elif option.collide(mx, my):
                    # Optionen
                    x = 1
                elif end.collide(mx, my):
                    pygame.display.quit()
                    pygame.quit()
                    exit()

        # hervorheben
        mx, my = pygame.mouse.get_pos()
        if start.collide(mx, my):
            start.highlight()
        elif option.collide(mx, my):
            option.highlight()
        elif end.collide(mx, my):
            end.highlight()

        display.fill(HINTERGRUND)

        start.update()
        option.update()
        end.update()

        pygame.display.flip()


class Menu:
    def __init__(self, text, color, display, x, y, font, height, width, color_blink):
        self.text = text
        self.color = color
        self.display = display
        self.text_x = int(x + width / 2)
        self.text_y = int(y + height / 8)
        self.x = int(x)
        self.y = int(y)
        self.height = height
        self.width = width
        self.font = font
        self.blink = False
        self.border_size = 5
        self.border_color = color_blink

    def update(self):

        if self.blink:
            self.blink = False
            pygame.draw.rect(self.display, self.border_color, [self.x - self.border_size, self.y - self.border_size,
                                                               self.width + self.border_size * 2,
                                                               self.height + self.border_size * 2])

            pygame.draw.circle(self.display, self.border_color, (int(self.x - self.border_size / 2),
                                                                 int(self.y + self.height / 2)),
                               int(self.height / 2 + self.border_size))
            pygame.draw.circle(self.display, self.border_color, (int(self.x + self.width + self.border_size / 2),
                                                                 int(self.y + self.height / 2)),
                               int(self.height / 2 + self.border_size))

        pygame.draw.rect(self.display, self.color, [self.x, self.y, self.width, self.height])

        pygame.draw.circle(self.display, self.color, (self.x, int(self.y + self.height / 2)), int(self.height / 2))
        pygame.draw.circle(self.display, self.color, (int(self.x + self.width), int(self.y + self.height / 2))
                           , int(self.height / 2))

        text = self.font.render(str(self.text), False, (0, 0, 0))
        text_width = text.get_width()
        self.display.blit(text, (int(self.text_x - text_width / 2), self.text_y))

    def collide(self, mx, my):
        if self.x < mx < self.x + self.width and self.y < my < self.y + self.height:
            return True

    def highlight(self):
        self.blink = True
