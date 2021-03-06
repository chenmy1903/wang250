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
import argparse
import threading
import asyncio

from bilibili_api import video
from pygame.locals import *
from pickleshare import PickleShareDB
from game import play as play_game, paths as game_paths

from PyQt5.QtWidgets import QInputDialog, QWidget, QMessageBox, QApplication


UP = "up"
DOWN = "down"
LEFT = "left"
RIGHT = "right"

true = "True"
false = "False"

launcher_version = "0.4.2"

speed = 1000
CONFIG_PATH = "~/.duck_game/wang250"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images")
paths = {"fengxiaoyi": os.path.join(IMAGE_PATH, "fengxiaoyi_1.png"),
         "wangjianguo": os.path.join(IMAGE_PATH, 'wangjianguo.png'),
         "bgm": os.path.join(BASE_DIR, 'bgm.mp3'),
         'white_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_w.png'),
         'black_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_b.png'),
         'icon': os.path.join(BASE_DIR, "icon.ico"),
         "bili_ir_code": os.path.join(IMAGE_PATH, "bili_ir_code.jpg"),
         "logo": os.path.join(IMAGE_PATH, "duck_game.png"),
         "bgm": os.path.join(BASE_DIR, "game_bg.mp3"),
         }

paths.update(game_paths)
lock = threading.Lock()

