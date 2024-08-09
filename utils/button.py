import pygame
from settings import *


class Button:

    def __init__(self, screen, x, y, icon, callback):
        self.screen = screen
        self.x = x
        self.y = y
        self.isClicked = False
        self.background_clicked = pygame.image.load('img/buttonClicked.png')
        self.background_normal = pygame.image.load('img/buttonNormal.png')
        self.icon = icon
        self.callback = callback
        self.rect = self.background_normal.get_rect(topleft=(self.x, self.y))

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
            self.isClicked = True
        if not pygame.mouse.get_pressed()[0] and self.isClicked:
            self.callback()
            self.isClicked = False

    def draw(self):
        if self.isClicked:
            self.screen.blit(self.background_clicked, self.rect)
        else:
            self.screen.blit(self.background_normal, self.rect)

        self.screen.blit(self.icon, (self.rect.x + 2, self.rect.y + 2))
