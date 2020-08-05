import pygame
import math
from datetime import datetime

from config import *
from UI import *
from Mainscreen import *

pygame.init()
pygame.font.init()

# TODO: Button Abstand
# TODO: Gebäude ausbauen (Holz, Essen, Gold, Menschen)
# TODO: Tooltip für Buttons
# TODO: Pausemenu
# TODO: Optionen (Fenster größe)

# TODO: Buttons spawnen dynamisch Minions
# TODO: Minions greifen andere Base an
# TODO: Base greift Minions an
# TODO: Schaden berechnen
# TODO: Minions greifen sich an
# TODO: Gegener KI
# TODO: verschiedene Karten (vordefinierte spawns)
# TODO: UI überarbeiten
# TODO: verschiedene Minions
# TODO: Tooltip für die Minions
# TODO: Hindernisse auf Karte
# TODO: Minions grob steuern
# TODO: Gegner auf Karte
# TODO: Tag/Nacht Zyklus


def button_1():
    if Gold.amount >= 50:
        Gold.amount -= 50
        speer = Spawn(x=150, y=150, img="resources/speer.png", player=1, display = screen)
        Info.newmessage(text="Speer gespawnt")
    else:
        Info.newmessage(text="Nicht genug Gold: " + str(Gold.amount) + "/50")


def button_2():
    Info.newmessage(text="Spieler hat 2-Taste gedrückt")


def button_3():
    Info.newmessage(text="Spieler hat 3-Taste gedrückt")


def button_4():
    Info.newmessage(text="Spieler hat 4-Taste gedrückt")


def button_5():
    Info.newmessage(text="Spieler hat 5-Taste gedrückt")


def button_6():
    Info.newmessage(text="Spieler hat 6-Taste gedrückt")


def button_7():
    Info.newmessage(text="Spieler hat 7-Taste gedrückt")


def button_8():
    Info.newmessage(text="Spieler hat 8-Taste gedrückt")


def button_9():
    Info.newmessage(text="Spieler hat 9-Taste gedrückt")


def button_10():
    Info.newmessage(text="Spieler hat 0-Taste gedrückt")


def button_11():
    Info.newmessage(text="Spieler hat ß-Taste gedrückt")


def button_12():
    Info.newmessage(text="Spieler hat ´-Taste gedrückt")


def spielstart(spielaktiv):
    ticks = 0
    sek = 0

    current_time = ""

    while spielaktiv:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
                print("Spieler hat Quit-Button angeklickt")
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if eins.collide(mx, my):
                    button_1()
                elif zwei.collide(mx, my):
                    button_2()
                elif drei.collide(mx, my):
                    button_3()
                elif vier.collide(mx, my):
                    button_4()
                elif fuenf.collide(mx, my):
                    button_5()
                elif sechs.collide(mx, my):
                    button_6()
                elif sieben.collide(mx, my):
                    button_7()
                elif acht.collide(mx, my):
                    button_8()
                elif neun.collide(mx, my):
                    button_9()
                elif null.collide(mx, my):
                    button_10()
                elif sz.collide(mx, my):
                    button_11()
                elif kommaoben.collide(mx, my):
                    button_12()

                base_1.hp = base_1.hp - 50
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    button_1()
                elif event.key == pygame.K_2:
                    button_2()
                elif event.key == pygame.K_3:
                    button_3()
                elif event.key == pygame.K_4:
                    button_4()
                elif event.key == pygame.K_5:
                    button_5()
                elif event.key == pygame.K_6:
                    button_6()
                elif event.key == pygame.K_7:
                    button_7()
                elif event.key == pygame.K_8:
                    button_8()
                elif event.key == pygame.K_9:
                    button_9()
                elif event.key == pygame.K_0:
                    button_10()
                elif event.key == 45:
                    button_11()
                elif event.key == 61:
                    button_12()
                elif event.key == pygame.K_ESCAPE:
                    spielaktiv = False
                    print("Spieler hat ESC-Button angeklickt")
                else:
                    print("Kein Funktion zugewiesen. Taste: " + str(event.key))

        # Tooltips
        mx, my = pygame.mouse.get_pos()
        if eins.collide(mx, my):
            eins.highlight()
        elif zwei.collide(mx, my):
            zwei.highlight()
        elif drei.collide(mx, my):
            drei.highlight()
        elif vier.collide(mx, my):
            vier.highlight()
        elif fuenf.collide(mx, my):
            fuenf.highlight()
        elif sechs.collide(mx, my):
            sechs.highlight()
        elif sieben.collide(mx, my):
            sieben.highlight()
        elif acht.collide(mx, my):
            acht.highlight()
        elif neun.collide(mx, my):
            neun.highlight()
        elif null.collide(mx, my):
            null.highlight()
        elif sz.collide(mx, my):
            sz.highlight()
        elif kommaoben.collide(mx, my):
            kommaoben.highlight()

        ticks += 1
        if ticks >= 60:  # 1sek
            ticks = 0
            sek += 1
            # Uhr
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if sek % 3 == 0:  # alle 3 sek
                Gold.amount += base_1.gold
                Holz.amount += base_1.holz
                Nahrung.amount += base_1.nahrung
                Menschen.amount += base_1.menschen
            if sek >= 60:
                sek = 0

        # Spielfeld zeichnen
        screen.fill(HINTERGRUND)
        Info.update()

        pygame.draw.rect(screen, Farbe_UI_Unten, [0, screen_height - breite_unten, screen_width, breite_unten])
        text2 = myfont3.render(current_time, False, (0, 0, 0))
        screen.blit(text2, (int(screen_width / 2), screen_height - breite_unten))
        eins.update()
        zwei.update()
        drei.update()
        vier.update()
        fuenf.update()
        sechs.update()
        sieben.update()
        acht.update()
        neun.update()
        null.update()
        sz.update()
        kommaoben.update()
        Gold.update()
        Holz.update()
        Nahrung.update()
        Menschen.update()

        # Base update
        base_1.update()
        base_2.update()

        pygame.display.flip()
        clock.tick(60)


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
    def __init__(self, x, y, img, player, display):
        self.schaden = 1
        self.x = x
        self.y = y
        self.hp = 5
        self.max_hp = 5
        self.progress = 1
        self.player = player
        self.display = display

        # HP Bar
        # Icon
        self.base = pygame.image.load(img)
        self.base_breite = self.base.get_size()[0]
        self.base_hoehe = self.base.get_size()[1]

    def update(self):
        self.progress = self.hp / self.max_hp
        if self.hp < 0:
            self.hp = 0
        self.display.blit(self.base, self.x, self.y)


