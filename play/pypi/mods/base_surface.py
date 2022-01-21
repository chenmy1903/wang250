from .mod_tools import Text, Setting, GameRect

import pygame

from pygame.locals import QUIT

class UI(Text):
    """一些ui组件"""

    def __init__(self):
        Text.__init__(self)
    
    def button(self, text: str, pos: tuple, size: int = 18):
        x, y = pygame.mouse.get_pos()
        if pygame.Rect(pos[0], pos[1], size * len(text), size).collidepoint(x, y):
            return Button(self.blit_text(text, pos, size, (0, 0, 0), (255, 255, 255)))
        else:
            return Button(self.blit_text(text, pos, size, (255, 255, 255), (0, 0, 0)))

class Button(object):
    """按钮事件类"""

    def __init__(self, button: GameRect):
        object.__init__(self)
        self.button = button

    def is_hold(self):
        """获取按钮是否按下"""
        x, y = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            return self.button.collidepoint(x, y)


class Window(Text):
    """主窗口类
    WARNING: 请不要在Python Shell中运行，这会让这个程序崩溃
    """

    def __init__(self, surface: pygame.Surface, mod_config: Setting):
        """初始化Window类
        surface为游戏运行中的主窗口，可用pygame.display.set_mode代替
        mod_config 为模组设置，通常为mods.mod_tools.Setting或继承他的对象
        """
        self.config = mod_config
        self.surface = surface
        self.set_surface(self.surface)

    def start(self):
        """运行事例程序
        WARNING: 请不要在Python Shell中运行，这会让这个程序崩溃"""
        game_mode = True
        while game_mode:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_mode = False
            pygame.display.update()
            self.clock.tick(self.FPS)
