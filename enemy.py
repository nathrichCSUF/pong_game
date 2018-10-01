import pygame
from pygame.sprite import Sprite
from settings import Settings
class Enemy(Sprite):
    def __init__(self,screen,settings,ball):
        super(Enemy,self).__init__()

        self.screen_player = screen
        self.settings_enemy=settings
        self.ball=ball
        #draw center line
        self.midfield=pygame.Rect(0,0,settings.sidewidth,settings.screenheight)

        #Draw side
        self.main_paddle=pygame.Rect(0,0,settings.sidewidth, settings.sideheight)
        self.screen_rect= self.screen_player.get_rect()

        self.midfield.centerx=self.screen_rect.centerx

        #Draw bottom and top

        self.top_paddle=pygame.Rect(0,0,settings.bottomwidth,settings.bottomheight)
        self.bottom_paddle=pygame.Rect(0,0,settings.bottomwidth,settings.bottomheight)

        #Put  paddles to the left of the screen
        self.main_paddle.centery=self.screen_rect.centery
        self.main_paddle.midright=self.screen_rect.midright


        self.top_paddle.centerx=self.screen_rect.centerx
        self.top_paddle.topright=self.screen_rect.topright

        self.bottom_paddle.centerx=self.screen_rect.centerx
        self.bottom_paddle.bottomright=self.screen_rect.bottomright


        self.center=float(self.main_paddle.centery)
        self.centertop=float(self.top_paddle.centerx)
        self.centerbottom=float(self.bottom_paddle.centerx)

        #Variables to update enemy paddles
        self.AI_main=float(0)
        self.AI_top = float(0)
        self.AI_bottom = float(0)

        self.main_paddle.centery=self.center
        self.top_paddle.centerx=self.centertop
        self.bottom_paddle.centerx=self.centerbottom

        self.movingright=False
        self.movingleft=False
    def main_AI(self):
        if self.main_paddle.centery > self.ball.rect.centery:
            self.AI_main=-1 # go down
        elif self.main_paddle.centery < self.ball.rect.centery:
            self.AI_main = 1#go up

    def top_AI(self):

        if self.top_paddle.centerx > self.ball.rect.centerx:
            self.movingleft = True
            #self.AI_top=-1 # go left
        if self.top_paddle.centerx < self.ball.rect.centerx:
            self.movingright = True
            #self.AI_top =1 # go right

    def bottom_AI(self):
        if self.bottom_paddle.centerx > self.ball.rect.centerx:
            self.movingleft=True
           # self.AI_bottom = -1  # go left
        if self.bottom_paddle.centerx < self.ball.rect.centerx:
            self.movingright = True
            #self.AI_bottom = 1  # go right

    def update(self):
        self.movingright = False
        self.movingleft = False
        #check positions
        self.main_AI()
        self.top_AI()
        self.bottom_AI()
        #move paddles
        self.main_paddle.centery += self.settings_enemy.enemyspeed * self.AI_main
        if self.movingleft and self.top_paddle.left > self.settings_enemy.screenwidth/2:
            self.top_paddle.centerx -= self.settings_enemy.enemyspeed
        if self.movingleft and self.bottom_paddle.left > self.settings_enemy.screenwidth / 2:
            self.bottom_paddle.centerx -= self.settings_enemy.enemyspeed
        if self.movingright:
            self.top_paddle.centerx += self.settings_enemy.enemyspeed
        if self.movingright:
            self.bottom_paddle.centerx += self.settings_enemy.enemyspeed

    def drawplayer(self):
            pygame.draw.rect(self.screen_player,self.settings_enemy.enemycolor,self.main_paddle)
            pygame.draw.rect(self.screen_player, self.settings_enemy.enemycolor, self.top_paddle)
            pygame.draw.rect(self.screen_player, self.settings_enemy.enemycolor, self.bottom_paddle)

