"""一些特殊的事件的实现方法"""
# ©chenmy1903
# by 鸭皇
# GitHub: 王建国

from pygame.locals import KEYUP, KEYDOWN


class EventObject(object):
    """提供HOLD（按住按键的检测）"""
    hold = False

    def hold_event(self, event, key: int):
        """检测按键的HOLD事件，并将结果输出到self.hold
        event: pygame的事件列表
        key: 要被按下的按键（按键码，与pygame.locals通用）
        """
        if event.type == KEYUP:
            if event.key == key:
                self.hold = False
        if event.type == KEYDOWN:
            if event.key == key:
                self.hold = True
        
