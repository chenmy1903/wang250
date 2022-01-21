from mods.mod_tools import Setting
from mods.test import test
from mods.base_surface import Window, UI

from pygame.locals import *

import pygame
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TITLE = "音频播放器"
run_on_load = False

config = Setting(TITLE)

class SoundWindow(Window):
    def __init__(self, surface: pygame.Surface, config: Setting):
        Window.__init__(self, surface, config)
        self.play_time = config.try_get("time", -1) * 60
        self.bgm = config.null_add("bgm_path", os.path.join(BASE_DIR, "sound.mp3"))
        self.game_mode = True
        self.ui = UI()
        self.ui.set_surface(surface)
    
    def start(self):
        pygame.mixer.music.load(self.sound)
        while self.game_mode:
            self.blit_text("音频播放器", (20, 20), 72)
            play_button = self.ui.button("播放", [20, 120], 35)
            stop_button = self.ui.button("停止", [120, 120], 35)
            if play_button.is_hold():
                pygame.mixer.music.play()
            elif stop_button.is_hold():
                pygame.mixer.music.stop()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.game_mode = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.game_mode = False
            pygame.display.update()
            self.clock.tick(self.FPS)

            

if __name__ == "__main__":
    test(SoundWindow, config)
