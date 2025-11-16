from dataclasses import dataclass
import time
import random
from typing import Generator

from time_module import MutableWaitTime, MutableWaitTimeAttrClass


def randsleep(start: int | float, end: int | float):
    """startからendの範囲のランダムな値でsleep"""
    try:
        assert (isinstance(start, int) or isinstance(start, float)) and start >= 0
        assert (isinstance(end, int) or isinstance(end, float)) and end >= 0
    except AssertionError:
        raise ValueError("start, endは0以上の数でお願いします。")
    sleep_count = random.uniform(start, end)
    time.sleep(sleep_count)


def countdown(timer: int):
    """コンソールに表示する"""
    try:
        assert isinstance(timer, int) and timer >= 0
    except AssertionError:
        raise ValueError("timerは0以上の整数でおなしゃす。")

    for i in range(timer):
        time.sleep(1)
        print(f"あと{timer - i}秒", end="\r")


class WaitTry(MutableWaitTimeAttrClass):
    """
    フラグが立つまで待機
    Args:
        wait_time (int | float): 待機時間の最大値
        sec (int | float): 待機中の更新間隔
    Usage:
        for _ in WaitTry(10):
            pass
    """

    def __init__(self, wait_time: int | float | MutableWaitTime, sec: int | float | None = None):
        self.wait_time = wait_time
        self._set_sec(sec)
        self._set_count()

    def _set_sec(self, sec: int | float | None = None):
        if sec is None:
            # デフォルト0.1秒
            sec = 0.1
        # バリデーション
        if not isinstance(sec, int | float):
            raise TypeError(f"wait_timeはintかfloatかNoneだけです。入力された型: {type(sec)}")
        if sec <= 0:
            raise ValueError(f"secは0以上です。入力された値: {sec}")
        self.sec = sec

    def _set_count(self):
        self.count = int(self.wait_time / self.sec)
        # 最低1回
        if self.count <= 0:
            self.count = 1

    def __iter__(self) -> Generator[int, None, None]:
        """for文で回せるイテレータ。戻り値として現在の総待機時間を返す"""
        total_wait_time = 0
        for _ in range(self.count):
            time.sleep(self.sec)
            total_wait_time += self.sec
            yield total_wait_time
