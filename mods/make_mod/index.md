# 逃离王建国·mods

## Setting类\钻石、金币修改教程

下面代码为Setting类的代码

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
        if value:
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

## 终端文本输出（用于制作公告）

先来看源代码
```python
def cmd_text(text: str, end_function=None):
    text_r = text.replace('\n', '-')
    run_path = os.path.join(sys.exec_prefix, "python.exe")
    os.system(f"start {run_path} -c \"text = '''{text_r}'''; print(text.replace('-', '\\n')); input('Enter关闭本窗口')\"")
    if end_function:
        end_function()
```

运行会弹出一个cmd窗口，并显示 {text}，