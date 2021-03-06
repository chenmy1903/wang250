# 逃离王建国·mods

## 更新日志

## 2022/1/11

1. 修复代码中的错误
2. 增加更详细的教程
3. 更新mod_tools，旧版本与新版本不兼容，请打开游戏进行更新

## 2022/1/12

1. 增加安装工具，可以将mod_tools集成到Python中（不是逃离王建国的Python，是系统中安装的Python）
2. 增加mods.base_surface类
3. 增加完整版（现在看的是新手教程）

[完整版](api.html)

## 2022/1/13

1. 修复Setting类的错误

# 1022/1/21

1. 修复bug (1.6.2版本)
2. 我们更新了1.7版本，要去[看看](whats-new-in-1.7.html)增加了什么吗

## 从PyPi安装mod_tools

> 2022/1/16 将mods包上传到pypi了

```batch
pip install wang250-mods
```

[点击下载](https://pypi.org/project/wang250-mods/)

<!-- > 推荐从游戏安装目录运行mod_tools安装程序进行安装mod_tools，上面的安装程序可能不是最新版

> 如果安装了游戏，所有人的安装命令都是`python C:/wang250/update_mod_tools.py --install`

> 卸载命令是`python C:/wang250/update_mod_tools.py --uninstall`

```bash
# 命令行操作
# 安装直接双击即可
# 卸载
python update_mod_tools.py --uninstall
# 静默安装
python update_mod_tools.py --install
```-->

## 0. Setting类\钻石、金币修改教程

下面代码为Setting类的代码
> 本章已停止维护，请移步[新文档](api.html)。

```python
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
        new[key] = value
        self.db[self.file_name] = new

    def read(self, config=None):
        """读文件"""
        if config:
            return self.db[self.file_name][config]
        return self.db[self.file_name]
```

### 1. __init__ 函数

定义：
```python
__init__(self, file_name, config={}, config_path="~/.duck_game/wang250/mods")
```
file_name: 存档文件的名称

config: 存档内容

config_path: 存档目录，模组内调用必须为"~/.duck_game/wang250/mods"

### 2. add函数
定义：
```python
add(self, key, value):
```

key: 目标名称

value: 目标值

这样说大家是不是有点难以理解，下面看个示例

```python
setting = Setting("jianguo")
setting.add("wangjianguo", "chenwenli") # 将目标 "wangjianguo" 设为 "chenwenli"
print(setting.read()) # 读取数据，返回 {"wangjianguo": "chenwenli"}
print(setting.read("wangjianguo")) # 读取数据db["wangjianguo"]，返回"chenwenli"
# setting.read("chenwenli") # 存档文件没有目标"chenwenli"，抛出KeyError
```

## 3. read函数
定义：
```python
read(self, config=None)
```

config: 目标名称，默认为`None`

如果`config`参数为`None`，则返回存档文件中全部的数据，否则返回`db[config]`

下面还是一个示例

```python
setting = Setting("jianguo")
print(setting.read()) # 返回{}
setting.add("wangjianguo", "chenwenli")
print(setting.read()) # 返回{"wangjianguo", "chenwenli"}
print(setting.read("wangjianguo")) # 返回 'chenwenli'
```

## 4. 终端文本输出（用于制作公告）

先来看源代码
```python
def cmd_text(text: str, end_function=None):
    text_r = text.replace('\n', '-')
    run_path = os.path.join(sys.exec_prefix, "python.exe")
    os.system(f"start {run_path} -c \"text = '''{text_r}'''; print(text.replace('-', '\\n')); input('Enter关闭本窗口')\"")
    if end_function:
        end_function()
```

运行会弹出一个cmd窗口，并显示 {text}

## 5. 标准模组文件
```python
import pygame # 在这里导入包
from pygame.locals import *

from mods.mod_tools import * # 导入模组工具

TITLE = "模组名字"
run_on_load = True # 是否为加载项True为是，False为假（加载项见下面词条）

class Window(object):
    """游戏主体"""
    ...

def run_mod(**kwargs): # 必须加**kwargs
    """运行模组的脚本"""
    pass
```

### 6. 游戏主体的编写

> tip: 这里不是教pygame的，只是教基本的东西

```python

import pygame
import os # 第8章中会用
import sys
from pygame.locals import *

from mods.mod_tools import * # 导入模组工具

TITLE = "模组名字"
run_on_load = False # 是否为加载项True为是，False为假（加载项见最下面词条）

class Window(Text): # 继承mod_tools.Text
    def __init__(self, surface: pygame.Surface):
        Text.__init__(self)
        # 在这里设变量
        self.config = Setting(TITLE) # 初始化设置类（设置类来自mod_tools包）
        self.surface = surface # 设置屏幕
        self.set_surface(self.surface) # 调用mod_tools.Text.set_surface进行初始化
    
    def start(self): # 运行游戏部分
        while True:
            self.surface.fill((0, 0, 0)) # 填充颜色
            # 游戏主循环在这写
            for event in pygame.event.get(): # 获取事件列表
                if event.type == QUIT: # 检测退出事件
                    pygame.quit()
                    sys.exit()
            pygame.display.update()
            self.clock.tick(self.FPS) # 控制帧数 FPS是系统设置中的FPS，可以改为自己的

```

## 7. 提示框选择框gui

```python
# 我们在上一章中已经做好了主gui，接下来我们实现按l键弹出提示框，按k弹出选择框
class MessageWindow(Window): # 继承上一章编写的Window类
    # __init__ 我们不用再写了，我们已经写过了
    def start(self): # 重写运行部分
        game_mode = True
        while game_mode:
            self.surface.fill((0, 0, 0)) # 填充颜色
            # 游戏主循环在这写
            for event in pygame.event.get(): # 获取事件列表
                if event.type == QUIT: # 检测退出事件
                    # pygame.quit()
                    # sys.exit() 这样做是错的，模组文件不支持这样写
                    game_mode = False # 将游玩设为假
                elif event.type == KEYUP: # 检测松开按键（pygame中没有hold逻辑，下一章中会讲）
                    if event.key == K_l: # 判断按键是否为L
                        self.message("我是金古") # 调用mod_tools.Text.message
                    elif event.key == K_k: # 判断按键是否为K:
                        if self.ask_yes_no("金古要趋势了，你开心吗"):
                            self.message("你按下了是")
                        else:
                            self.message("你按下了否")
                    elif event.key == K_ESCAPE:
                        game_mode = False

            pygame.display.update()
            self.clock.tick(self.FPS) # 控制帧数 FPS是游戏设置中的FPS，可以改为自己的
```

## 8. HOLD逻辑

```python
# hold即为按住按键的时候触发的事件，这个事件Unity中有，但是pygame中没有
# 我们继承第六章中编写的Window类
class HoldWindow(Window):
    def start(self):
        game_mode = True
        forward = False # 前进状态为假
        x, y = 20, 20 # 初始化x轴和y轴的值，为20, 20
        player = pygame.image.load(os.path.join(BASE_DIR, "图片的名称")) # 图片自备，把图片放在本模组文件一样的目录即可
        # BASE_DIR是mod文件夹，os.path.join是连接两个目录
        while game_mode:
            self.surface.fill((0, 0, 0)) # 填充颜色（清空画布），在它前面显示的东西都会消失
            self.surface.blit(player, (x, y)) # 显示图像
            if forward: # 如果forward触发
                x += 5 # 向前移动5像素
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_mode = False
                if event.type == KEYUP: # 检测按键松开
                    if event.key == K_w:
                        forward = False # 将前进状态设为假
                    elif event.key == K_ESCAPE:
                        game_mode = False
                if event.type == KEYDOWN: # 检测按键按下
                    if event.key == K_w:
                        forward = True # 将前进状态设为真
            pygame.display.update() # 更新画面
            self.clock.tick(self.FPS) # 控制帧数

```

## 9.运行

> 运行事例请修改里边使用的类名称（Window）

```python
def run_mod(**kwargs):
    pygame.init()
    surface = kwargs["surface"] # 获取主窗口
    window = Window
    # window = MessageWindow # 设为前面做过的类
    # window = HoldWindow
    window = window(surface) # 实例化
    window.start() # 开启玩法

_test = run_mod
pygame.init()

window_info = pygame.display.Info()
WINWIDTH = window_info.current_w
WINHEIGHT = window_info.current_h

if __name__ == "__main__":
    _test(surface=pygame.display.set_mode((WINWIDTH, WINHEIGHT))) # 测试

```

## 10. 坚果百科 - 加载项

1. 加载项为进入游戏（应用）自动加载的程序

