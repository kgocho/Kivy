# Kivy
GUIの勉強を兼ねて、Kivyを利用してファイル入力＋処理＋グラフを表示できるGUIプログラムを作成。

# 作成プログラム
omronの体組成計のスマホアプリから出力した測定結果のcsvファイルを読み込みグラフ表示するプログラム。
体脂肪量(Kg)、骨格筋量(Kg)がアプリでは見れないため(体脂肪率(%)、骨格筋率(%)のデータしかないため)、ファイル読み込み時に体脂肪量(Kg)、骨格筋量(Kg)を自動計算し表示できるようにする。

# 必要ライブラリ
* Kivy 2.0.0
* matplotlib 3.2.2*
* pandas 1.2.4

\* matplotlibに関しては3.2.2以下のバージョン出ないとエラーになるので注意 [^1] \*

[^1]: 実行時に`ImportError: cannot import name '_png' from 'matplotlib'`がエラーとして出力される。

# Installation
```bash
pip install kivy
pip install pandas
pip install matplotlib==3.2.2
```

もしmatplotlibをすでに新しいバージョンでインストールしている場合は以下コマンドでダウングレードする。

```bash
pip install -U "matplotlib<3.3.0"
```

# Usage
```bash
python body_composition.py
```

# Demo
