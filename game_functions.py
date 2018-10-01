import sys
import pygame

#############################KeyEvents###################################################
def check_key_events(screen,settings,ball,player,play_button,stats):
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            sys.exit()

        elif event.type == pygame.KEYDOWN:

            check_keydown(event,player)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,screen,settings,player)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            match_start( ball, play_button, stats, mouse_x, mouse_y)



def check_keydown(event,player,):
    if event.key == pygame.K_RIGHT:

        player.movingright = True

    elif event.key == pygame.K_LEFT:

        player.movingleft = True

    elif event.key== pygame.K_UP:

        player.movingup=True

    elif event.key== pygame.K_DOWN:

        player.movingdown=True


    elif event.key == pygame.K_q:

        sys.exit()
def match_start(ball,play_button,stats,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

    if button_clicked and not stats.game_active:

        stats.reset_stats()

        stats.game_active = True
        ball.ball_reset()
        ball.start_game()





def check_keyup_events(event,screen,settings,player):
    if event.key == pygame.K_RIGHT:

        player.movingright = False

    elif event.key == pygame.K_LEFT:

        player.movingleft = False

    elif event.key == pygame.K_UP:

        player.movingup = False

    elif event.key == pygame.K_DOWN:

        player.movingdown = False


#########################Updates################################################
def update_ball(ball,player,enemy):
    ball.update()
    collision_check(ball,player,enemy)

def collision_check(ball,player,enemy):

    #Update when player hits
    if ball.rect.colliderect(player.main_paddle):
        ball.x_velocity*= -1.2
        ball.rect.centerx += ball.x_velocity
        ball.rect.centery += ball.x_velocity/2
    if ball.rect.colliderect(player.top_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
    if ball.rect.colliderect(player.bottom_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity

    #Update when enemy hits
    if ball.rect.colliderect(enemy.main_paddle):
        ball.x_velocity*= -1.2
        ball.rect.centerx += ball.x_velocity
        ball.rect.centery += ball.x_velocity/2
    if ball.rect.colliderect(enemy.top_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
    if ball.rect.colliderect(enemy.bottom_paddle):
        ball.y_velocity *=-1
        ball.rect.centery += ball.y_velocity
        

def update_screen(screen,settings,ball,player,enemy,play_button,stats):
    screen.fill(settings.color_bg)
    player.drawmidfield()
    player.drawplayer()
    enemy.drawplayer()
    ball.blit_ball()

    if not stats.game_active:
        play_button.draw_button()
    pygame.display.flip()