from .mod_tools import Text, Setting

import pygame

from pygame.locals import QUIT

class Window(Text):
    """主窗口类"""

    def __init__(self, surface: pygame.Surface, mod_config: Setting):
        """初始化Window类
        surface为游戏运行中的主窗口，可用pygame.display.set_mode代替
        mod_config 为模组设置，通常为mods.mod_tools.Setting或继承他的对象
        """
        self.config = mod_config
        self.surface = surface
        self.set_surface(self.surface)

    def start(self):
        while True:
            self.surface.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(self.FPS)
