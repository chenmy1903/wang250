import os
import sys
import requests

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

lambda run_mod: print("加载成功")
