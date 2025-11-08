from dataclasses import dataclass
import time
import random


def randsleep(start: int | float, end: int | float):
    """startからendの範囲のランダムな値でsleep"""
    try:
        assert (isinstance(start, int) or isinstance(start, float)) and start >= 0
        assert (isinstance(end, int) or isinstance(end, float)) and end >= 0
    except AssertionError:
        raise ValueError("start, endは0以上の数でお願いします。")
    ru = random.uniform(start, end)
    time.sleep(ru)


def countdown(timer: int):
    """コンソールに表示する"""
    try:
        assert isinstance(timer, int) and timer >= 0
    except AssertionError:
        raise ValueError("timerは0以上の整数でおなしゃす。")

    for i in range(timer):
        time.sleep(1)
        print(f"あと{timer - i}秒", end="\r")


class WaitTry:
    """
    フラグが立つまで待機
    Args:
        sec (int | float): 待機中の更新間隔
        count (int): 更新回数
    Usage:
        wait_try = WaitTry()
        wait_try.decide_count(10) # 10秒待機

        for _ in range(wait_try.count) # ここyeildでrangeいらなそう
            # フラグが立ったら抜ける
            if is_flag():
                break
            wait_try.sleep() # ここyeildで更に省略できそう

    """

    def __init__(self):
        self.sec: int | float | None = None
        self.count: int | None = None

    def wait_setting(self, wait_time: int | float, sec: int | float | None = None):
        if sec is None:
            # デフォルト0.1秒
            self.sec = 0.1
        else:
            self.sec = sec
        self._validation(wait_time)
        self.count = int(wait_time / self.sec)
        # 最低1回
        if self.count <= 0:
            self.count = 1

    def _validation(self, wait_time: int | float):
        if not isinstance(self.sec, int | float):
            raise TypeError
        if self.sec <= 0:
            raise ValueError
        if not isinstance(wait_time, int | float):
            raise TypeError
        if wait_time < 0:
            raise ValueError

    def __iter__(self):
        total_wait_time = 0
        for _ in range(self.count):
            time.sleep(self.sec)
            total_wait_time += self.sec
            yield total_wait_time
