import os
import zipfile
import sys
import win32com.client as client
from pickleshare import PickleShareDB
import requests
import argparse
import code

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
GAME_DIR = BASE_DIR
shell = client.Dispatch("WScript.Shell")

__version__ = "0.4.2"


pip = os.path.join(GAME_DIR, "game_runner", "Scripts", 'pip.exe')
start_game = os.path.join(GAME_DIR, "start.exe")
start_api = os.path.join(GAME_DIR, "game_runner", "Scripts", 'activate.bat')
python = os.path.join(GAME_DIR, "game_runner", "python.exe")
pythonw = os.path.join(GAME_DIR, "game_runner", "pythonw.exe")

class Setting:
    def __init__(self, file_name, config={}, config_path="~/.duck_game/wang250/"):
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


def createShortCut(filename, lnkname):
    shortcut = shell.CreateShortCut(lnkname)
    shortcut.TargetPath = filename
    shortcut.WorkingDirectory = os.path.dirname(filename)
    shortcut.save()

try:
    rely_list = eval(requests.get("https://chenmy1903.github.io/wang250/relys").text)
except:
    rely_list = []
    print("依赖列表获取失败")

def assert_game():
    auto = -1
    if not os.path.isfile(os.path.join(GAME_DIR, 'game_runner.zip')):
        print("修复文件不存在，请检查本工具是否移动到游戏目录")
        print(f"现在处于的目录是：\"{BASE_DIR}\"")
        print(f"检测到的游戏目录是：\"{GAME_DIR}\"")
        print("如果目录不同，在底部输入path即可进行修复")
        print("如果处于游戏安装目录，建议重新下载游戏进行修复")
        print("如若未运行过游戏，请运行游戏进行配置基础目录，以后修复不需要在游戏目录运行")
        print("游戏无法启动，就必须把本文件放在游戏目录")
        print("下载链接：https://chenmy1903.github.io/wang250")
        if input("Enter键退出修复工具/输入path进行修复游戏目录问题：").replace(' ', '').lower() == "path":
            Setting("repair").add("game_path", BASE_DIR)
            print("修复完成")
            input("Enter重启启动器并启动游戏")
            os.system(f"start {__file__}")
        sys.exit()
    if not os.path.isfile(os.path.join(GAME_DIR, 'start.exe')):
        print("游戏文件丢失")
        print("丢失的文件为游戏主程序(start.exe)")
        print("请从官网重新下载游戏")
        print("下载链接：https://chenmy1903.github.io/wang250")
        input("Enter键退出启动器")
        sys.exit()
    if not os.path.isfile(pip):
        print("依赖安装程序丢失，准备启动自动修复")
        auto = 1
        input("Enter继续，并执行修复")
    if not os.path.isfile(python):
        print("代码运行文件丢失(python.exe)，准备启动自动修复")
        auto = 1
        input("Enter继续，并执行修复")
    if not os.path.isfile(pythonw):
        print("代码运行文件丢失(pythonw.exe)，准备启动自动修复")
        auto = 1
        input("Enter继续，并执行修复")
    if not os.path.isfile(start_api):
        print("启动文件丢失(activate.bat)，准备启动自动修复")
        auto = 1
        input("Enter继续，并执行修复")
    repair(auto)

def repair(config=0):
    if config == -1:
        print("不需要执行修复")
        return
    print("欢迎使用逃离王建国一键修复工具")
    if 'game_path' not in Setting("repair").read():
        Setting("repair").add("game_path", BASE_DIR)
    
    print("""
    游戏无法启动，游戏运行器被损坏按1（注意是游戏运行器，启动器无法被修复，只能重新下载游戏）
    依赖丢失，游戏文件无法正常运行按2
    游戏更新提示失败按3（也包括游戏内联网服务无法正常运行问题）
    桌面游戏快捷方式丢失请按4
    启动游戏请按5
    查看当前路径请按6
    退出修复请按7
    """)
    while True:
        if config:
            print("检测到自动执行代码，开始自动修复")
            res = config
            break
        res = input("请输入问题（序号）：").replace(" ", '')
        try:
            if int(res) > 7 or int(res) == 54188:
                print(f"没有功能{res}")
        except:
            print("输入错误")
        else:
            break
    res = int(res)
    if res == 1:
        print("修复中，请勿关闭窗口")
        with zipfile.ZipFile(os.path.join(GAME_DIR, 'game_runner.zip')) as z:
            z.extractall(GAME_DIR)
        print("修复完成")
        input("Enter退出程序")
    elif res == 2:
        if not os.path.isfile(pip):
            print("依赖安装程序丢失（pip.exe），请使用功能1进行修复")
        try:
            rely_list = eval(requests.get("https://chenmy1903.github.io/wang250/relys").text)
        except:
            rely_list = []
            print("依赖列表获取失败")
            print("请使用功能3进行修复")
            sys.exit()
        print("开始修复，请勿关闭窗口")
        for rely in rely_list:
            if os.system(f"{pip} install {rely} --timeout 10000"):
                print("修复失败，请检查网络连接")
        print("修复完成")
    elif res == 3:
        print("修复方法：")
        print("本问题无法自动修复，需要进行手动修复")
        print("1. 互联网未连接")
        print("2. DNS错误，有恶意程序修改了host文件，所以导致网站无法打开")
        print("3. 王丑菊改的，万恶的王丑菊修改交换机，导致鸭皇官网在南大附小无法访问（王丑菊太可恶了！！！）")
        input("Enter退出")
    elif res == 4:
        if not os.path.isfile(start_game):
            print("启动器文件丢失，请重新下载游戏")
            print("下载链接：https://chenmy1903.github.io/wang250")
            input("Enter退出修复程序")
            sys.exit()
        createShortCut(start_game, f"{os.path.expanduser('~')}/Desktop/逃离王建国.lnk")
        input("修复完成")
    elif res == 5:
        if not os.path.isfile(start_game):
            print("启动器文件丢失，请重新下载游戏")
            print("下载链接：https://chenmy1903.github.io/wang250")
            input("Enter退出修复程序")
        os.system(f"start {start_game}")
    elif res == 6:
        print(f"现在处在的路径是: {BASE_DIR}")
        print(f"游戏路径是：{GAME_DIR}")
        input("Enter确认")
        os.system(f"start {__file__} --repair")
    elif res == 7:
        sys.exit()
    elif res == 54188:
        setting = Setting("config")
        setting.add('coins', 100000000)
        setting.add('diamond', 100000000)
        setting.add('level', 120)
        print("外挂开启成功（建议使用蓝绿修改器，快速成大佬，还不封号[滑稽]）")
        input("Enter退出")

