"""
GAME: KITTY SWEET GAME

AUTHOR: LILYKPROGRAMMING

- variable
- initialization: function, variable,colors, height and width

"""


#Import and initialization library pygame.
import pygame

#DISPLAY RESOLUTION
HEIGHT=1280
WIDTH=1024

#MOUSE SETTINGS
countdown_mouse = 2500
range_mouse = 100
number_of_mouse = 5
#CUCUMBER SETTINGS
countdown_cucumber = 4000
range_cucumber = 100
number_of_cucumber = 5

initial_x = 400
initial_y = 300

#COLORS
purple =(106,13,173)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
pink = (255,192,203)
black = (0,0,0)

#RUNNING GAME SETTINGS
running = True

#SETTINGS POINTS
points = 0

#FUNCTIONS
show_start_screen = True
show_info_screen = False
show_end_screen = False
show_settings_screen = False


list_mouse = pygame.sprite.Group()
ADD_MOUSE = pygame.USEREVENT + 1

#IMAGES IMPORT
background_image_start_screen = pygame.image.load("primer/images/backgrounds/background_game.bmp")
background_image_start_screen = pygame.transform.scale(background_image_start_screen, (HEIGHT, WIDTH))
avatar_her_image = pygame.image.load("primer/icons/avatar_her.bmp")
signature_text_image = pygame.image.load("primer/images/texts/signature_text.bmp")

#CATS
cat_man_image = pygame.image.load("primer/images/cats/cat_man.bmp")
cat_with_bubble_tea_image = pygame.image.load("primer/images/cats/cat_with_bubble_tea.bmp")
eat_cat_image = pygame.image.load("primer/images/cats/eat_cat.bmp")
love_cat_image = pygame.image.load("primer/images/cats/love_cat.bmp")
sad_cat_image = pygame.image.load("primer/images/cats/sad_cat.bmp")
sleep_cat_image = pygame.image.load("primer/images/cats/sleep_cat.bmp")
sleep_bed_cat_image = pygame.image.load("primer/images/cats/sleep_bed_cat.bmp")
sit_cat_image = pygame.image.load("primer/images/cats/sit_cat.bmp")
cat_info_image = pygame.image.load("primer/images/cats/cat_info.bmp")
cat_eat_fish_image = pygame.image.load("primer/images/cats/cat_eat_fish.bmp")
sad_cry_cat_image = pygame.image.load("primer/images/cats/sad_cry_cat.bmp")
thinking_cat_image = pygame.image.load("primer/images/cats/thinking_cat.bmp")
happy_cat_image = pygame.image.load("primer/images/cats/happy_cat.bmp")
dubbing_cat_image = pygame.image.load("primer/images/cats/dubbing_cat.bmp")
chill_out_cat_image = pygame.image.load("primer/images/cats/chill_out_cat.bmp")
#BUTTONS SETTINGS

#BUTTON EXIT SETTINGS
exit_image = pygame.image.load("primer/images/buttons/button_exit.bmp")
exit_rect = exit_image.get_rect()
exit_rect.topleft = (WIDTH + 150, 20)
#BUTTON SETTINGS
settings_image = pygame.image.load("primer/images/buttons/button_settings.bmp")
settings_rect = settings_image.get_rect()
settings_rect.topleft = (WIDTH + 60, 20)
#BUTTON START SETTINGS
start_image = pygame.image.load("primer/images/buttons/button_start.bmp")
start_rect = start_image.get_rect()
start_rect.topleft = (WIDTH - 640, 500)
#BUTTON START SETTINGS IN INFO SCREEN
start_image_info = pygame.image.load("primer/images/buttons/button_start.bmp")
start_rect_info = start_image.get_rect()
start_rect_info = start_image.get_rect()
start_rect_info.topleft = (WIDTH - 640, 700)
#BUTTON RETURN START SETTINGS
return_start_image = pygame.image.load("primer/images/buttons/button_return_start.bmp")
return_start_rect = start_image.get_rect()
return_start_rect.topleft = (20,20)
#BUTTON TRY_AGAIN SETTINGS
try_again_image = pygame.image.load("primer/images/buttons/button_try_again.bmp")
try_again_rect = try_again_image.get_rect()
try_again_rect.topleft = (WIDTH - 640, 700)

#PAUSE SETTINGS
pause = False
#BUTTON PAUSE SETTINGS
pause_image = pygame.image.load("primer/images/buttons/button_pause.bmp")
pause_rect = pause_image.get_rect()
pause_rect.topleft = (WIDTH + 60, 20)
#BUTTON CONTINUE SETTINGS
con_game_image = pygame.image.load("primer/images/buttons/button_continue_game.bmp")
con_game_rect = con_game_image.get_rect()
con_game_rect.topleft = (WIDTH - 640,700)
#BUTTON MUTE SETTINGS
of_after_click = False #czy po kliknięciu
of_after_click_2 = False #czy po kliknięciu

mute_image = pygame.image.load("primer/images/buttons/button_mute.bmp")
continue_song_image = pygame.image.load("primer/images/buttons/button_continue_song.bmp")

#mute_image_2 = pygame.image.load("primer/images/buttons/button_mute.bmp")
#continue_song_image_2 = pygame.image.load("primer/images/buttons/button_continue_song.bmp")

current_image = mute_image #obecny_obrazek
current_image_rect = current_image.get_rect()
current_image_rect.topleft = (WIDTH - 30, 20)

current_image_rect_2 = current_image.get_rect()
current_image_rect_2.topleft = (WIDTH + 60, 20)

#current_image_2 = mute_image_2 #obecny_obrazek
#current_image_rect_2 = current_image_2.get_rect()
#current_image_rect_2.topleft = (WIDTH - 150, 20)

#BUTTON INFO SETTINGS
info_image = pygame.image.load("primer/images/buttons/button_info.bmp")
info_rect = info_image.get_rect()
info_rect.topleft = (WIDTH - 120, 20)

#OPEN FILES
#OPEN FILE HIGHEST_SCORE.TXT
with open("primer/documents/highest_score.txt","r") as highest_score:
    contents_file = highest_score.read() #zawartosc_pliku
    contents_file_number = int(contents_file)
    save_highest_score = contents_file_number 

#OPEN FILE HIGHEST_SCORE.TXT
with open("primer/documents/highest_score.txt", "r") as highest_score:
    contents_file = highest_score.read()
    amount_mouse = int(contents_file) // 5