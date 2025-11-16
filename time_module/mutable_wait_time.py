from dataclasses import dataclass
from abc import ABC


@dataclass
class MutableWaitTime:
    """待機時間(ミュータブル)"""

    wait_time: int | float

    def __post_init__(self):
        if not isinstance(self.wait_time, int | float):
            raise TypeError(f"wait_timeはintかfloatだけです。入力された型: {type(self.wait_time)}")
        if self.wait_time < 0:
            raise ValueError(f"wait_timeは0以上のみです。入力された値: {self.wait_time}")


class MutableWaitTimeAttrClass(ABC):
    """ミュータブルなwait_timeを持つクラス"""

    def branch_wait_time(self, wait_time: int | float | None = None):
        """新規MutableWaitTimeを作り、他MutableWaitTimeAttrClassとのつながりを断つ"""
        if wait_time is None:
            try:
                self._wait_time = MutableWaitTime(self._wait_time.wait_time)
                return
            except AttributeError:
                raise AttributeError("既存のwait_timeがない状態でNoneだと新規MutableWaitTimeが作れません。")
        self._wait_time = MutableWaitTime(wait_time)

    @property
    def wait_time(self) -> int | float:
        return self._wait_time.wait_time

    @wait_time.setter
    def wait_time(self, wait_time: int | float | MutableWaitTime):
        if not isinstance(wait_time, int | float | MutableWaitTime):
            raise TypeError(f"wait_timeはintかfloatかMutableWaitTimeだけです。入力された型: {type(wait_time)}")
        # MutableWaitTimeをそのまま使う場合
        if isinstance(wait_time, MutableWaitTime):
            self._wait_time = wait_time
            return
        # 入力されたwait_timeをミュータブルのまま適用させる
        try:
            self._wait_time.wait_time = wait_time
        # 定義されていない場合はMutableWaitTimeオブジェクトを定義
        except AttributeError:
            self._wait_time = MutableWaitTime(wait_time)
