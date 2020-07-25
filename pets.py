def input_pets_name():
    pets_name = input("ペットの名前を入力してください(10文字以内)\n終了はEnter:")

    if len(pets_name) < 10:
        return pets_name
    else:
        print("ペットの名前は10文字以内です")
        return input_pets_name()

def generate_pets_array():
    pets_array = []
    while True:
        pets_name = input_pets_name()
        if pets_name == "":
            break

        # pets_array = pets_array + [pets_name]
        pets_array.append(pets_name) #リストの末尾に追加

    print("入力されたペットの名前は以下の通り")
    for pets_name in pets_array:
        print(pets_name)

    print("配列の中身は以下")
    print(pets_array)

    return pets_array

def search_pets(pets_array):
    print("検索したいペットの名前を入力してください")
    search_pets_name = input()
    if search_pets_name not in pets_array:
        print(search_pets_name + "という名前のペットは飼っていません")
        return search_pets(pets_array)
    else:
        i = pets_array.index(search_pets_name)
        print(search_pets_name + "は私のペットです。リスト番号{}".format(i))
        return search_pets(pets_array)

pets_array = generate_pets_array()
search_pets(pets_array)