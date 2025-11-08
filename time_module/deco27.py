# デコレータ
from functools import wraps
import time


def measure_time(func):
    """時間計測デコレータ"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 実行開始時間を記録
        result = func(*args, **kwargs)
        end_time = time.time()  # 実行終了時間を記録
        elapsed_time = end_time - start_time
        print(f"関数 '{func.__name__}' 実行時間 is {elapsed_time:.4f} seconds.")
        return result

    return wrapper
