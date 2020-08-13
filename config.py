import pygame

screen_width = 1280
screen_height = 720
game_name = "Nur ein toller Test"

# base
base_hp = 1000
base_dmg = 5

# resources
r_abstand = 5

# UI
breite_unten = 35

# hpbar
hpbar_height = 9

# buttons
abstand = 2

# Farben
Farbe_UI_Unten = (190, 190, 190)
ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
HINTERGRUND = (36, 143, 36)

# Fonts
pygame.font.init()
myfont = pygame.font.SysFont('arial', hpbar_height)
myfont_uhr = pygame.font.SysFont('malgungothic', int(breite_unten / 2))
myfont_menu = pygame.font.SysFont('gillsans', 30)
myfont_button = pygame.font.SysFont('arial', int(breite_unten / 2))
myfont_ressourcen = pygame.font.SysFont('gillsans', int(breite_unten / 2))
myfont_pause = pygame.font.SysFont('gillsans', 120)


class Kosten:
    def __init__(self, gold, wood, human, food, dmg, hp, speed):
        self.gold = gold
        self.wood = wood
        self.human = human
        self.food = food
        self.dmg = dmg
        self.hp = hp
        self.speed = speed

    def enought(self, gold, wood, food, human):
        if gold >= self.gold and wood >= self.wood and food >= self.food and human >= self.human:
            return True
        else:
            return False


Speer = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
Archer = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
Knight = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
Horse = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=1)
Berserk = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
Mage = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
Priest = Kosten(gold=20, wood=5, food=2, human=1, dmg=100, hp=5, speed=0.5)
