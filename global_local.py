def addition():
    a = 0  #addition関数内のローカル変数
    b = 1
    subtraction()
    print(a)

def subtraction():
    a = 3  #subtraction関数内のローカル変数
    b = 4
    a = b - a
    print(c)

c = 5 #グローバル変数。関数内で参照可能
addition()  #ローカル変数は名前が同じでも区別されるため　a = 0
subtraction()