version_text = """
游戏公告

认准游戏官网：https://chenmy1903.github.io/wang250

新版配置要求：

1. 显示器（60Hz以上）
2. 系统版本（System Version）：Windows 10以上（或Windows 7 安装VC运行库）

tip: 系统版本输入`winver`即可查看

重要通知
1. 因为游戏维护，兑换、祈愿等GUI功能暂时关闭，恢复时间另行通知
2. 旧版本请重新从官网下载安装包，进行安装
3. 因为王丑菊使用交换机修改了鸭皇官网的DNS，所以导致在南大附小访问本游戏/网站，会提示资源下载失败的情况，想玩的人可以带U盘进入机房进行游玩
TIPS:1. 破解王丑菊方法：可以修改代理DNS（未尝试过，玩家们可以尝试一下） 或 前往 https://github.com/chenmy1903/wang250/ 去手动下载资源
2022/1/18更新
1. 我们支持替换开始游戏啦

支持列表：金古探险, ...（我们正在开发中，可以去github投稿）

网址：https://github.com/chenmy1903/wang250/

> 宁同开发的模组就非常优秀（胡编乱造）

12/26更新
1. 之前的更新忘更新了
2. 补发王轶臣生日的200钻石
3. 修改了鼠标箭头的样式（要不使用多显示器会出现bug，其实也是解码的问题）
12/24更新
1. 王轶臣的生日
2. 玩法改进：3
12/20更新 (0.6.3更新)
1. 明天作者生日，上线会有剧情 + 10000钻石
2. 修复支付功能断网bug
3. 修复手滑在支付页面按退出按钮而导致钻石不到账的问题
4. 修复生日活动bug导致游戏闪退的bug （其实是db的特性导致的）
12/14更新
1. 今天幻塔开放预下载（干翻原神，幻塔永存！为了自选五星！）
2. 支付页面增加确认按钮，防止支付不到账的问题
3. 修复支付闪退的bug，让你的硬币不浪费
4. 修复支付系统刷钻石的bug
5. tip: 每人最多购买200钻石（每个视频2个币，后面会优化。作者提示：不要冲动氪金！）
12/13更新
1. bilibili投币充钱测试版
2. 修复因语法错误无法启动游戏的问题
3. 修复充值页面闪退的问题
4. 修复字体显示异常的问题
5. 修复充值失败的问题
6. 修复由异步同行引发的bug
12/12更新
1. 兑换码功能回归（需官网下载兑换码组件包）
12/11 更新
1. 暴击王丑菊开始公测（游戏内点击活动进入）
2. 修复因鼠标捕捉错误而启动失败的bug
3. 修复退出活动会执行退出游戏的bug
4. 修复暴击王丑菊进入剧情提示出现错误的bug
5. 修复进入模组闪退的bug
12/10 更新
1. 纠正金老头的名字为陈国企
12/9 更新
1. 大战王丑菊开始测试（需安装Python及库，不建议普通玩家尝试）
2. 今天作者生日（阴历），全服发放648000钻石
3. 修复王丑菊资源下载失败导致游戏启动失败的bug
11/21更新
1. 管理员模式更新（游戏目录启动cmd，执行 start.exe --admin [password] 进行调用）
2. 管理员模式可以不受外挂监测的控制
管理员密码获取方式：不知道（以后才有，但是朋友免费送）
11/20更新
1. 增加启动器自动更新功能
2. 0.5版本之前入坑游戏无法进行更新bug修复
11/19更新
因为逃离王建国安装文件精化，导致祈愿等gui功能无法启动，预计9/20更新
11/13更新
1. 模组只会加载4个bug修复
2. mod_tools.py加载错误bug修复
11/12更新
1. 模组功能更新
2. 修复对话框点击时会异常跳转的问题
3. 部分界面增加退出按钮，短按返回，长按退出游戏
4. 增加mod_tools.py文件（模组依赖），不需要每次敲入工具代码
5. 修复游戏闪退的bug
6. 修复启动游戏时无法正常加载模组的问题

模组教程：https://chenmy1903.github.io/wang250/mods
11/9更新
1. 修复游戏功能更新（需另下载）
2. 坚果云dat文件解除工具更新（需另下载）
上面所述内容均在下面的网址
下载网址：https://chenmy1903.github.io/wang250/mods/tools

11/6版本更新（上线自动领取更新补偿300钻石）
1. 可恶的王丑菊把我网站给禁了，所以在南大附小无法游玩本游戏（指网络nkdxfsxx）
2. 鸭皇X苏诗朗 ，准备制作模组王建国趋势（去世）模拟器
3. 金古之匙模组预告：使用金古之匙可以开启王建国的**（自行脑补）游戏会直接获得胜利
4. 在爱发电捐款者可以获得一个1000钻石兑换码，并有机会登上官网的感谢榜
5. 修复等级可以突破120的bug，并且修复一些情况会误判为外挂的情况
6. 在0.4版本入坑的小伙伴请重新下载游戏，因为启动器变更了，旧版本启动器无法启动新版本
7. 启动器更完善（不需要重新下载游戏）

0.6还未完成的内容
1. 金古之匙模组
2. 王八哥『吴汉林』角色祈愿活动
3. 王建国趋势（去世）模拟器

0.7预告（2022/2/1更新）
1. 『万恶之源』王丑菊更新 （大概率白嫖）
2. 春节礼包
3. 剧情更新
4. 因为技术原因，本条无法完成
5. 王建国死全家活动 

tip: 所有更新内容以实际更新为准。
"""



def cmd_text(text: str, end_function=None):
    text_r = text.replace('\n', '-')
    run_path = os.path.join(sys.exec_prefix, "python.exe")
    os.system(f"start {run_path} -c \"text = '''{text_r}'''; print(text.replace('-', '\\n')); input('Enter关闭本窗口')\"")
    if end_function:
        end_function()



