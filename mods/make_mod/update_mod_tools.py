import requests
import shutil
import argparse
import ctypes
import sys
import pip
import os

from pip._internal.commands.show import search_packages_info
from pip._internal.utils.misc import get_installed_distributions




pygame_version = "2.1.2"
requests_version = "2.26.0"
pickleshare_version = "0.7.5"
__version__ = "1.3"

init_py = init_py.format(__version__)


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
    parser.add_argument('--version', "-v", action='version', version='mod_tools {}'.format(__version__), help="????????????")
    parser.add_argument("--install", help="????????????mod_tools", action='store_true')
    parser.add_argument("--uninstall", help="??????mod_tools", action='store_true')

    return parser.parse_args()

def title(text: str):
    os.system(f"title {text}")

def pause():
    os.system("pause")

def uninstall():
    title("???????????? - Package Manger")
    print("????????????????????????mod_tools")
    print(f"???????????????Python: {sys.executable}")
    print("???????????????????????????????????????")
    site_packages = os.path.join(sys.exec_prefix, "Lib", "site-packages")
    install = os.path.join(site_packages, 'mods')
    if not os.path.isdir(site_packages):
        print("?????????????????????pyinstaller???????????????????????????????????????")
        print("error: no site-packages floor", file=sys.stderr)
        pause()
        sys.exit()
    if not os.path.isdir(install):
        print("???????????????mod_tools")
        pause()
        sys.exit()
    try:
        shutil.rmtree(install)
        print("????????????")
        pause()
    except PermissionError:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__ + " --uninstall", None, 1)


def install(q=False):
    title("???????????? - Package Manger")
    print("??????????????????mod_tools????????????????????????Python???")
    print("???????????????????????????????????????")
    print(f"???????????????Python: {sys.executable}")
    site_packages = os.path.join(sys.exec_prefix, "Lib", "site-packages")
    pygame_install = False
    requests_install = False
    pickleshare_install = False
    tools_install = False
    for name, version, location in pip.get_all_packages():
        if name == "pygame":
            pygame_install = True
        if name == "requests":
            requests_install = True
        if name == "pickleshare":
            pickleshare_install = True
        if name == "mods":
            tools_install = True
            tinstall_version = pip.get_package_info("mods")
    install = os.path.join(site_packages, 'mods')
    if not os.path.isdir(site_packages):
        print("?????????????????????pyinstaller???????????????????????????????????????")
        print("error: no site-packages floor", file=sys.stderr)
        pause()
        sys.exit()
    print(f"???????????????{install}")
    if not os.path.isdir(install):
        os.mkdir(install)
        mode = "install"
    else:
        mode = "update"
    print("??????" + ("??????" if mode == "install" else "??????") + "mod_tools")
    print("????????????")
    try:
        print("?????????PyPi?????????")
        pip.upgrade("mods")
        if not pygame_install:
            if pip.install(f"pygame=={pygame_version}"):
                raise PermissionError()
        if not requests_install:
            if pip.install(f"requests=={requests_version}"):
                raise PermissionError()
        if not pickleshare_install:
            if pip.install(f"pickleshare=={pickleshare_version}"):
                raise PermissionError()
        print("???????????????Enjoy")
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
