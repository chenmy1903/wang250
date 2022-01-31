import random
import time
import sys
import os

from mods.mod_tools import Setting, random_gift

config = Setting("wufu")

def cards(sleep=True):
    if not config.read("次数") > 0:
        print("你没有次数了，快用朋友兑换吧~")
        if not sleep:
            return False
        for i in range(3, 0, -1):
            print(f"将于{i}秒后返回", end="\r")
            time.sleep(1)
            return False
    if random_gift(1):
        print("恭喜你获得\033[31m幸运卡\033[0m")
        config.add("幸运", config.read("幸运") + 1)
    elif random_gift(20):
        print("恭喜你获得财运卡")
        config.add("财运", config.read("财运") + 1)
    elif random_gift(40):
        print("恭喜你获得福运卡")
        config.add("福运", config.read("福运") + 1)
    else:
        add_card = random.choice(["鸿运", "禧运"])
        print(f"恭喜你获得{add_card}卡")
        config.add(add_card, config.read(add_card) + 1)
    config.add("次数", config.read("次数") - 1)
    if not sleep:
        return True
    for i in range(3, 0, -1):
        print(f"将于{i}秒后返回", end="\r")
        time.sleep(1)
    return True

def init_cards():
    config.null_add("次数", 3) # 免费赠送3次
    config.null_add("财运", 0)
    config.null_add("鸿运", 0)
    config.null_add("禧运", 0)
    config.null_add("福运", 0)
    config.null_add("幸运", 0)

def input_coin():
    print("正在氪金")
    friends(100)

def friends(n: int = 1):
    print(f"你失去了{n}个好友，但是获得了{n}次机会")
    config.add("次数", config.read("次数") + n)


def get_cards():
    for key, value in config.read().items():
        if key.endswith("运"):
            print(f"拥有{key}{value}张")
    for i in range(5, 0, -1):
        print(f"将于{i}秒后返回", end="\r")
        time.sleep(1)

def exec_cards():
    all_cards = [
        config.read("财运"),
        config.read("鸿运"),
        config.read("禧运"),
        config.read("福运"),
        config.read("幸运"),
    ]
    if all(all_cards):
        print("正在合成")
        print("防止你要把卡片送给好友，所以我们清空了您所有的幸运卡片")
        print("获得了666元")
        config.add("幸运", 0)

def clear():
    os.system("cls")

def while_cards():
    while cards(False):
        pass

def main():
    commands = {"1": cards, "2": get_cards, "3": input_coin, "4": friends, "5": exec_cards, "6": while_cards, "7": sys.exit}
    init_cards()
    clear()
    print("拼夕夕集五福，绝对不坑（doge）")
    while True:
        print("""欢迎光~临，超级坑集五福，前10000集齐可以获得亿元
1. 抽卡
2. 查看你的卡
3. 氪金（可以获得亿次机会）
4. 找好友助力
5. 合成
6. 自动抽卡
7. 退出
""")
        print(f"机会：{config.read('次数')}")
        while True:
            res = input("请输入序号，开启友尽模式：").replace(" ", "")
            if res in commands:
                clear()
                commands[res]()
                clear()
                break
            print("输入错误，这样你坑不到你的朋友")
        

if __name__ == '__main__':
    main()