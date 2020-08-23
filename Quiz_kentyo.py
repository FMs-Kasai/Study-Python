import pandas as pd
import random


# データ整形
def make_prefecture() -> list:
    prefecture_df = pd.read_excel("todouhuken.xlsx", sheet_name = 0)
    prefecture_df = prefecture_df[["都道府県 県あり", "県庁所在地 市区町村あり"]]

    prefecture = prefecture_df.values.tolist()


    return prefecture

# 整形されたデータから問題出す
def choice_prefecture(prefecture: list, past_prefecture: list) -> str and int:
    prefecture_num = random.randint(0,46)

    if prefecture[prefecture_num][0] in past_prefecture:
        return choice_prefecture(prefecture, past_prefecture)
    else:
        return prefecture[prefecture_num][0], prefecture_num


# 正解か判定
def judge_answer(prefecture_num: int, answer:str, prefecture: list) -> bool:

    if prefecture[prefecture_num][1] == answer:
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
def write_result_file(incorrect_prefecture: list) -> None:

# 都道府県クイズ処理（メインプログラム）
def prefecture_quiz() -> None:
    prefecture = make_prefecture()
    past_prefecture = []
    incorrect_prefecture = []
    incorrect_answer_count = 0
    for question_count in range(1, 47):
        question, prefecture_num = choice_prefecture(prefecture, past_prefecture)
        past_prefecture.append(question)

        print("問題{}:{}"
              .format(question_count, question)
              )

        answer = user_input_answer()

        if judge_answer(prefecture_num, answer, prefecture):
            print("正解！")
        else:
            print("不正解")
            incorrect_prefecture.append(question)
            incorrect_answer_count += 1

        if incorrect_answer_count == 3:

            print(
                "3回間違えたので終了します。結果はresult.txtに出力しました。\n"
                  "お疲れさまでした."
            )
            return None

    return None

prefecture_quiz()

