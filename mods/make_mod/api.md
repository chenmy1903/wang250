# 逃离王建国 · mods

### 这里才是真正的教程

> 建议看完前面的教程再来看这个教程，这个更深入，方法全部来自mods包，前面是里边的实现方法，了解了前面后面就易懂了

> 这里只有新内容才会出现注释，建议读前面的打好基础

> 这里的代码都可以直接复制进`ext`文件夹


## 2. mods包的HOLD事件

> 之前我以为实现不了，但是实现了

```python
from mods.events import EventObject # 导入事件类
from mods.base_surface import Window
from mods.mod_tools import Setting # 导入设置类

from pygame.locals import QUIT, KEYUP, K_w, ESCAPE

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
                    if event.key == ESCAPE:
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
    run_mod(surface)
    sys.exit() # 防止未响应

if __name__ == "__main__":
    _test()
```

## 使用mods包进行测试

```python
from mods.base_surface import Window
from mods.test import test # 导入mods.test包

TITLE = "test"
run_on_load = False

if __name__ == "__main__":
    test(Window) # Window类本身就是一个基本的窗口，放进入自动运行

```
