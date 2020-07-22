def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("不正な引数です")

num1 = int(input("num1:"))
num2 = int(input("num2:"))
print(division(num1,num2))
