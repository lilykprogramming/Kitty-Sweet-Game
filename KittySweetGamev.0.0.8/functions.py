"""
GAME: KITTY SWEET GAME

AUTHOR: LILYKPROGRAMMING

- functions:

- style_start_screen,
- style_end_screen,
- style_info_screen.

"""

#Import and initialization library pygame.
import pygame
#Import module mechanic
import mechanic
#Import module elements
import elements as e
#FUNCTION style_start_screen
def style_start_screen():
    #MOUSE VISIBLE
    pygame.mouse.set_visible(True)
    #FONTS
    font = pygame.font.SysFont(None,30)
    font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 200)
    font_description = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
    #TITLE
    title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
    title_rect = title_text.get_rect(center=(mechanic.HEIGHT //2,mechanic.WIDTH //3))
    #DESCRIPTION
    description_text1 = font_description.render('Kitty catching mice', False,mechanic.white)
    description_rect1 = description_text1.get_rect(center=(mechanic.HEIGHT // 2, 800))
    #SCREEN BLIT
    e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
    e.screen_game.blit(title_text, title_rect)
    e.screen_game.blit(description_text1, description_rect1)
#FUNCTION style_end_screen
def style_end_screen(points, save_highest_score):
    if save_highest_score > points:
        #MOUSE VISIBLE
        pygame.mouse.set_visible(True)
        #FONTS
        font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 100)
        font_description = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
        font = pygame.font.SysFont(None,250)
        #TITLE
        title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
        title_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//9))

        game_over_text = font.render('GAME OVER',False, mechanic.white)
        game_over_rect = game_over_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//3))

        #DESCRIPTION
        description_text1 = font_description.render(f"Final score: {points} points.  Highest score: {save_highest_score} points", False,mechanic.white)
        description_text2 = font_description.render(f"Congratulation! You have caught {points//5} mice!", False,mechanic.white)
        description_rect1 = description_text1.get_rect(center=(mechanic.HEIGHT // 2, 500))
        description_rect2 = description_text2.get_rect(center=(mechanic.HEIGHT // 2, 550))
        #SCREEN BLIT
        e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
        e.screen_game.blit(mechanic.sad_cry_cat_image,(1200,500))
        e.screen_game.blit(mechanic.thinking_cat_image,(-20,500))
        e.screen_game.blit(title_text, title_rect)
        e.screen_game.blit(game_over_text, game_over_rect)
        e.screen_game.blit(description_text1, description_rect1)
        e.screen_game.blit(description_text2, description_rect2)
    else:
        #MOUSE VISIBLE
        pygame.mouse.set_visible(True)
        #FONTS
        font = pygame.font.SysFont(None,250)
        font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 100)
        font_description = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
        #TITLE
        title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
        title_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//9))

        game_over_text = font.render('GAME OVER',False, mechanic.white)
        game_over_rect = game_over_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//3))
        #DESCRIPTION
        description_text1 = font_description.render(f"You won: {save_highest_score} points!", False,mechanic.white)
        description_text2 = font_description.render(f"Congratulation! You have caught {points//5} mice!.", False,mechanic.white)
        description_rect1 = description_text1.get_rect(center=(mechanic.HEIGHT // 2, 500))
        description_rect2 = description_text2.get_rect(center=(mechanic.HEIGHT // 2, 550))
        #SCREEN BLIT
        e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
        e.screen_game.blit(mechanic.happy_cat_image,(1200,500))
        e.screen_game.blit(mechanic.thinking_cat_image,(-20,500))
        e.screen_game.blit(title_text, title_rect)
        e.screen_game.blit(game_over_text, game_over_rect)
        e.screen_game.blit(description_text1, description_rect1)
        e.screen_game.blit(description_text2, description_rect2)
#FUNCTION style_info_screen
def style_info_screen():
    pygame.mouse.set_visible(True)
    #FONTS
    font = pygame.font.SysFont(None, 50)
    return_start_font = pygame.font.SysFont(None, 40)
    info_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
    title_info_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 50)
    #TITLE GAME
    font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 100)
    title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
    title_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//9))
    #TITLE INFORMATION
    title_info_text = title_info_font.render('Game Information',False, mechanic.white)
    title_info_rect = title_text.get_rect(center=(mechanic.HEIGHT//1.9,mechanic.WIDTH//4))
    #TEXT INFORMATION
    info_text = info_font.render('You must catch the most mice for the hungry kitty..', False, mechanic.white)
    info_rect = info_text.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 3))
    description_text = info_font.render('You only need a mouse to play the game.', False, mechanic.white)
    description_rect = info_text.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 2.7))
    description_text2 = info_font.render('Author: Lilykprogramming', False, mechanic.white)
    description_rect2 = info_text.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 2.4))
    description_text1 = info_font.render('Have fun :)', False, mechanic.white)
    description_rect1 = info_text.get_rect(center=(mechanic.HEIGHT // 1, mechanic.WIDTH // 2.2))
    #SCREEN BLIT
    e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
    e.screen_game.blit(title_info_text, title_info_rect)
    e.screen_game.blit(title_text, title_rect)
    e.screen_game.blit(description_text, description_rect)
    e.screen_game.blit(description_text1, description_rect1)
    e.screen_game.blit(description_text2, description_rect2)
    e.screen_game.blit(info_text, info_rect)
def style_settings_screen():
    pygame.mouse.set_visible(True)
    #FONTS
    font = pygame.font.SysFont(None, 50)
    return_start_font = pygame.font.SysFont(None, 40)
    settings_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
    title_settings_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 50)
    #TITLE GAME
    font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 100)
    title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
    title_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//9))
    #TITLE INFORMATION
    title_settings_text = title_settings_font.render('Settings Game',False, mechanic.white)
    title_settings_rect = title_text.get_rect(center=(mechanic.HEIGHT//1.85,mechanic.WIDTH//4))
    #TEXT INFORMATION
    settings_text = settings_font.render('The game settings are being built.', False, mechanic.white)
    settings_rect = settings_text.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 3))
    #SCREEN BLIT
    e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
    e.screen_game.blit(title_settings_text, title_settings_rect)
    e.screen_game.blit(title_text, title_rect)
    e.screen_game.blit(settings_text, settings_rect)
def style_continue_screen():
    pygame.mouse.set_visible(True)
    #FONTS
    font = pygame.font.SysFont(None, 50)
    fact_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 30)
    title_settings_font = pygame.font.Font("primer/fonts/Aleo-Regular.ttf", 100)
    #TITLE GAME
    font_title = pygame.font.Font("primer/fonts/BigShouldersDisplay-Light.ttf", 100)
    title_text = font_title.render('KITTY SWEET GAME',False, mechanic.white)
    title_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//9))
    #TITLE INFORMATION
    title_settings_text = title_settings_font.render('Continue?',False, mechanic.white)
    title_settings_rect = title_text.get_rect(center=(mechanic.HEIGHT//2,mechanic.WIDTH//4))
    #TEXT INFORMATION
    fact_text = fact_font.render('Cats sleep for around 13 to 16 hours a day (70% of their life).', False, mechanic.white)
    fact_rect = fact_text.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 2.7))

    fact_text_2 = fact_font.render('There are over 500 million pet cats!', False, mechanic.white)
    fact_rect_2 = fact_text_2.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 2.3))

    fact_text_3 = fact_font.render('The oldest cat was 38 years old.', False, mechanic.white)
    fact_rect_3 = fact_text_3.get_rect(center=(mechanic.HEIGHT // 2, mechanic.WIDTH // 2))

    #SCREEN BLIT
    e.screen_game.blit(mechanic.background_image_start_screen,(0, 0))
    e.screen_game.blit(mechanic.dubbing_cat_image,(1200,500))
    e.screen_game.blit(mechanic.chill_out_cat_image,(-40,300))
    e.screen_game.blit(title_settings_text, title_settings_rect)
    e.screen_game.blit(title_text, title_rect)
    e.screen_game.blit(fact_text, fact_rect)
    e.screen_game.blit(fact_text_2, fact_rect_2)
    e.screen_game.blit(fact_text_3, fact_rect_3)