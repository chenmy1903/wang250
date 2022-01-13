import requests
import shutil
import argparse
import ctypes
import sys
import pip
import os

from pip._internal.commands.show import search_packages_info
from pip._internal.utils.misc import get_installed_distributions



init_py = """\"\"\"逃离王建国的模组依赖\"\"\"
# by鸭皇
# https://chenmy1903.github.io/wang250/
# ©chenmy1903
# Github: 王建国
# 禁止盗用
from . import mod_tools
from .base_surface import Window
"""

pygame_version = "2.1.2"
requests_version = "2.26.0"
pickleshare_version = "0.7.5"
__version__ = "1.0"


class PyPiError(Exception):

    pass


class object_pip(object):
    def __init__(self):
        object.__init__(self)

    def install(self, *packages):
        return os.system(f'{sys.executable} -m pip install {" ".join(packages)} --timeout 1000')

    def uninstall(self, *packages):
        return os.system(f'{sys.executable} -m pip uninstall {" ".join(packages)} -y')

    def force_reinstall(self, *packages):
        return os.system(f'{sys.executable} -m pip install {" ".join(packages)} --force-reinstall --timeout 1000')

    def upgrade(self, *packages):
        return os.system(f'{sys.executable} -m pip install {" ".join(packages)} --upgrade --timeout 1000')

    def get_all_packages(self):
        installed_packages = get_installed_distributions()
        for package in installed_packages:
            yield package.project_name, package.version, package.location

    def get_package_info(self, package_name: str):
        distributions = search_packages_info([package_name])
        messages = {}
        for dist in distributions:
            messages['name'] = dist.get('name', '')
            messages['version'] = dist.get('version', '')
            messages['summary'] = dist.get('summary', '')
            messages['home-page'] = dist.get('home-page', '')
            messages['anthor'] = dist.get('author', '')
            messages['location'] = dist.get('location', '')
            messages['requires'] = dist.get('requires', [])
            messages['requires_by'] = dist.get('required_by', [])
        return messages

pip = object_pip()

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def cmd_argument():
    parser = argparse.ArgumentParser(__file__.replace('\\', '/').split("/")[-1])
    parser.add_argument("--install", help="静默安装mod_tools", action='store_true')
    parser.add_argument("--uninstall", help="卸载mod_tools", action='store_true')

    return parser.parse_args()

def title(text: str):
    os.system(f"title {text}")

def pause():
    os.system("pause")

def uninstall():
    title("鸭皇游戏 - Package Manger")
    print("本程序将为您移除mod_tools")
    print(f"现在运行的Python: {sys.executable}")
    print("失败可以使用管理员权限试试")
    site_packages = os.path.join(sys.exec_prefix, "Lib", "site-packages")
    install = os.path.join(site_packages, 'mods')
    if not os.path.isdir(site_packages):
        print("请不要尝试使用pyinstaller以及任何打包程序打包此文件")
        print("error: no site-packages floor", file=sys.stderr)
        pause()
        sys.exit()
    if not os.path.isdir(install):
        print("您没有安装mod_tools")
        pause()
        sys.exit()
    try:
        shutil.rmtree(install)
        print("移除完成")
        pause()
    except PermissionError:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__ + " --uninstall", None, 1)


def install(q=False):
    try:
        mod_tools = requests.get("https://chenmy1903.github.io/wang250/play/mod_tools.py").text
        base_surface = requests.get("https://chenmy1903.github.io/wang250/play/base_surface.py").text
        events = requests.get("https://chenmy1903.github.io/wang250/play/events.py").text
        test = requests.get("https://chenmy1903.github.io/wang250/play/test.py").text
    except:
        print("资源下载失败")
        if not q:
            pause()
    title("鸭皇游戏 - Package Manger")
    print("本程序为您将mod_tools集成到现在运行的Python中")
    print("失败可以使用管理员权限试试")
    print(f"现在运行的Python: {sys.executable}")
    site_packages = os.path.join(sys.exec_prefix, "Lib", "site-packages")
    pygame_install = False
    requests_install = False
    pickleshare_install = False
    for name, version, location in pip.get_all_packages():
        if name == "pygame":
            pygame_install = True
        if name == "requests":
            requests_install = True
        if name == "pickleshare":
            pickleshare_install = True
    install = os.path.join(site_packages, 'mods')
    if not os.path.isdir(site_packages):
        print("请不要尝试使用pyinstaller以及任何打包程序打包此文件")
        print("error: no site-packages floor", file=sys.stderr)
        pause()
        sys.exit()
    print(f"将要安装至{install}")
    if not os.path.isdir(install):
        os.mkdir(install)
        mode = "install"
    else:
        mode = "update"
    print("准备" + ("安装" if mode == "install" else "更新") + "mod_tools")
    print("开始写入")
    try:
        with open(os.path.join(install, "mod_tools.py"), "w", encoding="UTF-8") as f:
            print("写入mod_tools.py")
            f.write(mod_tools)
        with open(os.path.join(install, "base_surface.py"), "w", encoding="UTF-8") as f:
            print("写入base_surface.py")
            f.write(base_surface)
        with open(os.path.join(install, "events.py"), "w", encoding="UTF-8") as f:
            print("写入events.py")
            f.write(events)
        with open(os.path.join(install, "test.py"), "w", encoding="UTF-8") as f:
            print("写入test.py")
            f.write(test)
        with open(os.path.join(install, "__init__.py"), "w", encoding="UTF-8") as f:
            print("写入__init__.py")
            f.write(init_py)
        if not pygame_install:
            if pip.install(f"pygame=={pygame_version}"):
                raise PermissionError()
        if not requests_install:
            if pip.install(f"requests=={requests_version}"):
                raise PermissionError()
        if not pickleshare_install:
            if pip.install(f"pickleshare=={pickleshare_version}"):
                raise PermissionError()
        print("安装完成，Enjoy")
        if not q:
            pause()
    except PermissionError:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

def main():
    argv = cmd_argument()
    if argv.install:
        install(True)
    elif argv.uninstall:
        uninstall()
    else:
        install()

if __name__ == "__main__":
    main()
