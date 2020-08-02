import csv
import re
from pykakasi import kakasi


def left(s, amount):
    return s[:amount]

def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

def make_monstername_dict():
    monster_dict = {}
    csv_header = ["no","name","area","drop_item"]

    with open("dq8_monster.csv", "r", encoding="utf-8_sig") as file:
        for key in csv.DictReader(file,csv_header):
            if not key["name"] in monster_dict.keys():
                monster_dict[key["name"]] = key["name"]

        return monster_dict

def make_kana_dict():
    kana_list = {}
    for i in range(0,len(KATAKANA) + 1):
        kanas = []
        j = 1
        for key in MONSTER_NAME_DICT:
            if left(MONSTER_NAME_DICT[key],1) == mid(KATAKANA,i,1):
                kanas.append(MONSTER_NAME_DICT[key])
                j = j + 1
        kana_list[mid(KATAKANA,i,1)] = kanas

    return kana_list


MONSTER_NAME_DICT = make_monstername_dict()
KATAKANA = "アイウエオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂツヅテデ" \
           "トドナニヌネノハバパヒビピフブプヘベペホボポマミムメモヤユヨ" \
           "ラリルレロワヲンヴ"

kanalist = make_kana_dict()
print(kanalist)


