import pygame
import math
from datetime import datetime

from config import *
from UI import *
from Mainscreen import *
from figures import *

pygame.init()
pygame.font.init()

minions_alive = 0
minions = []
number_minions = 10


def missing(gold=0, wood=0, human=0, food=0):
    g_missing = gold - R_Gold.amount
    w_missing = wood - R_Holz.amount
    h_missing = human - R_Menschen.amount
    f_missing = food - R_Nahrung.amount
    start = "Euch fehlt: "
    strg = ""
    if g_missing > 0:
        strg += str(g_missing) + " Gold"
    if w_missing > 0:
        if strg != "":
            strg += ", "
            start = "Euch fehlen: "
        strg += str(w_missing) + " Holz"
    if h_missing > 0:
        if strg != "":
            strg += ", "
            start = "Euch fehlen: "
        strg += str(h_missing) + " Bevölkerung"
    if f_missing > 0:
        if strg != "":
            strg += ", "
            start = "Euch fehlen: "
        strg += str(f_missing) + " Nahrung"
    Info.newmessage(text=start + strg)


def button_1():
    if Speer.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Speer.gold
        R_Holz.amount -= Speer.wood
        R_Menschen.amount -= Speer.human
        R_Nahrung.amount -= Speer.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Speer.speed
        minions_alive += 1
        Info.newmessage(text="Speerträger gespawnt")
    else:
        missing(gold=Speer.gold, wood=Speer.wood, human=Speer.human, food=Speer.food)


