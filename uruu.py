def judge_uruu(num1):

    if num1 % 400 == 0 or num1 % 4 == 0:
        result = "閏年です"

    elif num1 % 100 == 0:
        result = "閏年ではありません"

    else:
        result = "閏年ではありません"

    return  result

print("西暦を入力してください:")
num1 = int(input("Year:"))

result = judge_uruu(num1)

print(result)