def download_files():
    if not os.path.isdir(os.path.join(BASE_DIR, 'ext')): # 检测模组文件夹
        os.mkdir(os.path.join(BASE_DIR, 'ext'))
    for key, value in paths.items():
        if not os.path.isfile(value):
            try:
                file_name = value.replace('\\', '/').split('/')[-1]
                r = requests.get(f"https://chenmy1903.github.io/wang250/play/files/{file_name}")
                if file_name.endswith('.png') or file_name.endswith('.jpg'):
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
        self.white_exit = pygame.image.load(paths['white_exit_button'])
        self.black_exit = pygame.image.load(paths['black_exit_button'])
        self.win_info = pygame.display.Info()
        self.win_height = self.win_info.current_h
        self.win_widht = self.win_info.current_w
    
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

    def next(self, text: str, color: tuple = (255, 255, 255), bg: tuple = (0, 0, 0)):
        self.DISPLAYSURF.fill(bg)
        self.blit_text(text, (600, 800), color=color)
        pygame.display.update()
        pygame.time.wait(1000)
        self.click_to_continue(bg)

    def click_to_continue(self, bg: tuple = (0, 0, 0)):
        self.blit_text("按键盘上的任何键继续", (600, self.win_height - 20))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.DISPLAYSURF.fill(bg)
                    return
                elif event.type == KEYUP:
                    self.DISPLAYSURF.fill(bg)
                    return
            pygame.display.update()

async def get_coin():

    v = video.Video(bvid="BV18L41177JR")
    info = await v.get_info()
    return info["stat"]["coin"]

