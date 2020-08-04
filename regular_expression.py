import re

word = "アークデーモン"
re_katakana = re.compile(r'[\u30A1-\u30F4]+')
status_kata = re_katakana.fullmatch(word)

if status_kata:
    print("ok")
else:
    print("no")