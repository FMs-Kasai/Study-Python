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
def judge_answer(prefecture: list, question: str, answer:str) -> bool:
    question_index = prefecture.index(question)

    if prefecture[question_index][0] == answer:
        return True
    else:
        return False

# ユーザの入力処理。
def user_input_answer() -> str:
    print("県庁所在地を入力してください")

    answer = str(input())

    if len(answer) <= 10:
        return answer
    else:
        print("県庁所在地は10文字以内で入力してください")
        return user_input_answer()

# 結果をファイル出力
# 出した都道府県覚えておく
# 出した都道府県消す。
# 都道府県クイズ処理（メインプログラム）
def prefecture_quiz() -> None:
    prefecture = make_prefecture()
    for question_count in range(1, 47):
        question = choice_prefecture(prefecture)

        print("問題{}:{}"
              .format(question_count, question)
              )

        answer = user_input_answer()
        if judge_answer(prefecture, question, answer):
            print("正解！")
        else:
            print("不正解")

    return None

prefecture = make_prefecture()
print(prefecture)