class KeJin(Text):

    def __init__(self, surface):
        self.surface = surface
        self.init_val()
        self.set_surface(surface)
        self.config = Setting()
        self.ir_code = pygame.image.load(paths['bili_ir_code'])
        self.coins =  asyncio.get_event_loop().run_until_complete(get_coin())

    def start(self):
        choice = 0
        if os.system("ping www.bilibili.com"):
            self.message("氪金平台数据获取失败")
            return
        while True:
            self.mouse_pos = pygame.mouse.get_pos()
            self.surface.fill((0, 0, 0))
            self.blit_text("扫描下面二维码给作者的第一个视频投币，投币完成后按回车键确认，ESC退出页面（100钻石/币）", (20, 20), 30)
            if choice == 1:
                chack_coin = self.blit_text("检测投币状态（概率闪退，请不要连续操作，否则奖励不会到账）", (100, 580), 20, (0, 0, 0), (255, 255, 255))
            else:
                chack_coin = self.blit_text("检测投币状态（概率闪退，请不要连续操作，否则奖励不会到账）", (100, 580), 20, (255, 255, 255), (0, 0, 0))

            if chack_coin.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 1
            else:
                choice = 0

            if pygame.mouse.get_pressed()[0]:
                if choice == 1:
                    self.add()
            self.surface.blit(self.ir_code, (20, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    if self.exit_ask():
                        return
                if event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        if self.exit_ask():
                            self.add()
                            return
                    elif event.key == K_RETURN:
                        self.add()
            self.surface.blit(self.lp, self.mouse_pos)
            pygame.display.update()

    def add(self, no_message=False):
        while True:
            try:
                add_coin = asyncio.get_event_loop().run_until_complete(get_coin()) - self.coins
                self.coins =  asyncio.get_event_loop().run_until_complete(get_coin())
            except:
                pass
            else:
                break
        if add_coin:
            self.config.add("diamond", self.config.read("diamond") + add_coin * 100)
            self.message(f"投币成功，获得{add_coin * 100}钻石")
        else:
            if not no_message:
                self.message("你还没有投币，白嫖是不可能的")
            


    def exit_ask(self, *, no_title=False):
        if not no_title:
            if not self.ask_yes_no("确认退出充钱系统？退出后支付会出现钻石不到账的问题"):
                return False
            return True
        return True

    def message(self, text: str):
            win_info = self.win_info
            cio = 0
            while True:
                mouse_pos = pygame.mouse.get_pos()
                self.surface.fill((0, 0, 0))
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
                    pygame.time.wait(500)
                    return True
                self.DISPLAYSURF.blit(self.lp, mouse_pos)
                pygame.display.update()

    def ask_yes_no(self, text: str):
        win_info = pygame.display.Info()
        cio = 0
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self.surface.fill((0, 0, 0))
            self.blit_text(text, (win_info.current_w / 4, win_info.current_h / 2), 40)
            if cio != 1:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (255, 255, 255), (0, 0, 0))
            elif cio == 1:
                yes = self.blit_text("确认", (win_info.current_w / 4 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (0, 0, 0), (255, 255, 255))
            if cio != 2:
                no = self.blit_text("取消", (win_info.current_w / 6 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (255, 255, 255), (0, 0, 0))
            elif cio == 2:
                no = self.blit_text("取消", (win_info.current_w / 6 + len(text) // 2 * 72, win_info.current_h / 2 + 100), 40, (0, 0, 0), (255, 255, 255))
            pygame.draw.rect(self.surface, (255, 255, 255),
                        (win_info.current_w / 4 - 30, win_info.current_h / 2 - 20, len(text) * 40 + 30, 200), 5)
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
            self.surface.blit(self.lp, mouse_pos)
            pygame.display.update()


def load_mod():
    mod_path = os.path.join(BASE_DIR, "ext")
    package_list = []
    mods = os.listdir(mod_path)
    for package in mods:
        if not package.endswith('.py'):
            continue
        load = importlib.import_module(f"ext.{package.replace('.py','')}")
        try:
            if load.run_on_load:
                load.run_mod()
        except:
            pass
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
        new[key] = value
        self.db[self.file_name] = new

    def read(self, config=None):
        """读文件"""
        if config:
            return self.db[self.file_name][config]
        return self.db[self.file_name]

if "fps" not in Setting().read():
    Setting().add("fps", 60)

FPS = Setting().read("fps")

def update_runner():
    config = Setting("repair")
    read = config.read()
    temp = os.environ["TEMP"]
    if "runner_version" not in read:
        # 11/20更新：0.5版本之前入坑游戏无法进行更新bug修复
        cmd_text("请重新从官网下载游戏，检测到启动器版本为0.1旧版，请更新")
        webbrowser.open("https://chenmy1903.github.io/wang250/play/setup.exe")
        sys.exit()
    if "runner_version" in read and read["runner_version"] != launcher_version:
        cmd_text("检测到启动器版本更新，准备启动自动更新")
        try:
            setup_file = requests.get("https://chenmy1903.github.io/wang250/play/update.exe").content
            with open(os.path.join(temp, "wang_setup.exe"), "wb") as f:
                f.write(setup_file)
            os.system(f"start {os.path.join(temp, 'wang_setup.exe')}")
            sys.exit()
        except:
            cmd_text("下载失败，尝试进入游戏")
    if os.path.isfile(os.path.join(temp, "wang_setup.exe")):
        os.remove(os.path.join(temp, "wang_setup.exe"))



class Shop(Text):
    def __init__(self, surface):
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

def join(command_list: list):
    out_str = ""
    for command in command_list:
        out_str += command
        out_str += " "
    return out_str


class JianguoBarbecue:
    def __init__(self):
        self.surface = pygame.Surface()

class GameRect(pygame.Rect):
    title = ""
    pos = ()
    size = 0

class GiftWindow():
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        


class Surf(Text):
    def __init__(self, surface):
        super().__init__()
        self.DISPLAYSURF = surface
        pygame.mouse.set_visible(False)
        sys.path.append(os.path.join(BASE_DIR, "ext"))
        sys.path.append(BASE_DIR)
        try:
            if os.system(f"{os.path.join(sys.exec_prefix, 'pythonw.exe')} -m pip install wang250-mods --upgrade"):
                raise Exception()
        except:
            if not os.path.isdir(os.path.join(BASE_DIR, "game_runner", "Lib", "site-packages", "mods")): # 脱机模式检测依赖
                self.message("资源下载失败")
                if not self.ask_yes_no("是否尝试继续进入游戏"):
                    self.kill_precess(no_title=True)
                self.mods = []
        else:
            try:
                self.mods = load_mod() # 加载模组
            except:
                self.message("模组加载失败")
                self.mods = [] # 设置为空，游戏内显示未加载模组
        try:
            time_file = requests.get("https://chenmy1903.github.io/wang250/play/time_activaly.py").text
            with open(os.path.join(BASE_DIR, "time_activaly.py"), "w", encoding="UTF-8") as f:
                f.write(time_file)
        except:
            self.message("活动资源下载失败，进入游戏后活动功能会丢失")
        try:
            self.time_py = importlib.import_module("time_activaly")
            paths.update(self.time_py.paths)
            self.time_display = self.time_py.BaseDisplay
        except:
            self.time_display = None
        self.mouse_pos = (0, 0)
        self.shop_gui = Shop(self.DISPLAYSURF)
        pygame.mixer.music.load(paths["bgm"])
        self.clock = pygame.time.Clock()
        self.setting = Setting()
        self.admin_mode = Setting('repair').read("admin_mode") == true
        if not "coins" in self.setting.read():
            self.setting.add("coins", 300) # 开服礼包 (10/1更新)
        if not "diamond" in self.setting.read():
            self.setting.add("diamond", 1000) # 开服礼包 (10/1更新)
        if not "level" in self.setting.read():
            self.setting.add("level", 1) # 初始化"level"防止调用时出KeyError (10/24更新)
        self.add_settings()
        self.get_gift() # 10/29更新：礼包领取
        pygame.display.set_icon(pygame.image.load(paths['icon']))

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
        if self.admin_mode:
            return
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

    def download_logo(self):
        value = paths["logo"]
        if not os.path.isfile(value):
            try:
                file_name = value.replace('\\', '/').split('/')[-1]
                r = requests.get(f"https://chenmy1903.github.io/wang250/play/files/{file_name}")
                if file_name.endswith('.png') or file_name.endswith('.jpg'):
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

    def download_files(self):
        for key, value in paths.items():
            file_name = value.replace('\\', '/').split('/')[-1]
            print("Download {}".format(file_name))
            if not os.path.isfile(value):
                try:
                    r = requests.get(f"https://chenmy1903.github.io/wang250/play/files/{file_name}")
                    if file_name.endswith('.png') or file_name.endswith('.jpg'):
                        download_path = os.path.join(IMAGE_PATH, file_name)
                    else:
                        download_path = os.path.join(BASE_DIR, file_name)
                        lock.acquire()
                        self.no_img += 1
                        lock.release()
                    if not os.path.isdir(IMAGE_PATH):
                        os.mkdir(IMAGE_PATH)
                    with open(download_path, 'wb') as f:
                        f.write(r.content)
                        
                except:
                    cmd_text("下载资源失败，强制退出游戏中...")
                    raise SystemExit()
                else:
                    lock.acquire()
                    self.download_file_count += 1
                    lock.release()
            else:
                if not file_name.endswith('.png') or file_name.endswith('.jpg'):
                    lock.acquire()
                    self.no_img += 1
                    lock.release()

    def duck_game(self):
        self.download_logo()
        window_info = pygame.display.Info()
        pygame.mouse.set_visible(True)
        self.download_file_count = 0
        self.no_img = 0
        self.DISPLAYSURF.fill((0, 0, 0))
        logo = pygame.image.load(paths["logo"])
        pygame.display.set_caption("逃离王建国")
        p = threading.Thread(target=self.download_files)
        p.start()
        for i in range(255):
            self.DISPLAYSURF.fill((0, 0, 0))
            self.blit_text("鸭皇游戏 | 逃离王建国", (window_info.current_w / 2 - 72 * 5, window_info.current_h / 2 - 100), 72, pygame.Color(255, 255, 255))
            self.DISPLAYSURF.blit(logo, (window_info.current_w / 4 - 72 * 5, window_info.current_h / 2 - 100))
            self.blit_text("准备启动", (window_info.current_w / 2 - 72 * 5, window_info.current_h - 100), 72, pygame.Color(255, 255, 255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.kill_precess(no_title=True)
            pygame.display.update()
            self.clock.tick(60)

        if not os.path.isdir(os.path.join(BASE_DIR, 'ext')): # 检测模组文件夹
            os.mkdir(os.path.join(BASE_DIR, 'ext'))
        load_dir_list = os.listdir(IMAGE_PATH)
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            process = (len(os.listdir(IMAGE_PATH)) + self.no_img) / len(paths) # 下载进度计算
            self.blit_text("鸭皇游戏 | 逃离王建国", (window_info.current_w / 2 - 72 * 5, window_info.current_h / 2 - 100), 72, pygame.Color(255, 255, 255))
            self.DISPLAYSURF.blit(logo, (window_info.current_w / 4 - 72 * 5, window_info.current_h / 2 - 100))
            self.blit_text(f"下载资源 进度：{round(round(process, 3) * 100, 1)}%", (window_info.current_w / 2 - 72 * 5, window_info.current_h - 100), 72, pygame.Color(255, 255, 255))
            if process == 1 or not p.is_alive():
                break
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.kill_precess(no_title=True)
            pygame.display.update()
            self.clock.tick(FPS)
        pygame.mouse.set_visible(False)
        p.join()
        self.init_val()

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
                exit_game = self.white_exit
            else:
                exit_game = self.black_exit
            for i in range(len(self.mods)):
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
                    try:
                        if not self.mods[coi].run_on_load:
                            self.DISPLAYSURF.fill((0, 0, 0))
                            pygame.mouse.set_visible(True)
                            self.mods[coi].run_mod(surface=self.DISPLAYSURF)
                        else:
                            self.message("本模组不支持游戏内启动，因为为加载项")
                    except:
                        self.message("模组出现问题，请尝试卸载该模组")
                    finally:
                        pygame.mouse.set_visible(False)
                        break
                elif coi == -2:
                    return
            self.DISPLAYSURF.blit(exit_game, (10, 60))
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            self.clock.tick(FPS)

    def give(self, key, value):
        if isinstance(value, int) or isinstance(value, float):
            self.setting.add(key, self.setting.read(key) + value)
        else:
            self.setting.add(key, value)

    def run_special_activities(self):
        special_version = '0.3'
        rd_special_version = self.setting.read("special_version") if "special_version" in self.setting.read() else None
        if rd_special_version == special_version:
            return # 已经参加完了
        def download():
            r = requests.get("https://chenmy1903.github.io/wang250/play/files/spring_festival2022.png")
            file_bytes = r.content
            with open(os.path.join(IMAGE_PATH, "spring_festival2022.png"), "wb") as f:
                f.write(file_bytes)
        download()
        self.next("大家好，我是鸭皇", (0, 0, 0), (100, 0, 0))
        self.DISPLAYSURF.blit(pygame.image.load(os.path.join(IMAGE_PATH, "spring_festival2022.png")), (50, 50))
        self.next("金古三雄在这里给您拜年啦~", (0, 0, 0), (100, 0, 0))
        self.give("diamond", 10000)
        self.next("我们在此献上10000钻石", (0, 0, 0), (100, 0, 0))
        self.next("祝您在游戏里玩的愉快", (0, 0, 0), (100, 0, 0))
        self.setting.add("special_version", special_version)

    def start_bgm(self):
        pygame.mixer.music.load(paths["bgm"])
        pygame.mixer.music.play(-1)



    def start(self):
        choice = 1    
        self.duck_game()
        self.start_bgm()
        self.run_special_activities()
        window_info = pygame.display.Info()
        while True:
            pygame.display.set_caption("鸭皇游戏·逃离王建国")
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
                exit_game = self.white_exit
            else:
                exit_game = self.black_exit
            
            if choice == 7:
                mods = self.blit_text("模组", (140, 10), 20,
                               (0, 0, 0), (255, 255, 255))
            else:
                mods = self.blit_text("模组", (140, 10), 20,(255, 255, 255), (0, 0, 0))
            
            if choice == 9:
                time_play = self.blit_text("活动", (250, 10), 20,
                               (0, 0, 0), (255, 255, 255))
            else:
                time_play = self.blit_text("活动", (250, 10), 20,(255, 255, 255), (0, 0, 0))
            
            if choice == 8 and not self.admin_mode:
                admin = self.blit_text("登录管理员", (0, 5), 20,
                               (0, 0, 0), (255, 255, 255))
            if choice == 10:
                bilicoin = self.blit_text("充值", (300, 20), 20,
                               (0, 0, 0), (255, 255, 255))
            else:
                bilicoin = self.blit_text("充值", (300, 20), 20, (255, 255, 255), 
                               (0, 0, 0))
            if not self.admin_mode:
                admin = self.blit_text("登录管理员", (0, 5), 20,(255, 255, 255), (0, 0, 0))
            else:
                admin = None

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
            elif admin and admin.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 8
            elif time_play.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 9
            elif bilicoin.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 10
            else:
                choice = 0
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.kill_precess()
            if pygame.mouse.get_pressed()[0]:
                if choice == 1:
                    pygame.mixer.music.stop()
                    self.run_game()
                elif choice == 2:
                    if os.path.isfile(os.path.join(BASE_DIR, 'gift.exe')):
                        os.system(f"start {os.path.join(BASE_DIR, 'gift.exe')}")
                    else:
                        self.message("未检测到文件，请前往官网下载组件包进行安装")
                    pygame.time.wait(200)
                elif choice == 3:
                    self.shop()
                elif choice == 4:
                    self.choice_player()
                    # self.message("维护中")
                elif choice == 5:
                    self.message("功能维护中")
                elif choice == 6:
                    self.kill_precess()
                elif choice == 7:
                    pygame.time.wait(200)
                    self.run_mods()
                elif choice == 8:
                    pygame.time.wait(200)
                    self.lognin_admin()
                elif choice == 9:
                    if self.time_display:
                        try:
                            self.time_display(self.DISPLAYSURF).start()
                        except:
                            pygame.mouse.set_visible(False)
                            self.message("代码执行中出现了错误")
                    else:
                        self.message("启动失败，文件丢失")
                elif choice == 10:
                    KeJin(self.DISPLAYSURF).start()
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            self.clock.tick(FPS)

    def get_gift(self):
        GiftWindow(self.DISPLAYSURF)

    def lognin_admin(self):
        pygame.quit()
        app = QApplication(sys.argv)
        text, ok = QInputDialog.getText(None, "管理员登录", "请输入管理员密码")
        if not ok:
            return
        try:
            web_password = requests.get("https://chenmy1903.github.io/wang250/admin").text
        except:
            QMessageBox.critical(None, "错误", "无网络连接")
        if text == web_password:
            QMessageBox.information(None, "提示", "认证成功，点击确定以重启游戏")
            Setting("repair").add("admin_mode", true)
        else:
            QMessageBox.information(None, "提示", "密码错误，点击确定启动游戏")
        os.system("start " + sys.executable + " " + __file__)
        sys.exit()

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

def cmd_argument():
    config = Setting("repair")
    parser = argparse.ArgumentParser(__file__.replace('\\', '/').split("/")[-1])
    parser.add_argument("--no_start_text", help="游戏启动时不显示公告", action='store_true')
    if config.read("admin_mode") == true:
        parser.add_argument("--no_update", help="游戏启动时不检测更新", action='store_true')
    return parser.parse_args()

def main():
    pygame.init()
    Setting("repair").add("game_path", BASE_DIR) # 更新运行目录，为了修复程序更快的找到游戏目录
    argv = cmd_argument()
    config = Setting("repair")
    if not argv.no_start_text:
        cmd_text(version_text)
    if config.read("admin_mode") == true and not argv.no_update:
        update_runner() # 更新启动器
    window_info = pygame.display.Info()
    DISPLAYSURF = pygame.display.set_mode(
        (window_info.current_w, window_info.current_h))
    window = Surf(DISPLAYSURF)
    window.start()


if __name__ == "__main__":
    main()
