list01 = ["サリンジャー","オーウェル","スウィフト",""]
list1_1 = ["村上春樹","夏目漱石","東野圭吾"]

print(list01)
print(list01[0])
print(list01[1])
print(list01[2])

list01[3] = "ディック"
print(list01[3])
print(list01[0:-1]) #スライスの記述はコロンで区切る。第一引数が開始インデックスで第二が終了インデックス。（第二引数自体は含まれず一つ小さい要素が出力される
print(list01[0:]) #第一引数または第二引数省略可能
print(list01[:2])
print(list01[-1]) #負のインデックスは末尾から
print(list01 + list1_1) #連結も可能

del list1_1[1] #リストのデータを消去する。空いた分は詰める。
print(list1_1[1])
print(list1_1)

# list01[4] = "kasai" 添え字エラー　配列のレンジを超えた挿入はできない
# print(list01[4])

#リストの中にリストを挿入できる！
list02 = [["kasai","sato"],["ubayama","sakuma"]]

print(list02[0][0])
print(list02[0][1])
print(list02[1][0])
print(list02[1][1])