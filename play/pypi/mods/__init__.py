"""逃离王建国的模组依赖
官网：https://chenmy1903.github.io/wang250/
用法：https://chenmy1903.github.io/wang250/mods/make_mod/
"""
# 此版本修复安装失败的问题

from .mod_tools import *
from .base_surface import Window
from .events import EventObject
from .test import test

from . import mod_tools, base_surface, events, test

__version__ = '1.7.4'
