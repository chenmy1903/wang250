# 原创鸭皇游戏
# 官网：https://chenmy1903.github.io/wang250
# --------------------------------------
# 王丑菊伞兵，叫你一天天禁我官网
# 伽卡他卡破解器现在被你搞得都用不了了
# 这东西我做了多久你知道吗
# -----------------------------------------
# 请勿盗用代码！
# 底部为代码部分，请勿盗用！！！

import pygame
import sys
import os
import random
import webbrowser
import importlib
import asyncio
import requests
import time

from pygame.locals import *
from pickleshare import PickleShareDB
from game import play as play_game, paths as game_paths


UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

true = "True"
false = "False"

FPS = 180
speed = 1000
CONFIG_PATH = "~/.duck_game/wang250"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images")
paths = {"fengxiaoyi": os.path.join(IMAGE_PATH, "fengxiaoyi_1.png"),
         "wangjianguo": os.path.join(IMAGE_PATH, 'wangjianguo.png'),
         "bgm": os.path.join(BASE_DIR, 'bgm.mp3'),
         'lp': os.path.join(IMAGE_PATH, "lp.png"),
         'write_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_w.png'),
         'black_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_b.png'),
         'icon': os.path.join(BASE_DIR, "icon.png"),
         }

paths.update(game_paths)

version_text = """
游戏公告

谨防盗版逃离王建国，最近有个叫老八游戏的给盗走了，而且大量修改游戏玩法
11/12更新
1. 模组功能更新
2. 修复对话框点击时会异常跳转的问题
3. 部分界面增加退出按钮，短按返回，长按退出游戏
4. 增加mod_tools.py文件（模组依赖），不需要每次敲入工具代码
5. 修复游戏闪退的bug
6. 修复启动游戏时无法正常加载模组的问题

模组教程：https://chenmy1903.github.io/wang250/mods/make_mod/
11/9更新
1. 修复游戏功能更新（需另下载）
2. 坚果云dat文件解除工具更新（需另下载）
上面所述内容均在下面的网址
下载网址：https://chenmy1903.github.io/wang250/mods/tools

11/6版本更新（上线自动领取更新补偿300钻石）
1. 可恶的王丑菊把我网站给禁了，所以在南大附小无法游玩本游戏（指网络nkdxfsxx）
2. 鸭皇X苏诗朗 ，准备制作模组王建国趋势（去世）模拟器
3. 金古之匙模组预告：
使用金古之匙可以开启王建国的**（自行脑补）游戏会直接获得胜利
4.在爱发电捐款者可以获得一个1000钻石兑换码，并有机会登上官网的感谢榜
5.修复等级可以突破120的bug，并且修复一些情况会误判为外挂的情况
6.在0.4版本入坑的小伙伴请重新下载游戏，因为启动器变更了，旧版本启动器无法启动新版本
7.启动器更完善（不需要重新下载游戏）
0.6还未完成的内容
1.金古之匙模组
2.王八哥『吴汉林』角色祈愿活动
3.王建国趋势（去世）模拟器

0.7预告（2022/2/1更新）
1. 『万恶之源』王丑菊更新
2.春节礼包
3.剧情更新
4.不知道
tip: 所有更新内容以实际更新为准。
"""



def cmd_text(text: str, end_function=None):
    text_r = text.replace('\n', '-')
    run_path = os.path.join(sys.exec_prefix, "python.exe")
    os.system(f"start {run_path} -c \"text = '''{text_r}'''; print(text.replace('-', '\\n')); input('Enter关闭本窗口')\"")
    if end_function:
        end_function()

def download_files():
    if not os.path.isdir(os.path.join(BASE_DIR, 'mods')): # 检测模组文件夹
        os.mkdir(os.path.join(BASE_DIR, 'mods'))
    for key, value in paths.items():
        if not os.path.isfile(value):
            try:
                file_name = value.replace('\\', '/').split('/')[-1]
                r = requests.get(f"https://chenmy1903.github.io/wang250/play/files/{file_name}") # 可恶的王丑菊把我的网站dns禁了，在网站名称为nkdxfsxx的网络下无法正常加载，可恢复到正常网络环境下下载
                if file_name.endswith('.png'):
                    download_path = os.path.join(IMAGE_PATH, file_name)
                else:
                    download_path = os.path.join(BASE_DIR, file_name)
                if not os.path.isdir(IMAGE_PATH):
                    os.mkdir(IMAGE_PATH)
                with open(download_path, 'wb') as f:
                    f.write(r.content)
                
            except:
                cmd_text("下载资源失败，强制退出游戏中...")
                sys.exit()


