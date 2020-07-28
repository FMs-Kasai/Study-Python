def input_name():
    name = input("名前を入力してください\n終了するにはエンター：")

    if name == "":
        return exit

    if len(name) > 15:
        print("名前は15文字以内で入力してください")
        return input_name()
    else:
        return name

def input_birthday():
    print("誕生日を入力してください\n例：19980721:")
    birthday = input()
    try:
        birthday = int(birthday)
    except:
        print("数字で入力してください")
        return input_birthday()

    return birthday

def generate_birthdays_array():
    name = input_name()
    birthday = input_birthday()

    birthdays_array[name] = birthday
    print("登録を完了しました。")
    ans = input_ans()
    if ans == "y":
        return generate_birthdays_array()
    else:
        return birthdays_array,show_birthdays_array()

def input_ans():
    print("続けて登録しますか？y/n")
    ans = input()
    if ans == "y" or ans == "n":
        return ans
    else:
        print("yかnで入力してください")
    return input_ans()

def show_birthdays_array():
    print("作成された誕生日表は下記の通りです。")
    for k,v in birthdays_array.items():
        print("名前:" + k + "誕生日:" + str(v))
    print(birthdays_array)

birthdays_array = {} #{}で辞書型を定義[]はリスト。
generate_birthdays_array()