# 逃离王建国 （鸭皇游戏）

import random
import sys
import time
import math
import pygame
import os
from pickleshare import PickleShareDB
from pygame.locals import *

FPS = 60
pygame.init()
window_info = pygame.display.Info()
WINWIDTH = window_info.current_w
WINHEIGHT = window_info.current_h
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GREEN = (24, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

LEFT = 'left'
RIGHT = 'right'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images")

paths = {"fengxiaoyi": os.path.join(IMAGE_PATH, "fengxiaoyi.png"),
         "wangjianguo": os.path.join(IMAGE_PATH, 'wangjianguo.png'),
         "chenwenli": os.path.join(IMAGE_PATH, "chenwenli.png"), # 11/12更新：陈文丽『庇护之子』贴图
         "wangbage": os.path.join(IMAGE_PATH, "wangba.png"), # 王八哥贴图
         "wangyichen": os.path.join(IMAGE_PATH, "wangyichen.png"), # 王轶臣『伞兵之子』贴图
         "jinlaotou": os.path.join(IMAGE_PATH, "jinlaotou.png"), # 金老头『无名之人』贴图
         # "maxiaofang": os.path.join(IMAGE_PATH, 'maxiaofang.png'), # 是谁就不说了，这个可能不会更新
         "wangchouju": os.path.join(IMAGE_PATH, "wangchouju.jpg"), # 王丑菊「万恶之源」贴图
         "sunbin": os.path.join(IMAGE_PATH, "sunbin.jpg"), # 孙斌「孙结冰」贴图 
         "peach": os.path.join(IMAGE_PATH, "peach.png"),
         "grass1": os.path.join(IMAGE_PATH, "grass1.png"),
         "grass2": os.path.join(IMAGE_PATH, "grass2.png"),
         "grass3": os.path.join(IMAGE_PATH, "grass3.png"),
         "grass4": os.path.join(IMAGE_PATH, "grass4.png"),
         'lp': os.path.join(IMAGE_PATH, "lp.png"),
         }
CONFIG_PATH = "~/.duck_game/wang250"


class GameRect(pygame.Rect):
    title = ""
    pos = ()
    size = 0

class Setting:
    def __init__(self, file_name='config', config={}):
        super().__init__()
        self.file_name = file_name
        self.db = PickleShareDB(CONFIG_PATH)
        if file_name not in self.db:
            self.db[file_name] = config

    def add(self, key, value):
        """添加新值"""
        new = self.db[self.file_name]
        if value:
            new[key] = value
            self.db[self.file_name] = new

    def read(self, config=None):
        """读文件"""
        if config:
            return self.db[self.file_name][config]
        return self.db[self.file_name]


setting = Setting()

if "level" not in setting.read():
    setting.add("level", 1)


class Text():
    def init_val(self):
        self.lp = pygame.image.load(paths['lp'])
        self.white_exit = pygame.image.load(paths['white_exit_button'])
        self.black_exit = pygame.image.load(paths['black_exit_button'])
    
    def set_surface(self, surface):
        self.DISPLAYSURF = surface

    def blit_text(self, text_w: str, pos: tuple, size: int = 18, color: tuple = (0, 0, 0), bg: tuple = None, display=None):
        font = pygame.font.SysFont('SimHei', size)
        text = font.render(u"{}".format(text_w), True, color, bg)
        if not display:
            display = self.DISPLAYSURF
        display.blit(text, pos)
        rect = GameRect(pos[0], pos[1], size * len(text_w), size)
        rect.title = text_w
        rect.pos = pos
        return rect

    def message(self, text: str):
        win_info = pygame.display.Info()
        cio = 0
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.DISPLAYSURF.fill((0, 0, 0))
            self.blit_text(text, (win_info.current_w / 4, win_info.current_h / 2), 50)
            if cio == 0:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (255, 255, 255), (0, 0, 0))
            else:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (0, 0, 0), (255, 255, 255))
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255),
                        (win_info.current_w / 4 - 30, win_info.current_h / 2 - 20, len(text) * 50 + 30, 200), 5)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
            if yes.collidepoint(mouse_pos[0], mouse_pos[1]):
                cio = 1
            else:
                cio = 0
            if pygame.mouse.get_pressed()[0] and cio == 1:
                time.sleep(0.5)
                return True
            self.DISPLAYSURF.blit(self.lp, mouse_pos)
            pygame.display.update()
    
    def ask_yes_no(self, text: str):
        win_info = pygame.display.Info()
        cio = 0
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.DISPLAYSURF.fill((0, 0, 0))
            self.blit_text(text, (win_info.current_w / 4, win_info.current_h / 2), 72)
            if cio != 1:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (255, 255, 255), (0, 0, 0))
            elif cio == 1:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (0, 0, 0), (255, 255, 255))
            if cio != 2:
                no = self.blit_text("取消", (win_info.current_w / 6 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (255, 255, 255), (0, 0, 0))
            elif cio == 2:
                no = self.blit_text("取消", (win_info.current_w / 6 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (0, 0, 0), (255, 255, 255))
            pygame.draw.rect(self.DISPLAYSURF, (255, 255, 255),
                        (win_info.current_w / 4 - 30, win_info.current_h / 2 - 20, len(text) * 72 + 30, 200), 5)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
            if yes.collidepoint(mouse_pos[0], mouse_pos[1]):
                cio = 1
            elif no.collidepoint(mouse_pos[0], mouse_pos[1]):
                cio = 2
            else:
                cio = 0
            if pygame.mouse.get_pressed()[0]:
                if cio == 1:
                    return True
                elif cio == 2:
                    return False
            self.DISPLAYSURF.blit(self.lp, mouse_pos)
            pygame.display.update()

class RunGame(Text):
    
    def __init__(self, display: pygame.Surface):
        self.DISPLAYSURF = display
        self.set_surface(self.DISPLAYSURF)
        self.player_img = pygame.image.load(paths[setting.read("player")])

    def begin_timmer(self):
        for i in range(4, 0, -1):
            self.DISPLAYSURF.fill(GREEN)
            self.blit_text(f"准备开始：{i}", (HALF_WINWIDTH, HALF_WINHEIGHT), 75)
            pygame.display.update()
            pygame.time.wait(1000)
                

    def start(self):
        self.begin_timmer()
        x, y = 70, 70
        while True:
            self.DISPLAYSURF.fill(GREEN)
            self.DISPLAYSURF.blit(self.player_img, (x, y))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
                
            pygame.display.update()


def play(surface):
    RunGame(surface).start()

if __name__ == '__main__':
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    play(DISPLAYSURF)