def install():
    os.chdir(BASE_DIR)
    print("初始化设置中")
    config = Setting("repair")
    if not os.path.isdir(os.path.join(BASE_DIR, "game_runner")):
        print("安装启动器中... ...")
        print("安装完成后会自动启动游戏")
        print("安装过程请勿关闭本程序，关闭会导致安装失败")
        with zipfile.ZipFile(os.path.join(BASE_DIR, "game_runner.zip")) as f:
            f.extractall()
        createShortCut(os.path.join(BASE_DIR, "start.exe"), f"{os.path.expanduser('~')}/Desktop/逃离王建国.lnk")
    if rely_list:
        print("开始安装必要组件")
    for rely in rely_list:
        if os.system(f"{os.path.join(BASE_DIR, 'game_runner', 'Scripts', 'pip.exe')} install {rely} --timeout 10000"):
            print(f"安装失败，请检查网络重新更新")
            sys.exit()

    print("检测游戏程序更新")
    try:
        main_code = requests.get("https://chenmy1903.github.io/wang250/play/main.py").text
        game_code = requests.get("https://chenmy1903.github.io/wang250/play/game.py").text
    except:
        print("检测更新失败")
        if os.path.isfile(os.path.join(BASE_DIR, 'main.py')) and os.path.isfile(os.path.join(BASE_DIR, 'game.py')):
            print("游戏程序存在，开始启动游戏")
        else:
            print("游戏程序丢失")
            print("请检测网络是否正常，再重新启动启动器来进行修复")
            input("Enter退出安装")
            sys.exit()
    else:
        with open(os.path.join(BASE_DIR, "main.py"), "w", encoding="UTF-8") as f:
            f.write(main_code)
        with open(os.path.join(BASE_DIR, "game.py"), "w", encoding="UTF-8") as f:
            f.write(game_code)
    print("更新安装目录")
    print(f"dir: \"{BASE_DIR}\"")
    config.add("game_path", BASE_DIR)
    print("初始化环境变量中")
    sys.path.append(BASE_DIR)
    print("初始化模组依赖")
    sys.path.append(os.path.join(BASE_DIR, "ext"))
    print("准备进行安装检测")
    assert_game()
    print("准备运行游戏")
    config.add("runner_version", __version__)
    os.system(f"start {os.path.join(BASE_DIR, 'game_runner/Scripts/activate.bat')}")

def cmd_argument():
    config = Setting("repair")
    parser = argparse.ArgumentParser(__file__.replace('\\', '/').split("/")[-1])
    parser.add_argument("--repair", help="进行游戏修复", action='store_true')
    parser.add_argument("--auto_repair", help="自动检测游戏问题并进行修复", action='store_true')
    if config.read("admin_mode") == "True":
        parser.add_argument("--shell", "--console", help="启动调试终端", action='store_true')
        parser.add_argument("--exec", "-c", help="执行命令")
        parser.add_argument("--unadmin", help="取消登录管理员账号", action='store_true')
    else:
        parser.add_argument("--admin", help="登录管理员账号")
    return parser.parse_args()
    
class Wang250DevConsole(code.InteractiveConsole):
    pass

def start_shell():
    shell = Wang250DevConsole({"Setting": Setting, "exit": sys.exit, "quit": sys.exit, "createShortCut": createShortCut})
    shell.interact()

def title(title: str):
    os.system("title {}".format(title))

def main():
    title("鸭皇游戏")
    config = Setting("repair")
    if "admin_mode" not in config.read():
        config.add("admin_mode", "False")
    argv = cmd_argument()
    admin_mode = config.read("admin_mode") == "True"
    if not admin_mode and argv.admin:
        password = argv.admin
        print("联机认证中，请稍等")
        try:
            web_password = requests.get("https://chenmy1903.github.io/wang250/admin").text
        except:
            print("无网络连接")
            input("Enter退出")
            sys.exit()
        if web_password == password:
            print("通过验证")
            config.add("admin_mode", "True")
            input("Enter退出")
        else:
            print("认证失败")
            input("Enter退出")
    elif admin_mode and argv.unadmin:
        print("已成功移除管理员权限")
        config.add("admin_mode", "False")
        input("Enter退出")
    elif argv.repair:
        title("逃离王建国修复工具")
        repair()
    elif admin_mode and argv.shell:
        title("逃离王建国调试终端")
        start_shell()
    elif admin_mode and argv.exec:
        eval(argv.exec, {"Setting": Setting})
        print("指令执行成功")
        input("Enter退出")
    elif argv.auto_repair:
        title("逃离王建国游戏检测工具")
        assert_game()
    else:
        print("鸭皇·逃离王建国")
        print("正在准备启动，请稍等")
        install()

if __name__ == '__main__':
    main()
