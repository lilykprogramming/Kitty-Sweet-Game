"""
GAME: KITTY SWEET GAME

AUTHOR: LILYKPROGRAMMING

- Classes:
- Player,
- Mouse.
- Cucumber, 
- Mousetrap
- Catmint.
"""


#Import and initialization library pygame.
import pygame
#Import and initialization library random.
from random import randint
#Import and initialization library typing.
from typing import Tuple
#Import and initialization library pathlib.
from pathlib import Path
#Import and initialization library typing.
from typing import Tuple
#Import module mechanic
import mechanic

#CLASS PLAYER
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        player_avatar=str(
            Path.cwd() / "primer" / "images" / "avatars" / "avatar_cat.bmp"
        )
        self.surf = pygame.image.load(player_avatar).convert_alpha()
        self.rect = self.surf.get_rect()
    def update(self,pos: Tuple):
        self.rect.center=pos
    def reset_position(self, initial_position: Tuple):
        self.rect.center = initial_position
#CLASS MOUSE
class Mouse(pygame.sprite.Sprite):
    def __init__(self):
        super(Mouse,self).__init__()
        self.catch = False
        self.mouse_avatar = "primer/images/avatars/avatar_mouse.bmp"
        mouse_avatar = str(Path.cwd() / "primer" / "images" / "avatars" / "avatar_mouse.bmp")
        self.surf = pygame.image.load(mouse_avatar).convert_alpha()
        self.rect = self.surf.get_rect(
            center=(
                randint(10,mechanic.HEIGHT - 10),
                randint(10,mechanic.WIDTH - 10),
            )
        )
    def reset_position(self):
        self.rect.center = (randint(10, mechanic.HEIGHT - 10), randint(10, mechanic.WIDTH - 10))
        
class Cucumber(pygame.sprite.Sprite): #ogórek
    def __init__(self):
        super(Cucumber,self).__init__()
        self.catch = False
        self.cucumber_avatar = "primer/images/avatars/avatar_cucumber.bmp"
        cucumber_avatar = str(Path.cwd() / "primer" / "images" / "avatars" / "avatar_cucumber.bmp")
        self.surf = pygame.image.load(cucumber_avatar).convert_alpha()
        self.rect = self.surf.get_rect(
            center = (
                randint(10,mechanic.HEIGHT - 10),
                randint(10,mechanic.WIDTH - 10),
        )
    )   
#class Mousetrap(pygame.sprite.Sprite) #pułapka na myszy
 #   def __init__(self):
#        super(
#class Catmint #koci miętka
