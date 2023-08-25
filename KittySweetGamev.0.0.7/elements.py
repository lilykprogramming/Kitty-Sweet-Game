"""
GAME: KITTY SWEET GAME

AUTHOR: LILYKPROGRAMMING

- elements, screen game, icon, title

"""


#Import and initialization library pygame.
import pygame
#Import and initialization library pathlib.
from pathlib import Path
#Import module mechanic
import mechanic

#ICON GAME SETTING
icon_game = pygame.image.load("primer/icons/icon_cat.bmp")
pygame.display.set_icon(icon_game)
#SCREEN ON GAME
screen_game = pygame.display.set_mode(size=[mechanic.HEIGHT,mechanic.WIDTH])
#TITLE GAME
pygame.display.set_caption('Kitty Sweet Game')
#MOUSE SETTINGS
pygame.mouse.set_visible(False)
#CLOCK SETTINGS
clock_game = pygame.time.Clock()
#MUSIC SETTING AND PATH
music_path = "primer/sounds/Voicians-Seconds-_NCS-Release_.wav"