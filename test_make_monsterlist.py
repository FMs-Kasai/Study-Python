import csv

def make_monster_dict():
    monster_dict = {}
    csv_header = ["no","name","area","drop_item"]

    with open("dq8_monster.csv", "r", encoding="utf-8_sig") as file:
        for row in csv.DictReader(file,csv_header):
            print(row["name"])


make_monster_dict()

kana = "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほ" \
       "まみむめもやゆよらりるれろわゐゑをんがぎぐげござじずぜぞだぢづで" \
       "どばびぶべぼぱぴぷぺぽ"

