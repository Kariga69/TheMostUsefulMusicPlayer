from settings import *
import pygame


# Simple music player that supports loading songs, pausing, resuming, and adjusting volume.
# To change anything, look into main.py file.
# To edit things like start volume, go to settings.py file.

class MusicPlayer:

    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.set_volume(START_VOLUME)

    def play_song(self, song_path):
        pygame.mixer.music.load(song_path)
        pygame.mixer.music.play()

    def stop_song(self):
        pygame.mixer.music.stop()

    def change_volume(self, volume):
        pygame.mixer.music.set_volume(volume)

    def pause_unpause_song(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    def is_song_paused(self):
        return pygame.mixer.music.get_busy()
