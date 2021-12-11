# 12/7 - 12/21 活动：大战王丑菊
# 前言：
# 王丑菊使用雷电之力封锁了你的电脑，我们需要击败他，来获得电脑
# 根据真实事件改编！
# 王丑菊封锁鸭皇官网事件，勿忘耻辱！
# 玩法：
# 1.开始的时候王丑菊会控制你的电脑，你需要打开桌面上的伽卡他卡破解器，破解控制
# 2. 但是王丑菊会禁掉鸭皇官网，你需要找到服务器进行关闭（密码：QWEr!2#4）
# 3. 然后王丑菊会联合王八哥，尝试击败你
# 4. 加油，程序猿，打败王丑菊获得胜利吧！
# 活动结束后本文件可以当成模组进行游玩

import pygame
import os
import sys

import requests
import random

from pygame.locals import *
from pickleshare import PickleShareDB

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "images")

true = 'True'
false = 'false'

paths = {
    'white_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_w.png'),
    'black_exit_button': os.path.join(IMAGE_PATH, 'exitbutton_b.png'),
    'lp': os.path.join(IMAGE_PATH, 'lp.png'),
    "download_git": os.path.join(IMAGE_PATH, "download_git.png"),
    "command_board_gui": os.path.join(IMAGE_PATH, "command_board_gui.png"),
    "command_board": os.path.join(IMAGE_PATH, "command_board.png"),
    "program": os.path.join(IMAGE_PATH, "program.png"),
    "uninstall_git": os.path.join(IMAGE_PATH, "uninstall_git.png"),
    "uninstall_button": os.path.join(IMAGE_PATH, "uninstall_button.png"),
    "wangchouju": os.path.join(IMAGE_PATH, "wangchouju.jpg"),
    "jiakataka_quiter": os.path.join(IMAGE_PATH, "jiakataka_quiter.png"),
    }

clock = pygame.time.Clock()

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

class GameRect(pygame.Rect):
    title = ""
    pos = ()
    size = 0

class Setting:
    def __init__(self, file_name, config={}, config_path="~/.duck_game/wang250/time"):
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
    def init_val(self):
        self.lp = pygame.image.load(paths['lp'])
        self.white_exit = pygame.image.load(paths['white_exit_button'])
        self.black_exit = pygame.image.load(paths['black_exit_button'])
    
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


