# 测试

## 1. 使用mods组件制作一个音乐播放器

> 音频：[下载](/wang250/play/files/game_bg.mp3)

> 至少1.6版本的mods才可运行

```bash
# 升级指令
python -m pip install -U wang250-mods
# 或
python -m pip install --upgrade wang250-mods
```

要求：

1. 有定时播放，无限播放两种模式
2. 可以设置播放时间，而且重启游戏无需重新设置
3. 可以实时显示剩余的播放时间
4. 只能使用规定的包（如果要浏览文件，可以引用wxpython, PyQt5, tkinter等组件，但是不能用这些组件做其他的UI）
5. 下面是文件开头（没有写错，不许用sys结束进程，`exit()`也不行）

```python
from mods.mod_tools import Setting
from mods.test import test
from mods.base_surface import Window, UI

from pygame.locals import *

import pygame
import time
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

TITLE = "音频播放器"
run_on_load = False


class SoundWindow(Window):
    ... # 后面就要自己写了
```

6. 下面是测试代码的方法

```python
if __name__ == "__main__":
    test(SoundWindow)
```

# 答案

> 建议先尝试，不要一上来就看答案

## 测试1

> 题目：使用mods组件制作一个音乐播放器

为了防止偷看答案，请点击[此处](test1_code.py)下载。
