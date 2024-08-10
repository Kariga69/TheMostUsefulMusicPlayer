from settings import *
import pygame
import utils.button
import os
import time


class Frame:

    def __init__(self, app):

        self.app = app
        self.screen: pygame.Surface = app.screen
        self.x, self.y = 0, 0
        self.current_song_name = "example.mp3"


        self.icon_pause = pygame.image.load('img/iconPause.png')
        self.icon_play = pygame.image.load('img/iconPlay.png')
        self.icon_back = pygame.image.load('img/iconBack.png')
        self.icon_skip = pygame.image.load('img/iconSkip.png')


        self.width, self.height = WIDTH, HEIGHT
        self.play_button = utils.button.Button(self.screen, self.x + 380, self.y + 550, self.icon_pause, self.play_button_callback)
        self.choose_button = utils.button.Button(self.screen, self.x + 420, self.y + 550, self.icon_skip, self.change_song_button_callback)
        self.add_song_button = utils.button.Button(self.screen, self.x + 460, self.y + 550, self.icon_skip, self.add_song_button_callback)
        self.back_button = utils.button.Button(self.screen, self.x + 340, self.y + 550, self.icon_back, self.go_back_button_callback)
        self.add_folder_button = utils.button.Button(self.screen, self.x + 500, self.y + 550, self.icon_back, self.add_folder_button_callback)
        self.current_song_index = 0
    def draw(self):
        self.play_button.draw()
        self.choose_button.draw()
        self.back_button.draw()
        self.add_song_button.draw()
        self.add_folder_button.draw()
        rect_width = 800
        rect_height = 50
        rect_x = self.x
        rect_y = self.y + 490
        pygame.draw.rect(self.screen, (0, 0, 0, 128), (rect_x, rect_y, rect_width, rect_height))
        text_surface = pygame.font.SysFont('Arial', 20).render(self.current_song_name, True, (255, 255, 255))

        # Center the text within the rectangle
        text_rect = text_surface.get_rect(center=(rect_x + rect_width // 2, rect_y + rect_height // 2))
        self.screen.blit(text_surface, text_rect)


    def update(self):
        self.play_button.update()
        self.choose_button.update()
        self.back_button.update()
        self.add_song_button.update()
        self.add_folder_button.update()

    def play_button_callback(self):
        self.app.music_player.pause_unpause_song()
        if self.app.music_player.is_song_paused():
            self.play_button.icon = self.icon_pause
        else:
            self.play_button.icon = self.icon_play

    def clear_song_name(self):
        self.current_song_name = ""

    def change_song_button_callback(self):
        # Increment the current song index
        self.current_song_index = (self.current_song_index + 1) % len(self.app.Songs)

        self.play_button.icon = self.icon_pause

        # Play the new song
        self.app.music_player.play_song(self.app.Songs[self.current_song_index])

        self.app.music_player.play_song(self.app.Songs[self.current_song_index])
        self.current_song_name = os.path.basename(self.app.Songs[self.current_song_index])


    def go_back_button_callback(self):

        self.current_song_index = (self.current_song_index - 1) % len(self.app.Songs)

        self.play_button.icon = self.icon_pause

        self.app.music_player.play_song(self.app.Songs[self.current_song_index])
        self.current_song_name = os.path.basename(self.app.Songs[self.current_song_index])

    def add_song_button_callback(self):
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(initialdir="./", title="Choose an audio file",
                                               filetypes=(("Audio Files", "*.mp3;*.wav"),))
        root.destroy()

        if file_path:
            self.app.add_song(file_path)
            self.current_song_name = os.path.basename(file_path)
            self.current_song_index = len(self.app.Songs) - 1


    def add_folder_button_callback(self):
        pass

    def add_song(self):
        # Update the song list in the App class
        self.app.update_song_list()






