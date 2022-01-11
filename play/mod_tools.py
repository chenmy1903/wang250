import os
import sys
import requests
import pygame

from pickleshare import PickleShareDB

TITLE = "mod_tools"
run_on_load = True

def cmd_text(text: str, end_function=None):
    text_r = text.replace('\n', '-')
    run_path = os.path.join(sys.exec_prefix, "python.exe")
    os.system(f"start {run_path} -c \"text = '''{text_r}'''; print(text.replace('-', '\\n')); input('Enter关闭本窗口')\"")
    if end_function:
        end_function()


class Setting:
    def __init__(self, file_name, config={}, config_path="~/.duck_game/wang250/mods"):
        super().__init__()
        self.file_name = file_name
        self.db = PickleShareDB(config_path)
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

class Text:
    clock = pygame.time.Clock()
    FPS = Setting().read("fps")
    
    def set_surface(self, surface):
        self.DISPLAYSURF = surface

    def blit_text(self, text_w: str, pos: tuple, size: int = 18, color: tuple = (255, 255, 255), bg: tuple = None, display=None):
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

def run_mod():
    pass
