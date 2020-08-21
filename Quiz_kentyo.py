import pandas as pd
import random


# データ整形
def make_prefecture() -> list:
    prefecture_df = pd.read_excel("todouhuken.xlsx", sheet_name = 0)
    prefecture_df = prefecture_df[["都道府県 県あり", "県庁所在地 市区町村あり"]]

    prefecture = prefecture_df.values.tolist()


    return prefecture

# 整形されたデータから問題出す
def choice_prefecture(prefecture: list) -> str:
    prefecture_num = random.randint(0, 46)

    return prefecture[prefecture_num][0]
# 正解か判定
# ユーザの入力処理。
# 結果をファイル出力
# 出した都道府県覚えておく
# 出した都道府県消す。
prefecture = make_prefecture()
print(choice_prefecture(prefecture))

