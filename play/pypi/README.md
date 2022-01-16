# 逃离王建国模组依赖

> 项目官网：https://chenmy1903.github.io/wang250/

> 完整版开发者教程：https://chenmy1903.github.io/wang250/mods/make_mod/

> 项目GitHub：https://github.com/chenmy1903/wang250/

> 官网：https://chenmy1903.github.io/

> 快手：chenmy1903

## 测试安装

> 我们需要先安装它
```
pip install wang250-mods
```
> 然后创建一个python文件
```python
from mods import Window # 简便写法
# from mods.base_surface import Window # 标准写法
from mods.test import test # 导入测试组件

if __name__ == "__main__":
    test(Window) # 使用调试模式启动

```
> 然后运行它，你懂的
```batch
python main.py
```
> 如果出现了一个黑窗口，那么就说明安装成功了
