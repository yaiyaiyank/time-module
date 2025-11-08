# timeモジュール

自分のエコシステム用につくった†時間操作†モジュール<br>
役立ちそう ∧ 機密情報なし なのでパブリックで公開

# install
### 動作環境
* Python 3.13↑
### インストール方法 
uvなら
```bash
uv add git+https://github.com/yaiyaiyank/time-module
```
pipなら
```bash
pip install git+https://github.com/yaiyaiyank/time-module
```
### 備考
標準ライブラリのみで完結するので外部ライブラリ依存なし

# usage

```python
from time_module import randsleep

# 指定した2つの秒数の範囲内でランダムにスリープする。スクレイピングなどで使う。
randsleep(2, 5)
```
```python
from time_module import countdown

# 指定した秒数、コンソールにカウントダウンを表示する。bashのtimeoutコマンドをPythonで使う感じ(?)。
countdown(3)
```
```python
from time_module import measure_time, randsleep

# 関数の実行時間を計測するデコレータ
@measure_time
def func():
    randsleep(4, 9)
```

### 実装予定
```python
from time_module import Time

time_ = Time(4200)
print(time_.hour) # -> 1
print(time_.minute) # -> 10
```