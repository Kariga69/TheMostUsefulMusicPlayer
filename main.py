import pygame
from settings import *
from player import MusicPlayer
from frame import Frame


# All the config is in settings.py file.

class App:
    Songs = ['./music/example.mp3', './music/Electrified.mp3', './music/FTL.mp3']  # List of songs to play.
    def __init__(self):
        self.screen = pygame.display.set_mode(RES)  # Define the screen and its resolution.
        pygame.display.set_caption(TITLE)  # Set the title of the window.

        self.clock = pygame.time.Clock()  # Utilize a clock to control the FPS.
        self.deltaTime = 0  # Define delta time for FPS calculation.

    # Updates every {FPS} frames/
    def update(self):
        self.deltaTime = self.clock.tick(FPS)
        pygame.display.update()
        self.frame.update()
        print(f"PLAYER PAUSED : {self.music_player.is_song_paused()}")

    # Used only for drawing.
    def draw(self):
        self.frame.draw()

    def base_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    # Run this function to start of the program.
    def run(self):

        self.music_player = MusicPlayer()
        self.frame = Frame(self)
        self.music_player.play_song(self.Songs[0])
        while True:
            self.base_events()
            self.draw()
            self.update()


if __name__ == "__main__":
    app = App()
    app.run()
