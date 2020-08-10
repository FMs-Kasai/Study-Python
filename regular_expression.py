import re
# .*は貪欲マッチ（マッチする文字列が複数あった場合一番長い文字列を選択する）
# .?は非貪欲マッチ（上記の逆）

def phonenumber_regex(phonenumber: str) -> bool:
    pattern = re.compile(r"(\d\d\d-\d\d\d-\d\d\d\d)")

    if pattern.fullmatch(phonenumber):
        return True
    else:
        return False

def password_check(password: str) -> bool:
    pattern = re.compile(r"[a-zA-Z0-9]{8,20}")

    if pattern.fullmatch(password):
        return True
    else:
        return False

print("電話番号を入力してください")
phonenumber = input()
print(phonenumber_regex(phonenumber))
password = input()
print(password_check(password))

"""
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
"""