import sys
import pygame

import game_functions as GF
from settings import Settings
from ball import Ball
from player import Player
from enemy import Enemy
from button import Button
from stats import Stats

def run_game():
    pygame.init()
    pygame.display.set_caption('4-Sided Pong')
    settings=Settings()
    screen=pygame.display.set_mode((settings.screenwidth, settings.screenheight))
    ball=Ball(screen,settings)
    player = Player(screen,settings)
    enemy= Enemy(screen,settings,ball)
    play_button=Button(screen,"Play")
    stats=Stats()



    #ball.start_game()
    while True:
        GF.check_key_events(screen,settings,ball,player,play_button,stats)

        if stats.game_active:

            player.update()
            enemy.update()
            GF.update_ball(ball,player,enemy)
        GF.update_screen(screen,settings,ball,player,enemy,play_button,stats)

run_game()