from settings import *
import pygame
import utils.button


class Frame:

    def __init__(self, app):
        self.app = app
        self.screen: pygame.Surface = app.screen
        self.x, self.y = 0, 0

        self.icon_pause = pygame.image.load('img/iconPause.png')
        self.icon_play = pygame.image.load('img/iconPlay.png')

        self.width, self.height = WIDTH, HEIGHT
        self.play_button = utils.button.Button(self.screen, self.x + 20, self.y + 20, self.icon_pause, self.play_button_callback)

    def draw(self):
        self.play_button.draw()

    def update(self):
        self.play_button.update()

    def play_button_callback(self):
        self.app.music_player.pause_unpause_song()
        if self.app.music_player.is_song_paused():
            self.play_button.icon = self.icon_pause
        else:
            self.play_button.icon = self.icon_play