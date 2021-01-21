import pandas as pd
import random
import numpy as np

#目標：ランダムな問題集ファイルを作成する

# データ整形
def make_capitals() -> list:
    capitals_df = pd.read_excel("todouhuken.xlsx", sheet_name = 0)
    capitals_df = capitals_df[["都道府県 県あり", "県庁所在地 市区町村あり"]]

    capitals = capitals_df.values.tolist()


    return capitals

def make_prefecture(capitals: list) -> list:
    prefecture = []
    prefecture_count = 0

    for prefecture_count in range (len(capitals)):
        prefecture.append(capitals[prefecture_count][0])

    return prefecture

# 問題集,回答集ファイルを作成
def make_workbook(quiz_num: int) -> None:
    for quiz_num in range(5):
        quiz_file = open('capitalquiz{}.txt'
                         .format(quiz_num), 'w')

        answer_key_file = open('capitalquiz_answers{}.txt'
                               .format(quiz_num), 'w')

        quiz_file.write('名前：\n\n日付：\n\n学籍番号：')
        quiz_file.write(('' * 20) + '都道府県庁所在地クイズ(問題番号{})'
                        .format(quiz_num))
        quiz_file.write('\n\n')


# 問題集と回答のファイルを作成

# 都道府県(prefecture)の順番シャッフル
def shuffle_prefecture(prefecture: list) -> list:
    random.shuffle(prefecture)
    return prefecture


# 47都道府県をループ、それぞれ問題を作成

# メイン
def make_prefecture_quiz() -> None:
    capitals = make_capitals()
    prefecture = make_prefecture(capitals)
    quiz_num = 1
    # shuffle_prefecture(prefecture)
    print(prefecture)

make_prefecture_quiz()