class Text:
    def init_val(self):
        self.lp = pygame.image.load(paths['lp'])
        self.write_exit = pygame.image.load(paths['write_exit_button'])
        self.black_exit = pygame.image.load(paths['black_exit_button'])
    
    def set_surface(self, surface):
        self.DISPLAYSURF = surface

    def blit_text(self, text_w: str, pos: tuple, size: int = 18, color: tuple = (255, 255, 255), bg: tuple = None):
        font = pygame.font.SysFont('SimHei', size)
        text = font.render(u"{}".format(text_w), True, color, bg)
        self.DISPLAYSURF.blit(text, pos)

def load_mod():
    mod_path = os.path.join(BASE_DIR, "mods")
    package_list = []
    mods = os.listdir(mod_path)
    for package in mods:
        if not package.endswith('.py'):
            continue
        load = importlib.import_module(f"mods.{package.replace('.py','')}")
        if load.run_on_load:
            load.run_mod()
        package_list.append(load)
    
    return package_list



class Blame(Text):
    def __init__(self, images: list, size: tuple, life: int, pos: tuple = (0, 0)):
        super().__init__()
        self.x, self.y = pos
        self.images = images
        self.start_life = life
        self.life = life
        self.__image_n = 1
        self.x = size[0] + 300
        if size[1] < life * 0.002:
            self.y = life * 0.002
        else:
            self.y = size[1]
        self.surface = pygame.Surface((self.x, self.y))
        self.set_surface(self.surface)
        self.surface.blit(images[self.__image_n % len(images) - 1], (0, 20))

    def is_kill(self):
        if self.life <= 0:
            return True

    def get_rect(self):
        return self.surface.get_rect()

    def get_life(self):
        return self.life

    def set_life(self, life: int):
        self.life = life

    def kill(self, life: int):
        self.life -= life

    def update_life(self):
        self.surface.fill((0, 0, 0))
        self.surface.blit(self.images[self.__image_n %
                                      len(self.images) - 1], (300, 0))

    def get_blame(self):
        return self.surface

    def move(self, direction: str):
        self.surface.blit(self.images[self.__image_n %
                                      len(self.images) - 1], (300, 0))
        self.__image_n += 1
        if direction == UP:
            self.x -= 1

    def get_pos(self):
        return self.x, self.y


class WangJianGuo(Blame):
    name = "王建国"
    __set_mod = False

    def update_life(self, surface):
        if not self.__set_mod:
            self.set_surface(surface)
            self.__set_mod = True
        pygame.draw.rect(surface, (255, 255, 255),
                         (400, 20, self.start_life * 0.1, 40), 5)
        pygame.draw.rect(surface, (255, 0, 0),
                         (400, 20, self.life * 0.1, 40))
        self.blit_text(self.name + ":", (230, 20), 40)


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


