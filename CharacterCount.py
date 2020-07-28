import pprint

def charecter_count():
    print("文章を入力してください:")
    message = input()
    for character in message:
        count.setdefault(character,0)
        count[character] = count[character] + 1

    print(count)
    pprint.pprint(count) #整形表示できる

count = {}
charecter_count()