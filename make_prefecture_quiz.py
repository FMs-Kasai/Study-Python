import pandas as pd
import random
import numpy as np

#目標：ランダムな問題集ファイルを作成する

#[[都道府県][県庁所在地]]のようにデータ整形
def make_capitals() -> list:
    capitals_df = pd.read_excel("todouhuken.xlsx", sheet_name = 0)
    capitals_df = capitals_df[["都道府県 県あり", "県庁所在地 市区町村あり"]]

    capitals = capitals_df.values.tolist()


    return capitals

#配列シャッフル
def shuffle_capitals(capitals: list) -> list:
    return np.random.shuffle(capitals)

def make_answer_options(capitals: list) -> list:
    answer_options = []

    for i in range(5):
        answer_options.append(capitals[i][0])

    random.shuffle(answer_options)

    return answer_options

# 問題ファイルを作成
def make_workbook(quiz_num: int, question_num: int, capitals: list) -> None:

    quiz_file = open('capitalquiz{}.txt'
                     .format(quiz_num), 'w')

    answer_key_file = open('capitalquiz_answers{}.txt'
                           .format(quiz_num), 'w')

    quiz_file.write('名前：\n\n日付：\n\n学籍番号：')
    quiz_file.write(('' * 20) + '都道府県庁所在地クイズ(問題番号{})'
                    .format(quiz_num))
    quiz_file.write('\n\n')

    for question_num in range(5):
        quiz_file.write('{}. {}の県庁所在地は？\n'
                    .format(question_num + 1, capitals[question_num][0]))

        for choice_count in range(4):
            #ここが変　quiz_file.write('{}. {}\n'.format('ABCD'[choice_count], capitals[choice_count + 5][1]))

#解答ファイルを作成

# メイン
def make_prefecture_quiz() -> None:
    for quiz_num in range(5):
        capitals = make_capitals()
        shuffle_capitals(capitals)
        answer_options = make_answer_options(capitals)

        print(answer_options)

make_prefecture_quiz()

