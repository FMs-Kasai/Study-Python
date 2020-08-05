import re

word = "アークデーモン"
word2 = "ウドラー"

re_katakana_notyoon = re.compile(r"[\u30A1-\u30F4]+") #長音含まない
status_kata = re_katakana_notyoon.fullmatch(word)

re_katakana_oktyoon = re.compile(r"[\u30A1-\u30FC]+") #長音含む
status_kata_tyoon = re_katakana_oktyoon.fullmatch(word)

re_teil_tyoon = re.compile(r".*[\u30FC]$")
status_teil_tyoon = re_teil_tyoon.fullmatch(word2)

if status_kata:
    print("ok")
else:
    print("no")

if status_kata_tyoon:
    print("ok")
else:
    print("no")

if status_teil_tyoon:
    print("ok-tyoon")
else:
    print("no-tyoon")