class Shop(Text):
    def __init__(self, surface, ):
        self.setting = Setting()
        self.names = {}
        self.surface = surface
        self.set_surface(self.surface)

    def start(self):
        add_functions = {}
        num = 1
        self.init_val()
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.surface.fill((0, 0, 0))
            self.blit_text("游戏商城", (580, 100), 75)
            self.blit_text(f"等级:{self.setting.read('level')}", (30, 30), 24)
            self.blit_text(f"金币:{self.setting.read('coins')}", (30, 60), 24)
            self.blit_text(f"钻石:{self.setting.read('diamond')}", (30, 90), 24)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
                    if event.key == K_DOWN:
                        if num < len(add_functions):
                            num += 1
                    elif event.key == K_UP:
                        if num > 1:
                            num -= 1
                    if event.key == K_RETURN:
                        if num == 1:
                            add_functions['level']()
                        if num == 2:
                            add_functions['coins']()
            if num == 1:
                self.blit_text("等级*1 (10000金币)", (200, 200), 35, (0, 0, 0), (255, 255, 255))
                self.blit_text("购买", (300, 250), 35, (0, 0, 0), (255, 255, 255))
            else:
                self.blit_text("等级*1 (10000金币)", (200, 200), 35)
                self.blit_text("购买", (300, 250), 35)

            if num == 2:
                self.blit_text("1000金币 (10钻石)", (600, 200), 35, (0, 0, 0), (255, 255, 255))
                self.blit_text("购买", (700, 250), 35, (0, 0, 0), (255, 255, 255))
            else:
                self.blit_text("1000金币 (10钻石)", (600, 200), 35)
                self.blit_text("购买", (700, 250), 35)
            
            if "level" not in add_functions:
                add_functions["level"] = self.buy_level

            if "coins" not in add_functions:
                add_functions["coins"] = self.buy_coins
            self.DISPLAYSURF.blit(self.lp, mouse_pos)
            pygame.display.update()

    def buy_level(self):
        inter = 10000
        if self.setting.read("level") < 120:
            if self.setting.read("coins") > inter:
                self.setting.add("coins", self.setting.read("coins") - inter)
                self.setting.add("level", self.setting.read("level") + 1)
                self.message("购买成功")
            else:
                self.message("金币不足")
        else:
            self.message("等级已经到顶了，无法升级")

    def buy_coins(self):
        inter = 10
        if self.setting.read("diamond") > inter:
            self.setting.add("diamond", self.setting.read("diamond") - inter)
            self.setting.add("coins", self.setting.read("coins") + 1000)
            self.message("购买成功")
        else:
            self.message("钻石不足")
    
    def message(self, text: str):
        win_info = pygame.display.Info()
        while True:
            self.blit_text(text, (win_info.current_w / 4, win_info.current_h / 2), 72)
            self.blit_text("ESC返回", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40)
            pygame.draw.rect(self.surface, (255, 255, 255),
                        (win_info.current_w / 4 - 30, win_info.current_h / 2 - 20, len(text) * 72 + 30, 200), 5)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
            pygame.display.update()


class JianguoBarbecue:
    def __init__(self):
        self.surface = pygame.Surface()

class GameRect(pygame.Rect):
    title = ""
    pos = ()
    size = 0


