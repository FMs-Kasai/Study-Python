def input_num():
    num = input("整数を入力してください:")
    try:
        num = int(num)
    except:
        print("整数で入力してください")
        return input_num()

    return num

def collatz(a):
    if a == 1:
        return print(a)
    elif a % 2 == 0:
        print(a)
        a = a // 2
        return collatz(a)
    else:
        print(a)
        a = (a * 3) + 1
        return collatz(a)

num = input_num()
collatz(num)