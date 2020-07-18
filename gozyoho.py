def caluculat_gcd(num1,num2):
    a = num1
    b = num2

    while a % b != 0:
        c = a % b
        a = b
        b = c

    result = b
    return  result

print("ユークリッド互除法のプログラム")
num1 = int(input("Num1:"))
num2 = int(input("Num2:"))

result = caluculat_gcd(num1,num2)
print("最大公約数は{}です".format(result))

