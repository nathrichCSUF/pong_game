import pygame
import math
import random
from pygame.sprite import Sprite
from settings import Settings
class Ball(Sprite):
    def __init__(self,screen,settings):
        super(Ball, self).__init__()

        self.image=pygame.image.load('ball.png')
        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.rect=self.image.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.centery=self.screen_rect.centery



        self.startspeed=5

        self.x_velocity=0
        self.y_velocity=0

    def blit_ball(self):
        self.screen.blit(self.image,self.rect)
    def start_game(self):
        rand_angle=random.randint(-45,45)

        if abs(rand_angle) < 5 or abs(rand_angle-180 < 5):
            rand_angle=random.randint(10,20)
        if random.random() > .5:
            rand_angle +=180
        x=math.cos(math.radians(rand_angle))
        y= math.sin(math.radians(rand_angle))

        self.x_velocity= x * self.startspeed
        self.y_velocity=y * self.startspeed

    def ball_reset(self):
        self.x_velocity = 0
        self.y_velocity = 0
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def update(self):
        self.rect.centerx +=self.x_velocity
        self.rect.centery += self.y_velocity

