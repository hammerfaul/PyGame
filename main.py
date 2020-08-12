import pygame
import math
from datetime import datetime

from config import *
from UI import *
from Mainscreen import *
from figures import *

pygame.init()
pygame.font.init()

def button_1():
    if Gold.amount >= 50:
        Gold.amount -= 50
        einheiten[0].visible = True
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
    if Gold.amount >= base_1.gold * 15 and Holz.amount >= base_1.holz * 5 and Nahrung.amount >= 1:
        Gold.amount -= base_1.gold * 15
        Holz.amount -= base_1.holz * 5
        Nahrung.amount -= 1
        base_1.gold += 1
        Info.newmessage(text="Die Goldmine wurde verbessert.")
    else:
        Info.newmessage(text="Die Goldmine ist zu teuer.")


def button_10():
    if Gold.amount >= base_1.gold * 20 and Holz.amount >= base_1.holz * 5 and Nahrung.amount >= 2:
        Gold.amount -= base_1.gold * 10
        Holz.amount -= base_1.holz * 5
        Nahrung.amount -= 2
        base_1.holz += 1
        Info.newmessage(text="Die Holzhütte wurde verbessert.")
    else:
        Info.newmessage(text="Die Holzhütte ist zu teuer.")


def button_11():
    if Gold.amount >= base_1.gold * 15 and Holz.amount >= base_1.holz * 15 and Menschen.amount >= 2:
        Gold.amount -= base_1.gold * 15
        Holz.amount -= base_1.holz * 15
        Menschen.amount -= 2
        base_1.nahrung += 1
        Info.newmessage(text="Die Farm wurde verbessert.")
    else:
        Info.newmessage(text="Die Farm ist zu teuer.")


def button_12():
    if Gold.amount >= base_1.gold * 10 and Holz.amount >= base_1.holz * 15 and Nahrung.amount >= 5:
        Gold.amount -= base_1.gold * 10
        Holz.amount -= base_1.holz * 10
        Nahrung.amount -= 5
        base_1.menschen += 1
        Info.newmessage(text="Das Wohnhaus wurde verbessert.")
    else:
        Info.newmessage(text="Das Wohnhaus ist zu teuer.")


def spielpause(pause=True):
    while pause:
        Pause.update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False


def spielstart(spielaktiv):
    ticks = 0
    sek = 0

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    einheiten = [Spawn(x=50, y=50, img="resources/speer.png", player=1, display=screen, visible=False)]

    while spielaktiv:

        # Spielfeld zeichnen
        screen.fill(HINTERGRUND)
        Info.update()

        # Bar unten
        pygame.draw.rect(screen, Farbe_UI_Unten, [0, screen_height - breite_unten, screen_width, breite_unten])
        text2 = myfont_uhr.render(current_time, False, (0, 0, 0))
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
        Gold.update(add=base_1.gold)
        Holz.update(add=base_1.holz)
        Nahrung.update(add=base_1.nahrung)
        Menschen.update(add=base_1.menschen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                spielaktiv = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    spielpause()
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
            Tooltip.update(x=mx, y=my, who=1)
        elif zwei.collide(mx, my):
            zwei.highlight()
            Tooltip.update(x=mx, y=my, who=2)
        elif drei.collide(mx, my):
            drei.highlight()
            Tooltip.update(x=mx, y=my, who=3)
        elif vier.collide(mx, my):
            vier.highlight()
            Tooltip.update(x=mx, y=my, who=4)
        elif fuenf.collide(mx, my):
            fuenf.highlight()
            Tooltip.update(x=mx, y=my, who=5)
        elif sechs.collide(mx, my):
            sechs.highlight()
            Tooltip.update(x=mx, y=my, who=6)
        elif sieben.collide(mx, my):
            sieben.highlight()
            Tooltip.update(x=mx, y=my, who=7)
        elif acht.collide(mx, my):
            acht.highlight()
            Tooltip.update(x=mx, y=my, who=8)
        elif neun.collide(mx, my):
            neun.highlight()
            Tooltip.update(x=mx, y=my, who=9, amount=base_1.gold)
        elif null.collide(mx, my):
            null.highlight()
            Tooltip.update(x=mx, y=my, who=10, amount=base_1.holz)
        elif sz.collide(mx, my):
            sz.highlight()
            Tooltip.update(x=mx, y=my, who=11, amount=base_1.nahrung)
        elif kommaoben.collide(mx, my):
            kommaoben.highlight()
            Tooltip.update(x=mx, y=my, who=12, amount=base_1.menschen)

        ticks += 1
        if ticks >= 60:  # 1sek
            ticks = 0
            sek += 1
            # Uhr
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if sek % 2 == 0:  # alle 2 sek
                Gold.amount += base_1.gold
                Holz.amount += base_1.holz
                Nahrung.amount += base_1.nahrung
                Menschen.amount += base_1.menschen
            if sek >= 60:
                sek = 0

        # Base update
        base_1.update()
        base_2.update()

        einheiten[0].update(x=50, y=50)

        pygame.display.flip()
        clock.tick(60)


# Fenster öffnen
screen = pygame.display.set_mode((screen_width, screen_height))

# user32 = ctypes.windll.user32
# monitor_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.display.set_caption(game_name)

clock = pygame.time.Clock()

base_1 = Base(img="resources/castle_red.png", player=1, display=screen, color=GRUEN)
base_2 = Base(img="resources/castle_red.png", player=2, display=screen, color=GRUEN)

eins = Button(display=screen, pos=1, text="1", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
zwei = Button(display=screen, pos=2, text="2", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
drei = Button(display=screen, pos=3, text="3", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
vier = Button(display=screen, pos=4, text="4", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
fuenf = Button(display=screen, pos=5, text="5", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
sechs = Button(display=screen, pos=6, text="6", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
sieben = Button(display=screen, pos=7, text="7", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
acht = Button(display=screen, pos=8, text="8", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
neun = Button(display=screen, pos=9, text="9", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
null = Button(display=screen, pos=10, text="0", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
sz = Button(display=screen, pos=11, text="ß", color=WEISS, font=myfont_button, color_blink=SCHWARZ)
kommaoben = Button(display=screen, pos=12, text="´", color=WEISS, font=myfont_button, color_blink=SCHWARZ)

Pause = Text(display=screen, x=screen_width/2-200, y=screen_height/2-100, text="PAUSE", color=SCHWARZ, font=myfont_pause)

Tooltip = Tooltip(display=screen, width=50, height=50, color=SCHWARZ)

Gold = Resource(amount=100, pos=1, display=screen, add=base_1.gold, font=myfont_ressourcen, img="resources/gold.png")
Holz = Resource(amount=50, pos=2, display=screen, add=base_1.holz, font=myfont_ressourcen, img="resources/wood.png")
Nahrung = Resource(amount=50, pos=3, display=screen, add=base_1.nahrung, font=myfont_ressourcen, img="resources/food.png")
Menschen = Resource(amount=50, pos=4, display=screen, add=base_1.menschen, font=myfont_ressourcen, img="resources/human.png")

Info = Chat(display=screen, height=250, width=200, color=SCHWARZ, zeilen=13)

# Schleife Hauptprogramm
mainscreen(display=screen, mainscreen_width=screen_width, mainscreen_height=screen_height)
spielstart(spielaktiv=True)

pygame.quit()