class BaseDisplay(Text):

    title = "大战王丑菊"
    fps = 60
    config_name = "vs_wangchouju"

    def __init__(self, display=None):
        pygame.mouse.set_visible(False)
        self.config = Setting(self.config_name)
        self.base_config = Setting("config", config_path="~/.duck_game/wang250/")
        self.win_info = pygame.display.Info()
        self.init_val()
        self.win_width = self.win_info.current_w
        self.win_height = self.win_info.current_h
        self.DISPLAYSURF = pygame.display.set_mode((self.win_width, self.win_height)) if not display else display
        self.set_surface(self.DISPLAYSURF)
        pygame.display.set_caption(self.title)


    def start(self):
        self.duck_game()
        choice = 0
        if "jingu_coin" not in self.config.read():
            self.config.add('jingu_coin', 1)
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
            if choice == -1:
                exit_game = self.white_exit
            else:
                exit_game = self.black_exit
            if "play_help" not in self.config.read() or self.config.read('play_help') == false:
                if choice == 1:
                    start_game = self.blit_text("玩法游玩教程", (800, 300), 72, (0, 0, 0), (255, 255, 255))
                else:
                    start_game = self.blit_text("玩法游玩教程", (800, 300), 72, (255, 255, 255), (0, 0, 0))
            else:
                if choice == 1:
                    start_game = self.blit_text("启动玩法", (800, 300), 72, (0, 0, 0), (255, 255, 255))
                else:
                    start_game = self.blit_text("启动玩法", (800, 300), 72, (255, 255, 255), (0, 0, 0))

            if choice == 2:
                cards = self.blit_text("买卡", (800, 600), 72, (0, 0, 0), (255, 255, 255))
            else:
                cards = self.blit_text("买卡", (800, 600), 72, (255, 255, 255), (0, 0, 0))
            if start_game.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 1
            elif pygame.Rect(10, 60, 80, 86).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = -1
            elif cards.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 2
            else:
                choice = 0
            if pygame.mouse.get_pressed()[0]:
                if choice == -1:
                    pygame.time.wait(500)
                    return
                elif choice == 1:
                    self.play()
                elif choice == 2:
                    self.getting_cards()
            self.DISPLAYSURF.blit(exit_game, (10, 60))
            self.DISPLAYSURF.blit(exit_game, (10, 60))
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            clock.tick(self.fps)

    def play(self):
        no_play = "play_help" not in self.config.read() or self.config.read('play_help') == false
        if no_play:
            self.help_play()
            return

    def help_play(self):
        part1 = "part1" in self.config.read() and self.config.read('part1') == true
        part2 = "part2" in self.config.read() and self.config.read('part2') == true
        part3 = "part3" in self.config.read() and self.config.read('part3') == true
        while True:
            self.DISPLAYSURF.fill((0, 0 ,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    if self.ask_yes_no("确认退出教程？"):
                        return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        if self.ask_yes_no("确认退出教程？"):
                            return
            if not part1:
                self.next("系统：欢迎来到沙雕小学")
                self.next("（过了两节课，终于到电脑课了）")
                self.next("王丑菊：我们开始讲课... ...")
                self.next("（不知过了多久，讲完了，开始操作）")
                self.next("（你是个非常厉害的程序猿，快速地做完了老师交给你的任务）")
                self.next("（然后你下载了Git）")
                self.next("（提示：在接下来的页面上点击Download Git）")
                self.download_git()
                self.next("浏览器：下载中10%")
                self.next("浏览器：下载中40%")
                self.next("浏览器：下载中70%")
                self.next("浏览器：下载中80%")
                self.next("浏览器：下载中99%")
                self.next("浏览器：下载中100%")
                self.next("浏览器：下载完成，执行安装")
                self.next("（快速地进行了安装）")
                self.next("你熟练的使用Win + r打开了运行")
                self.next("cmd")
                self.next("git clone https://github.com/chenmy1903/chenmy1903.github.io/")
                self.next("tip:这段无需看懂，感兴趣的玩家可以网上查一下")
                self.next("git init .")
                self.next("git gui")
                self.next("...")
                self.next("王丑菊：你活干完了吗？还有本事van电脑")
                self.next("鸭皇：...（被王丑菊的气势吓住了）")
                self.next("鸭皇：我...我现在就删")
                self.next("操作提示：打开控制面板-程序与功能-git-删除")
                self.delete_git()
                self.next("王丑菊：就你会删是吧")
                self.next("下课铃：~~（下课铃的声音）")
                self.next("鸭皇：（王丑菊真的太可恶了）")
                self.next("鸭皇：（等哪天他肯定会被我们xxs打败的）")
                self.base_config.add('diamond', self.base_config.read("diamond") + 60)
                self.config.add("part1", true)
                self.next("获得了钻石60")
                self.next("~未完待续~")
            if not part2:
                self.next("wait a period of time (过了一段时间)")
                self.next("我们的电脑课又开始了")
                self.next("王丑菊：我们今天开始上课！")
                self.next("王丑菊：我们今天来填调查问卷")
                self.next("金谷：（叫小伙伴过来看奥特曼）")
                self.next("王丑菊：你们怎么上课看奥特曼啊（没有鸭皇）")
                self.next("王丑菊：将所有的男生的电脑黑掉")
                self.next("鸭皇：这**老师，艹！")
                self.next("提示：使用伽卡他卡破解器破解控制")
                self.next("tip: 本软件真实存在，感兴趣的玩家可以去 https://chenmy1903.github.io/student/ 看看")
                self.quit_jiakataka()
                self.next("破解器：寻找伽卡他卡")
                self.next("破解器：成功。")
                self.next("输入了调查问卷的网址")
                self.next("...")
                self.next("鸭皇：填完了")
                self.next("过了好几分钟，半节课都要过去了")
                self.next("王丑菊：现在我们解封男生的电脑")
                self.next("五分钟后，下课铃又响了...")
                self.base_config.add('diamond', self.base_config.read("diamond") + 60)
                self.config.add("part2", true)
                self.next("完成剧情，获得60钻石")
                self.next("~未完待续~")
            if not part3:
                self.next("王丑菊：鸭皇、君宝、秋天、金谷、丁明，你们都别用电脑了。（无真实人名，根据现实改编）")
                self.next("鸭皇：我又怎么了，怎么就不让我用电脑了啊")
                self.next("丁明：你别理他，他就是个伞*")
                self.next("鸭皇：就是个垃圾i3用什么用")
                self.next("二十分钟过去了，下课了")
                self.next("君宝：我们要建立")
                self.next("君宝：王丑菊（小声地说）")
                self.next("君宝：反动派！")
                self.next("我们全部加入了反动派")
                self.next("因为我们要一起对抗王丑菊，所以我们不用逃离王建国了（王建国就是金谷）")
                self.next("tip: 切勿模仿游戏内的行为，游戏内的剧情经过夸张化")
                self.next("你还没有金古奥特曼的卡片，接下来我们去小卖部买包卡")
                self.next("tip: 完整游戏内容需要网络连接体验，南大附小无权参与该活动")
                self.next("在南大附小进行游玩时会提示无网络连接")
                self.next("这是正常现象（可恶的王丑菊）")
                self.next("操作提示：点击十元包按钮，接下来我会给你10钻石")
                self.base_config.add("diamond", self.base_config.read("diamond") + 11)
                self.getting_cards(["wangjianguo", "chenwenli", "wangyichen"])
                self.next(f"点击右下角的卡包就可以查看拥有的卡")
                self.next("基本玩法你都知道了，接下来开始游戏吧，加油，去打败王丑菊，这些是给你买卡的资金（600钻石）")
                self.config.add("part3", true)
                self.base_config.add("diamond", self.base_config.read("diamond") + 600)
                self.next("剧情完成，获得 600 钻石")
                self.next("~未完待续~")
            self.config.add("play_help", true)
            return
            pygame.display.update()
            clock.tick(self.fps)

    def quit_jiakataka(self):
        pygame.mouse.set_visible(True)
        jiakataka_quiter = pygame.image.load(paths["jiakataka_quiter"])

        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.DISPLAYSURF.blit(jiakataka_quiter, (10, 10))
            if pygame.mouse.get_pressed()[0]:
                if pygame.Rect(10, 10, 135, 162).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                    pygame.mouse.set_visible(False)
                    self.DISPLAYSURF.fill((0, 0, 0))
                    return
            pygame.display.update()
            clock.tick(self.fps)

    def getting_cards(self, random_list=None):
        download_url = "https://chenmy1903.github.io/wang250//play/temp/chouju_card.html"
        try:
            cards = eval(requests.get(download_url).text)
            cards_list = random_list if random_list else [i for i in cards.keys()]
        except:
            self.message("检测到无网络连接，即将退出")
            pygame.quit()
            sys.exit()
        choice = 0
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.mouse_pos = pygame.mouse.get_pos()
            self.blit_text("获取金谷奥特曼", (20, 40), 40)
            self.blit_text(f"钻石：{self.base_config.read('diamond')}", (10, 10))
            self.blit_text(f"金古币：{self.config.read('jingu_coin')}", (200, 10))
            if choice == 1:
                one = self.blit_text("十元包（10钻石）", (50, 120), 20, (0, 0, 0), (255, 255, 255))
            else:
                one = self.blit_text("十元包（10钻石）", (50, 120), 20, (255, 255, 255), (0, 0, 0))
            if choice == 2:
                two = self.blit_text("二十元包（20钻石）", (250, 120), 20, (0, 0, 0), (255, 255, 255))
            else:
                two = self.blit_text("二十元包（20钻石）", (250, 120), 20, (255, 255, 255), (0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        return
            
            if one.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 1
            elif two.collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                choice = 2
            else:
                choice = 0

            if pygame.mouse.get_pressed()[0]:
                if choice == 1:
                    if self.base_config.read("diamond") > 11:
                        self.base_config.add("diamond", self.base_config.read("diamond") - 10)
                        for i in range(8):
                            card = random.choice(cards_list)
                            rd = random.randint(3, 10)
                            if card in self.config.read():
                                self.next(f"{cards[card]}重复，转换为{rd}金谷兑换币")
                                self.config.add("jingu_coin", self.config.read("jingu_coin") + rd if "jingu_coin" in self.config.read() else 5)
                                continue
                            self.config.add(card, true)
                            self.next(f"获得：{cards[card]}")
                    else:
                        self.message("钻石不足")
                elif choice == 2:
                    if self.base_config.read("diamond") > 21:
                        self.base_config.add("diamond", self.base_config.read("diamond") - 20)
                        for i in range(20):
                            card = random.choice(cards_list)
                            rd = random.randint(3, 10)
                            if card in self.config.read():
                                self.next(f"{cards[card]}重复，转换为{rd}金谷兑换币")
                                self.config.add("jingu_coin", self.config.read("jingu_coin") + rd if "jingu_coin" in self.config.read() else 5)
                                continue
                            self.config.add(card, true)
                            self.next(f"获得：{cards[card]}")
                    else:
                        self.message("钻石不足")
            
            self.DISPLAYSURF.blit(self.lp, self.mouse_pos)
            pygame.display.update()
            clock.tick(self.fps)

    def delete_git(self):
        pygame.mouse.set_visible(True)
        command_board = pygame.image.load(paths["command_board"])
        command_board_gui = pygame.image.load(paths["command_board_gui"])
        program = pygame.image.load(paths["program"])
        uninstall_button = pygame.image.load(paths["uninstall_button"])
        uninstall_git = pygame.image.load(paths["uninstall_git"])

        part1 = False
        part2 = False
        while True:
            self.DISPLAYSURF.fill((0, 0, 0))
            self.mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if not part1:
                self.DISPLAYSURF.blit(command_board, (10, 20))
                if pygame.mouse.get_pressed()[0]:
                    if pygame.Rect(10, 20, 67, 75).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                        part1 = True
            else:
                self.DISPLAYSURF.blit(command_board_gui, (0, 0))
                pygame.time.wait(2000)
                self.DISPLAYSURF.fill((0, 0, 0))
                pygame.mouse.set_visible(False)
                return
            pygame.display.update()
            clock.tick(self.fps)
            

        

    def download_git(self):
        pygame.mouse.set_visible(True)
        git_download = pygame.image.load(paths["download_git"])
        while True:
            self.mouse_pos = pygame.mouse.get_pos()
            self.DISPLAYSURF.fill((0, 0, 0))
            self.DISPLAYSURF.blit(git_download, (self.win_width / 2, self.win_height / 2))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed()[0]:
                if pygame.Rect(self.win_width / 2, self.win_height / 2, 368, 211).collidepoint(self.mouse_pos[0], self.mouse_pos[1]):
                    pygame.mouse.set_visible(False)
                    self.DISPLAYSURF.fill((0, 0, 0))
                    return
            pygame.display.update()
            clock.tick(self.fps)
            

    def next(self, text: str):
        self.blit_text(text, (600, 800))
        pygame.display.update()
        pygame.time.wait(1000)
        self.click_to_continue()

    def click_to_continue(self):
        self.blit_text("按键盘上的任何键继续", (600, self.win_height - 20))
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.DISPLAYSURF.fill((0, 0, 0))
                    return
                elif event.type == KEYUP:
                    self.DISPLAYSURF.fill((0, 0, 0))
                    return
            pygame.display.update()
            

    def duck_game(self):
        pass

    def message(self, text: str):
            win_info = self.win_info
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
                    pygame.time.wait(500)
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
    # 测试
    pygame.init()
    download_files()
    display = BaseDisplay()
    display.start()

if __name__ == "__main__":
    run_mod()
