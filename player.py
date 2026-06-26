import pygame
from settings import *

class Player:

    def __init__(self):
        self.rect = pygame.Rect(100,400,PLAYER_WIDTH,PLAYER_HEIGHT)

        self.velocity_y = 0
        self.on_ground = False

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED

        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED

        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y

        if self.rect.bottom >= 520:
            self.rect.bottom = 520
            self.velocity_y = 0
            self.on_ground = True
        else:
            self.on_ground = False

        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity_y = JUMP_POWER

    def draw(self,screen):
        pygame.draw.rect(screen,(255,50,50),self.rect)
