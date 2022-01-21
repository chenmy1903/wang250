# 将本文件放入ext文件夹中即可替换原来的游戏
# 本模组自带编辑器
# 格式：
# "//"为单行注释
# "map start:"为地图起始符
# "map end:"为地图终止符
# "!"为告示牌，可以进行新手教程
# "@是路"
# "#"是敌人
# "$"为重生点（只能有一个）
# "^"是玩家
# "&"是墙
# 文件示例

from mods.base_surface import Window, UI
from mods.mod_tools import Setting, cmd_text

from pygame.locals import *
import pygame

class Setting(Setting):
    def __init__(self, file_name: str, config={}, config_path="~/.duck_game/wang250/map"):
        Setting.__init__(self, file_name, config, config_path)

def get_null_map(size: int):
    row_x = []
    for x in range(size[0]):
        row_x.append("@")
    return [row_x for i in range(size[1])]

def read_map_file(config: Setting):
    map_text = Setting("jingu_maps")
    with open(map_file.try_get("map", os.path.join(BASE_DIR, "map.txt"))):
        pass
    if not play_map:
        return False
    return play_map

class MapWindow(Window):

    def __init__(self, surface: pygame.Surface, config: Setting):
        Window.__init__(self, surface, config)
        self.ui = UI()
        self.ui.set_surface(self.surface)
        self.DISPLAYSURF = self.surface

    def blit_map(self):
        read_map_file

def main():
    pass

if __name__ == '__main__':
    main()