# Fenster öffnen
screen = pygame.display.set_mode((screen_width, screen_height))

# user32 = ctypes.windll.user32
# monitor_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

base_1 = Base(img="resources/castle_red.png", player=1, display=screen, color=GRUEN)
base_2 = Base(img="resources/castle_red.png", player=2, display=screen, color=GRUEN)

eins = Button(display=screen, pos=1, text="1", color=WEISS, font=myfont2, color_blink=SCHWARZ)
zwei = Button(display=screen, pos=2, text="2", color=WEISS, font=myfont2, color_blink=SCHWARZ)
drei = Button(display=screen, pos=3, text="3", color=WEISS, font=myfont2, color_blink=SCHWARZ)
vier = Button(display=screen, pos=4, text="4", color=WEISS, font=myfont2, color_blink=SCHWARZ)
fuenf = Button(display=screen, pos=5, text="5", color=WEISS, font=myfont2, color_blink=SCHWARZ)
sechs = Button(display=screen, pos=6, text="6", color=WEISS, font=myfont2, color_blink=SCHWARZ)
sieben = Button(display=screen, pos=7, text="7", color=WEISS, font=myfont2, color_blink=SCHWARZ)
acht = Button(display=screen, pos=8, text="8", color=WEISS, font=myfont2, color_blink=SCHWARZ)
neun = Button(display=screen, pos=9, text="9", color=WEISS, font=myfont2, color_blink=SCHWARZ)
null = Button(display=screen, pos=10, text="0", color=WEISS, font=myfont2, color_blink=SCHWARZ)
sz = Button(display=screen, pos=11, text="ß", color=WEISS, font=myfont2, color_blink=SCHWARZ)
kommaoben = Button(display=screen, pos=12, text="´", color=WEISS, font=myfont2, color_blink=SCHWARZ)

Gold = Resource(text="Gold", amount=100, pos=1, display=screen, add=base_1.gold, font=myfont3)
Holz = Resource(text="Holz", amount=50, pos=2, display=screen, add=base_1.holz, font=myfont3)
Nahrung = Resource(text="Nahrung", amount=50, pos=3, display=screen, add=base_1.nahrung, font=myfont3)
Menschen = Resource(text="Bauern", amount=50, pos=4, display=screen, add=base_1.menschen, font=myfont3)

Info = Chat(display=screen, height=250, width=200, color=SCHWARZ, zeilen=13)

# Schleife Hauptprogramm
mainscreen(display=screen, mainscreen_width=screen_width, mainscreen_height=screen_height)
spielstart(spielaktiv=True)

pygame.quit()
