import pygame
from pygame.sprite import Sprite
from settings import Settings
class Player(Sprite):
    def __init__(self,screen,settings):
        super(Player,self).__init__()

        self.screen_player = screen
        self.settings_player=settings
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
        self.main_paddle.midleft=self.screen_rect.midleft


        self.top_paddle.centerx=self.screen_rect.centerx
        self.top_paddle.topleft=self.screen_rect.topleft

        self.bottom_paddle.centerx=self.screen_rect.centerx
        self.bottom_paddle.bottomleft=self.screen_rect.bottomleft


        self.center=float(self.main_paddle.centery)
        self.centertop=float(self.top_paddle.centerx)
        self.centerbottom=float(self.bottom_paddle.centerx)

        self.movingup=False
        self.movingdown=False
        self.movingleft=False
        self.movingright=False

    def update(self):
        if self.movingup and self.main_paddle.top  > self.screen_rect.top:
            self.center-= self.settings_player.playerspeed
        if self.movingdown and self.main_paddle.bottom < self.screen_rect.bottom:
            self.center += self.settings_player.playerspeed
        if self.movingright and self.top_paddle.right < self.screen_rect.right/2:
            self.centertop += self.settings_player.playerspeed
        if self.movingleft and self.top_paddle.left > 0:
            self.centertop -= self.settings_player.playerspeed
        if self.movingright and self.bottom_paddle.right < self.screen_rect.right/2:
            self.centerbottom += self.settings_player.playerspeed
        if self.movingleft and self.bottom_paddle.left > 0:
            self.centerbottom -= self.settings_player.playerspeed

        self.main_paddle.centery=self.center
        self.top_paddle.centerx=self.centertop
        self.bottom_paddle.centerx=self.centerbottom
    def drawplayer(self):
            pygame.draw.rect(self.screen_player,self.settings_player.playercolor,self.main_paddle)
            pygame.draw.rect(self.screen_player, self.settings_player.playercolor, self.top_paddle)
            pygame.draw.rect(self.screen_player, self.settings_player.playercolor, self.bottom_paddle)
    def drawmidfield(self):
        pygame.draw.rect(self.screen_player,self.settings_player.centerlinecolor,self.midfield)
