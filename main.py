import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

# CSVファイルのパスを設定する
BASE_DIR = os.path.dirname(__file__) # pyファイルの場所
file_path = os.path.join(BASE_DIR, "data.csv") # pyファイルの場所+CSVファイル名でパスを設定

# 引数でファイル名が指定されない場合は、同ディレクトリのデフォルトCSVを読み込む
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = file_path

try:
    # グラフ用データ
    df = pd.read_csv(filename)

    # グラフの表示
    plt.plot(df["date"], df["sales"]) # グラフ作成
    plt.savefig("graph.png") # 保存
    plt.show() # 表示（show()でバッファがクリアされるから、保存後にやる）

except Exception as e:
    # エラー内容を表示
    print(f"データの処理中に予期せぬエラーが発生しました: {e}")