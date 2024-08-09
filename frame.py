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
        self.icon_back = pygame.image.load('img/iconBack.png')
        self.icon_skip = pygame.image.load('img/iconSkip.png')


        self.width, self.height = WIDTH, HEIGHT
        self.play_button = utils.button.Button(self.screen, self.x + 380, self.y + 550, self.icon_pause, self.play_button_callback)
        self.choose_button = utils.button.Button(self.screen, self.x + 420, self.y + 550, self.icon_skip, self.change_song_button_callback)
        self.back_button = utils.button.Button(self.screen, self.x + 340, self.y + 550, self.icon_back, self.go_back_button_callback)
        self.current_song_index = 0
    def draw(self):
        self.play_button.draw()
        self.choose_button.draw()
        self.back_button.draw()

    def update(self):
        self.play_button.update()
        self.choose_button.update()
        self.back_button.update()

    def play_button_callback(self):
        self.app.music_player.pause_unpause_song()
        if self.app.music_player.is_song_paused():
            self.play_button.icon = self.icon_pause
        else:
            self.play_button.icon = self.icon_play


    def change_song_button_callback(self):
        # Increment the current song index
        self.current_song_index = (self.current_song_index + 1) % len(self.app.Songs)

        self.play_button.icon = self.icon_pause

        # Play the new song
        self.app.music_player.play_song(self.app.Songs[self.current_song_index])


    def go_back_button_callback(self):

        self.current_song_index = (self.current_song_index - 1) % len(self.app.Songs)

        self.play_button.icon = self.icon_pause

        self.app.music_player.play_song(self.app.Songs[self.current_song_index])

