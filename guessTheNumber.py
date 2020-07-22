import random

def input_number():
    num1 = input("1から20までの整数を入力してください:")
    try:
        num1 = int(num1)
    except:
        print("整数で入力してください")
        return input_number()

    if num1 > 0 and num1 <= 20:
        return num1
    else:
        print("エラー：0以上20未満で入力してください")
        return input_number()

def judge_number(a,b):
    for i in range(1,6):
        if a == b:
            return print("正解です！{}回で当たりました".format(i))
        elif a > b:
            print("もっと大きいです")
            b = input_number()
        else:
            print("もっと小さいです")
            b = input_number()

    return print("ドンマイ！正解は{}でした！".format(a))


answer = random.randint(1,20)
judge_number(answer,input_number())