list01 = ["サリンジャー","オーウェル","スウィフト",""]

print(list01)
print(list01[0])
print(list01[1])
print(list01[2])

list01[3] = "ディック"
print(list01[3])

# list01[4] = "kasai" 添え字エラー　配列のレンジを超えた挿入はできない
# print(list01[4])

#リストの中にリストを挿入できる！
list02 = [["kasai","sato"],["ubayama","sakuma"]]

print(list02[0][0])
print(list02[0][1])
print(list02[1][0])
print(list02[1][1])