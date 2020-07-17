import math

def summer_wars(num1,num2,num3):
    month_taiouhyo = [1,4,4,0,2,5,0,3,6,1,4,6]
    youbihyo = ["土","日","月","火","水","木","金"]

    if num1 - 2000 >= 0:
        a = num1 - 2000
        b = math.floor((num1 - 2000) / 4)
        e = 6
    elif num1 - 1900 >= 0:
        a = num1 -1900
        b = math.floor((num1 - 1900) / 4)
        e = 0
    else:
        print("お前はもう死んでいる!!")
        exit()

    c = num3
    d = month_taiouhyo[num2 - 1]

    mod = (a + b + c + d + e) % 7
    youbi = youbihyo[mod]

    return youbi


print("先輩って誕生日いつですか？")
year = int(input("Year:"))
month = int(input("Month:"))
day = int(input("Day:"))

youbi = summer_wars(year,month,day)

print(youbi + "曜日ですね！")
print('{}年{}月{}日は{}曜日でした！合ってましたか？？？'.format(year,month,day,youbi))

