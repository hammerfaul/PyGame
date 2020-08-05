import pygame

screen_width = 1280
screen_height = 720
game_name = "Nur ein toller Test"

#base
base_hp = 1000
base_dmg = 5

#resources
r_abstand = 5

#UI
breite_unten = 35

#hpbar
hpbar_height = 9

#buttons
abstand = 2

# Farben
Farbe_UI_Unten = (255, 0, 0)
ORANGE = (255, 140, 0)
ROT = (255, 0, 0)
GRUEN = (0, 255, 0)
SCHWARZ = (0, 0, 0)
WEISS = (255, 255, 255)
HINTERGRUND = (220, 220, 220)

#Fonts
pygame.font.init()
myfont = pygame.font.SysFont('arial', hpbar_height)
myfont2 = pygame.font.SysFont('arial', int(breite_unten / 2))
myfont3 = pygame.font.SysFont('arial', int(breite_unten / 2))
myfont_menu = pygame.font.SysFont('arial', 30)
