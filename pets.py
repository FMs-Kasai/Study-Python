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

        pets_array = pets_array + [pets_name]

    print("入力されたペットの名前は以下の通り")
    for pets_name in pets_array:
        print(pets_name)

    print("配列の中身は以下")
    print(pets_array)

generate_pets_array()