class Surf(Text):
    def __init__(self, surface):
        super().__init__()
        self.DISPLAYSURF = surface
        self.init_val() # 修复无法启动的问题
        pygame.mouse.set_visible(False)
        try: # 11/12更新：设定为强制更新
            mod_file = requests.get("https://chenmy1903.github.io/wang250/play/mod_tools.py").text # 下载依赖
            with open(os.path.join(BASE_DIR, 'mods', 'mod_tools.py'), 'w', encode="UTF-8") as f:
                f.write(mod_file)
        except:
            if not os.path.isfile(os.path.join(BASE_DIR, 'mods', 'mod_tools.py')): # 脱机模式检测依赖
                self.message("资源下载失败")
                self.kill_precess()
        try:
            self.mods = load_mod() # 加载模组
        except:
            self.message("模组加载失败")
            self.mods = [] # 设置为空，游戏内显示未加载模组
        self.mouse_pos = (0, 0)
        self.shop_gui = Shop(self.DISPLAYSURF)
        pygame.mixer.music.load(paths["bgm"])
        self.clock = pygame.time.Clock()
        self.setting = Setting()
        if not "coins" in self.setting.read():
            self.setting.add("coins", 300) # 开服礼包 (10/1更新)
        if not "diamond" in self.setting.read():
            self.setting.add("diamond", 1000) # 开服礼包 (10/1更新)
        if not "level" in self.setting.read():
            self.setting.add("level", 1) # 初始化"level"防止调用时出KeyError (10/24更新)
        self.add_settings()
        self.get_gift() # 10/29更新：礼包领取
        pygame.display.set_caption("鸭皇游戏·逃离王建国")
        pygame.display.set_icon(pygame.image.load(paths["icon"]))

    def add_settings(self):
        if not "fengxiaoyi" in self.setting.read():
            self.setting.add("fengxiaoyi", true)
            self.setting.add("player", "fengxiaoyi")
        if not "wangjianguo" in self.setting.read():
            self.setting.add("wangjianguo", false)
    
    def get_gift(self):
        try:
            r = requests.get("https://chenmy1903.github.io/wang250/gift.html")
            gift = r.text
        except:
            return
        if "version" in self.setting.read():
            if self.setting.read("version") != eval(str(gift))["version"]:
                for key, value in eval(str(gift)).items():
                    if isinstance(value, int): # 11/12更新：可以领取角色了
                        self.setting.add(key, self.setting.read(key) + value) # 10/30更新：修复添加数据错误的bug
                    else:
                        self.setting.add(key, value)
        else:
            self.setting.add("version", "0.0")

    def run_game(self):
        try:
            assert self.setting.read(self.setting.read('player'))
            assert self.setting.read(self.setting.read('player')) == true # 11/12更新：修复为false不会判定为外挂
        except (KeyError, AssertionError):
            self.use_wg()
        if self.setting.read("level") > 120:
            self.use_wg()
        pygame.mixer.music.play()
        play_game(self.DISPLAYSURF)
        pygame.mixer.music.stop()

    def use_wg(self):
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.blit_text("检测到你非法修改游戏内数据，奖励你封号1亿年大礼包", (100, 300), 72)
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        self.kill_precess()
                elif event.type == QUIT:
                    self.kill_precess()
            pygame.display.update()

    def buy(self, coin: int):
        old = self.setting.read('coins')
        if old >= coin:
            self.setting.add('coins', old - coin)
            return True

    def shop(self):
        self.shop_gui.start()

    def duck_game(self):
        window_info = pygame.display.Info()
        pygame.mouse.set_visible(True)
        self.DISPLAYSURF.fill((0, 0, 0))
        for i in range(255):
            self.blit_text("鸭皇游戏 | 逃离王建国", (window_info.current_w / 2 - 72 * 5, window_info.current_h / 2 - 100), 72, pygame.Color(255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.kill_precess()
            pygame.display.update()
            self.clock.tick(60)
        pygame.mouse.set_visible(False)

    def run_mods(self):
        count = 1
        coi = -1
        mod_rects = []
        exit_game = None
        y = 50
        while True:
            y = 50
            self.DISPLAYSURF.fill((0, 0, 0))
            self.mouse_pos = pygame.mouse.get_pos()
            if not self.mods:
                self.message("没有安装模组")
                return
            if coi == -2:
                exit_game = self.write_exit
            else:
                exit_game = self.black_exit
            for i in range(4) if len(self.mods) > 4 else range(len(self.mods)):
                mod = self.mods[i]
                text = self.blit_text(mod.TITLE, (200, y)) if coi != i else self.blit_text(mod.TITLE, (200, y), 18, (0, 0, 0), (255, 255, 255))
                if text.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                    coi = i
                elif pygame.Rect(10, 60, 80, 86).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                    coi = -2
                else:
                    coi = -1
                mod_rects.append(text)
                y += 28
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
                if abs(coi) == coi:
                    if not self.mods[coi].run_on_load:
                        self.mods[coi].run_mod()
                    else:
                        self.message("本模组不支持游戏内启动，因为为加载项")
                elif coi == -2:
                    return
            self.DISPLAYSURF.blit(exit_game, (10, 60))
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            self.clock.tick(FPS)


    def start(self):
        choice = 1    
        self.duck_game()
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.blit_text(f"等级:{self.setting.read('level')}", (30, 30), 24)
            self.blit_text("逃离王建国", (580, 100), 75)
            self.mouse_pos = pygame.mouse.get_pos()
            if choice == 1:
                start_game = self.blit_text("开始游戏", (600, 300), 75,
                               (0, 0, 0), (255, 255, 255))
            else:
                start_game = self.blit_text("开始游戏", (600, 300), 75,
                               (255, 255, 255), (0, 0, 0))
            if choice == 2:
                gift = self.blit_text("礼包兑换", (650, 400), 75,
                               (0, 0, 0), (255, 255, 255))
            else:
                gift = self.blit_text("礼包兑换", (650, 400), 75,
                               (255, 255, 255), (0, 0, 0))
            if choice == 3:
                shop = self.blit_text("商城", (650, 500), 75,
                               (0, 0, 0), (255, 255, 255))
            else:
                shop = self.blit_text("商城", (650, 500), 75,
                               (255, 255, 255), (0, 0, 0))
            if choice == 4:
                player = self.blit_text("角色配置", (650, 600), 75,
                               (0, 0, 0), (255, 255, 255))
            else:
                player = self.blit_text("角色配置", (650, 600), 75,
                               (255, 255, 255), (0, 0, 0))
            if choice == 5:
                pray = self.blit_text("祈愿", (650, 700), 75,
                               (0, 0, 0), (255, 255, 255))
            else:
                pray = self.blit_text("祈愿", (650, 700), 75,(255, 255, 255), (0, 0, 0))
            
            if choice == 6:
                exit_game = self.write_exit
            else:
                exit_game = self.black_exit
            
            if choice == 7:
                mods = self.blit_text("模组", (140, 10), 20,
                               (0, 0, 0), (255, 255, 255))
            else:
                mods = self.blit_text("模组", (140, 10), 20,(255, 255, 255), (0, 0, 0))

            self.DISPLAYSURF.blit(exit_game, (10, 60))

            if start_game.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 1
            elif gift.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 2
            elif shop.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 3
            elif player.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 4
            elif pray.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 5
            elif pygame.Rect(10, 60, 80, 86).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 6
            elif mods.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 7
            else:
                choice = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.kill_precess()
            if pygame.mouse.get_pressed()[0]:
                if choice == 1:
                    self.run_game()
                elif choice == 2:
                    os.system(f"start {os.path.join(BASE_DIR, 'gift.exe')}")
                    time.sleep(0.2)
                elif choice == 3:
                    self.shop()
                elif choice == 4:
                    self.choice_player()
                elif choice == 5:
                    os.system(f"start {os.path.join(BASE_DIR, 'pray.exe')}")
                    time.sleep(0.2)
                elif choice == 6:
                    self.kill_precess()
                elif choice == 7:
                    time.sleep(0.3)
                    self.run_mods()
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            self.clock.tick(FPS)

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

    def get_player_display(self, image, game_name, name, size):
        surface = pygame.Surface((size[0] + 30, size[1] + 50))
        if self.setting.read("player") == name:
            self.blit_text("已出战", (85, size[1] + 28), color=(0, 0, 0), bg=(255, 255, 255), display=surface)
        else:
            self.blit_text("选择", (85, size[1] + 28), color=(255, 255, 255), bg=(0, 0, 0), display=surface)
        surface.blit(image, (0, 30))
        self.blit_text(game_name, (70, 0), display=surface)
        return surface

    def choice_player(self):
        fengxiaoyi_image = pygame.image.load(paths['fengxiaoyi'])
        wangjianguo_image = pygame.image.load(paths['wangjianguo'])
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            mouse_pos = pygame.mouse.get_pos()
            fengxiaoyi = self.get_player_display(fengxiaoyi_image, "风小逸", 'fengxiaoyi', (130, 140))
            wangjianguo = self.get_player_display(wangjianguo_image, "王建国", 'wangjianguo', (130, 140))
            if self.setting.read("fengxiaoyi") == true:
                self.DISPLAYSURF.blit(fengxiaoyi, (50, 50))
            if self.setting.read("wangjianguo") == true:
                self.DISPLAYSURF.blit(wangjianguo, (400, 50))
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
                elif event.type == QUIT:
                    return
                elif event.type == MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if self.setting.read("fengxiaoyi") == true:
                        if fengxiaoyi.get_rect().collidepoint(pos[0], pos[1]):
                            self.setting.add('player', "fengxiaoyi")
                    if self.setting.read("wangjianguo") == true:
                        if not wangjianguo.get_rect().collidepoint(pos[0], pos[1]):
                            self.setting.add('player', "wangjianguo")
            self.DISPLAYSURF.blit(self.lp, mouse_pos)
            pygame.display.update()

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

    def kill_precess(self, *, no_title=False):
        if not no_title:
            if not self.ask_yes_no("退出游戏？"):
                return
        pygame.quit()
        sys.exit()

def main():
    pygame.init()
    Setting("repair").add("game_path", BASE_DIR) # 更新运行目录，为了修复程序更快的找到游戏目录
    cmd_text(version_text)
    window_info = pygame.display.Info()
    DISPLAYSURF = pygame.display.set_mode(
        (window_info.current_w, window_info.current_h))
    download_files()
    window = Surf(DISPLAYSURF)
    window.start()


if __name__ == "__main__":
    main()
