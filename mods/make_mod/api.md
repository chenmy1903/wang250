# 逃离王建国 · mods

### 这里才是真正的教程

> 建议看完前面的教程再来看这个教程，这个更深入，方法全部来自mods包，前面是里边的实现方法，了解了前面后面就易懂了

> 这里只有新内容才会出现注释，建议读前面的打好基础

> 这里的代码都可以直接复制进`ext`文件夹

> 运行本教程最低mods包版本: 1.6，可以通过`mods.__version__`查看

> 如果要挑战一下自己，你可以去[测试](tests.html)页面

## 1. 安装

> 1.4以后的版本将会上传到PyPi，游戏内安装器将会失效

```batch
pip install wang250-mods
```

## 2. 新Setting类

> 修复bug：值为假添加失败

导入：

```python
from mods.mod_tools import Setting

config = Setting("模组名字", {}) # __init__(设置项的名字, 默认设置={})
```

读取整个配置文件：

```python
config.read() # -> dict
```

读取一个值：

```python
config.read("项名") # 如果不存在抛出KeyError
```

尝试读取一个值：

```python
config.try_get("项名", 如果不存在返回的默认值) # 默认值默认为None
```

不存在则添加某个值：

```python
config.null_add("项名", "项值") # 项值默认为None
```

删除某个值：

```python
config.delete("项名")
```


## 3. mods包的HOLD事件

> 之前我以为实现不了，但是实现了

```python
from mods.events import EventObject # 导入事件类
from mods.base_surface import Window
from mods.mod_tools import Setting # 导入设置类

from pygame.locals import QUIT, KEYUP, K_w, K_ESCAPE

import pygame
import sys
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 文件所在目录（绝对）

TITLE = "hold"
run_on_load = False

class HoldWindow(Window):

    def __init__(self, surface: pygame.Surface, config: Setting): # 新版api：需要提供设置项
        Window.__init__(self, surface, config) # 使用父类的初始化方法
        self.event = EventObject() # 实例化事件类

    def start(self):
        game_mode = True
        player = pygame.image.load(os.path.join(BASE_DIR, "player.png")) # 图片自备
        x, y = 60, 60
        while game_mode:
            self.surface.blit(player, (x, y)) # 这里的surface已经被定义了，在Window.__init__中有设置surface变量的过程
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_mode = False
                elif event.type == KEYUP:
                    if event.key == K_ESCAPE:
                        game_mode = False
                self.event.hold_event(event, K_w) # 检测按住按键事件
            if self.event.hold: # 如果被按下
                x -= 1

def run_mod(**kwargs):
    surface = kwargs["surface"]
    window = HoldWindow(surface, TITLE)
    window.start()

def _test():
    pygame.init() # 初始化pygame
    surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("hold事件") # 设置题目
    run_mod(surface=surface)
    sys.exit() # 防止未响应

if __name__ == "__main__":
    _test()
```

## 4. 使用mods包进行测试

```python
from mods.base_surface import Window
from mods.test import test # 导入mods.test包

TITLE = "test"
run_on_load = False

if __name__ == "__main__":
    test(Window) # Window类本身就是一个基本的窗口，放进入自动运行

```

## 5. GUI布局

> 现在只支持按钮和文本框

### 按钮

```python
from mods.base_surface import UI, Window # 导入UI类

import pygame
from pygame.locals import QUIT

```

> tip: 使用前请务必不要忘记实例化`UI`类

ui是需要和Window类结合使用的

> 先创建一个类(继承Window)

```python
class UIButton(Window):
    ui = UI() # 实例化ui（存入self.ui）
```

> 我们在start函数中添加按钮

```python
class UIButton(Window):
    ui = UI() # 实例化ui（存入self.ui）
    
    def start(self):
        game_mode = True
        while game_mode:
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_mode = False
            pushbutton = self.ui.button("点一下开挂", (100, 100), 72) # --> Button 返回一个Button对象
            # 按钮定义
            # def button(self, text: str, pos: tuple, size: int = 18) --> Button:
            if pushbutton.is_hold(): # 判断是否被按下
                self.message("外挂开启成功，奖励你10年大礼包") # 提示消息

```