def button_2():
    if Berserk.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Berserk.gold
        R_Holz.amount -= Berserk.wood
        R_Menschen.amount -= Berserk.human
        R_Nahrung.amount -= Berserk.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Berserk.speed
        minions[minions_alive].base = pygame.image.load("resources/beserker red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (39, 39))
        minions_alive += 1
        Info.newmessage(text="Beserker gespawnt")
    else:
        missing(gold=Berserk.gold, wood=Berserk.wood, human=Berserk.human, food=Berserk.food)


def button_3():
    if Archer.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Archer.gold
        R_Holz.amount -= Archer.wood
        R_Menschen.amount -= Archer.human
        R_Nahrung.amount -= Archer.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Archer.speed
        minions[minions_alive].base = pygame.image.load("resources/archer red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (42, 42))
        minions_alive += 1
        Info.newmessage(text="Bogenschütze gespawnt")
    else:
        missing(gold=Archer.gold, wood=Archer.wood, human=Archer.human, food=Archer.food)


def button_4():
    if Horse.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Horse.gold
        R_Holz.amount -= Horse.wood
        R_Menschen.amount -= Horse.human
        R_Nahrung.amount -= Horse.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Horse.speed
        minions[minions_alive].base = pygame.image.load("resources/horse red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (50, 50))
        minions_alive += 1
        Info.newmessage(text="Reiter gespawnt")
    else:
        missing(gold=Horse.gold, wood=Horse.wood, human=Horse.human, food=Horse.food)


def button_5():
    if Knight.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Knight.gold
        R_Holz.amount -= Knight.wood
        R_Menschen.amount -= Knight.human
        R_Nahrung.amount -= Knight.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Knight.speed
        minions[minions_alive].base = pygame.image.load("resources/knight red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (35, 35))
        minions_alive += 1
        Info.newmessage(text="Ritter gespawnt")
    else:
        missing(gold=Knight.gold, wood=Knight.wood, human=Knight.human, food=Knight.food)


def button_6():
    if Mage.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Mage.gold
        R_Holz.amount -= Mage.wood
        R_Menschen.amount -= Mage.human
        R_Nahrung.amount -= Mage.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Mage.speed
        minions[minions_alive].base = pygame.image.load("resources/mage red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (60, 60))
        minions_alive += 1
        Info.newmessage(text="Magier gespawnt")
    else:
        missing(gold=Mage.gold, wood=Mage.wood, human=Mage.human, food=Mage.food)


def button_7():
    if Priest.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Priest.gold
        R_Holz.amount -= Priest.wood
        R_Menschen.amount -= Priest.human
        R_Nahrung.amount -= Priest.food
        global minions
        global minions_alive
        minions[minions_alive].visible = True
        minions[minions_alive].x = base_1.x + 60
        minions[minions_alive].y = base_1.y + 30
        minions[minions_alive].speed = Priest.speed
        minions[minions_alive].base = pygame.image.load("resources/priest red.png")
        minions[minions_alive].base = pygame.transform.scale(minions[minions_alive].base, (40, 40))
        minions_alive += 1
        Info.newmessage(text="Priester gespawnt")
    else:
        missing(gold=Priest.gold, wood=Priest.wood, human=Priest.human, food=Priest.food)


def button_8():
    Info.newmessage(text="Spieler hat 8-Taste gedrückt")


def button_9():
    if Gold.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Gold.gold
        R_Holz.amount -= Gold.wood
        R_Nahrung.amount -= Gold.food
        base_1.gold += 1
        Gold.gold = base_1.gold * 15
        Gold.wood = base_1.gold * 5
        Info.newmessage(text="Die Goldmine wurde verbessert.")
    else:
        missing(gold=Gold.gold, wood=Gold.wood, food=Gold.food)


def button_10():
    if Holz.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Holz.gold
        R_Holz.amount -= Holz.wood
        R_Nahrung.amount -= Holz.food
        base_1.holz += 1
        Holz.gold = base_1.holz * 10
        Holz.wood = base_1.holz * 5
        Info.newmessage(text="Die Holzhütte wurde verbessert.")
    else:
        missing(gold=Holz.gold, wood=Holz.wood, food=Holz.food)


def button_11():
    if Essen.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Essen.gold
        R_Holz.amount -= Essen.wood
        R_Menschen.amount -= Essen.human
        base_1.nahrung += 1
        Essen.gold = base_1.nahrung * 15
        Essen.wood = base_1.nahrung * 15
        Info.newmessage(text="Die Farm wurde verbessert.")
    else:
        missing(gold=Essen.gold, wood=Essen.wood * 15, human=Essen.human)


def button_12():
    if Menschen.enought(R_Gold.amount, R_Holz.amount, R_Nahrung.amount, R_Menschen.amount):
        R_Gold.amount -= Menschen.gold
        R_Holz.amount -= Menschen.wood
        R_Nahrung.amount -= Menschen.food
        base_1.menschen += 1
        Menschen.gold = base_1.menschen * 10
        Menschen.wood = base_1.menschen * 10
        Info.newmessage(text="Das Wohnhaus wurde verbessert.")
    else:
        missing(gold=Menschen.gold, wood=Menschen.wood, food=Menschen.food)


def arestart():
    base_2.hp = base_hp
    base_1.hp = base_hp
    R_Gold.amount = start_gold
    R_Holz.amount = start_wood
    R_Nahrung.amount = start_food
    R_Menschen.amount = start_human
    base_1.gold = 1
    base_1.holz = 1
    base_1.menschen = 1
    base_1.nahrung = 1
    Gold.gold = 15
    Gold.wood = 5
    Gold.food = 1
    Holz.gold = 10
    Holz.wood = 5
    Holz.food = 2
    Essen.gold = 15
    Essen.wood = 15
    Essen.human = 2
    Menschen.gold = 10
    Menschen.wood = 10
    Menschen.food = 5

    for i in range(number_minions):
        minions[i].x = -1000


def spielpause(pause=True):
    while pause:
        Pause.update()
        base_1.update()
        base_2.update()
        for i in range(number_minions):
            minions[i].update()
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause = False


def last_update(current_time):
    screen.fill(HINTERGRUND)
    Info.update()
    pygame.draw.rect(screen, Farbe_UI_Unten,
                     [0, screen_height - breite_unten, screen_width, breite_unten])
    text2 = myfont_uhr.render(current_time, False, (0, 0, 0))
    screen.blit(text2, (int(screen_width / 2 - text2.get_width() / 2), screen_height - breite_unten))
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
    R_Gold.update()
    R_Holz.update()
    R_Nahrung.update()
    R_Menschen.update()
    base_1.update()
    base_2.update()
    for i in range(number_minions):
        minions[i].update()
    pygame.display.flip()


def spielstart(spielaktiv):
    ticks = 0
    sek = 0

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    for i in range(number_minions):
        minions.append(
            Spawn(x=50, y=50, img="resources/speer red.png", player=1, display=screen, visible=False, last=current_time,
                  dmg=Speer.dmg, hp=Speer.hp, speed=Speer.speed))

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
        R_Gold.update()
        R_Holz.update()
        R_Nahrung.update()
        R_Menschen.update()

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
            Tooltip.update(x=mx, y=my, who=9, amount=base_1.gold, wer=Gold)
        elif null.collide(mx, my):
            null.highlight()
            Tooltip.update(x=mx, y=my, who=10, amount=base_1.holz, wer=Holz)
        elif sz.collide(mx, my):
            sz.highlight()
            Tooltip.update(x=mx, y=my, who=11, amount=base_1.nahrung, wer=Essen)
        elif kommaoben.collide(mx, my):
            kommaoben.highlight()
            Tooltip.update(x=mx, y=my, who=12, amount=base_1.menschen, wer=Menschen)

        ticks += 1
        if ticks >= 60:  # 1sek
            ticks = 0
            sek += 1
            # Uhr
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            if sek % 1 == 0:
                R_Gold.amount += base_1.gold
                R_Holz.amount += base_1.holz
                R_Nahrung.amount += base_1.nahrung
                R_Menschen.amount += base_1.menschen
            if sek >= 60:
                sek = 0

        # Base update
        base_1.update()
        base_2.update()

        for i in range(number_minions):
            if minions[i].visible:
                minions[i].move(target=base_2, last=current_time)
                if base_1.hp <= 0:
                    last_update(current_time=current_time)
                    pause = True
                    while pause:
                        Lose.update()
                        restart.update()
                        pygame.display.flip()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    spielaktiv = False
                                    pause = False
                            elif event.type == pygame.QUIT:
                                pygame.display.quit()
                                pygame.quit()
                                exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mx, my = pygame.mouse.get_pos()
                                if restart.collide(mx, my):
                                    pause = False
                                    arestart()
                                    break
                        screen.fill(HINTERGRUND)

                if base_2.hp <= 0:
                    last_update(current_time=current_time)
                    pause = True
                    while pause:
                        Win.update()
                        restart.update()
                        pygame.display.flip()
                        # hervorheben
                        mx, my = pygame.mouse.get_pos()
                        if restart.collide(mx, my):
                            restart.highlight()
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_ESCAPE:
                                    spielaktiv = False
                                    pause = False
                            elif event.type == pygame.QUIT:
                                pygame.display.quit()
                                pygame.quit()
                                exit()
                            elif event.type == pygame.MOUSEBUTTONDOWN:
                                mx, my = pygame.mouse.get_pos()
                                if restart.collide(mx, my):
                                    pause = False
                                    arestart()
                                    break
                        screen.fill(HINTERGRUND)

            minions[i].update()

        pygame.display.flip()
        clock.tick(60)


# user32 = ctypes.windll.user32
# monitor_size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.display.set_caption(game_name)

clock = pygame.time.Clock()


restart = Menu(display=screen, x=screen_width / 2 - screen_width * (1 / 5) / 2, y=screen_height / 6 * 5,
               text="Neustart", color=WEISS,
               font=myfont_menu, height=50, width=screen_width * (1 / 5), color_blink=ROT)

Pause = Text(display=screen, x=screen_width / 2 - 200, y=screen_height / 2 - 100, text="PAUSE", color=SCHWARZ,
             font=myfont_pause)
Win = Text(display=screen, x=screen_width / 2 - 300, y=screen_height / 2 - 100, text="Gewonnen", color=SCHWARZ,
           font=myfont_pause)
Lose = Text(display=screen, x=screen_width / 2 - 300, y=screen_height / 2 - 100, text="Verloren", color=SCHWARZ,
            font=myfont_pause)

R_Gold.add = base_1.gold
R_Holz.add = base_1.holz
R_Nahrung.add = base_1.nahrung
R_Menschen.add = base_1.menschen

# Schleife Hauptprogramm
mainscreen(display=screen, mainscreen_width=screen_width, mainscreen_height=screen_height)
spielstart(spielaktiv=True)

pygame.quit()
