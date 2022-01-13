"""mods的测试组件"""
# by 鸭皇
# ©chenmy1903
# GitHub: 王建国

from mods.base_surface import Window

import pygame
import sys

def test(window: Window):
    pygame.init()
    window_info = pygame.display.Info()
    w, h = window_info.current_w, window_info.current_h
    surface = pygame.display.set_mode((w, h))
    pygame.display.set_caption("test window")
    exec_win = window(surface, "test_config")
    exec_win.start()
    sys.exit()

if __name__ == '__main__':
    test(Window)
