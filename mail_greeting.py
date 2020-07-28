#! python3

import sys
import pyperclip

greeting = {"greeting": "初めてメールを送らせていただきます。「」の「」と申します",
            "greeting2": "突然のご連絡しつれいいたします。「」の「」と申します",
            "greeting3": "お世話になっております。「」の「」と申します"}

message = sys.argv[1]

if message in greeting:
    pyperclip.copy(greeting[message])
    print("定型文をクリップボードにコピーしました")
else:
    print("指定した定型文は存在しません。")

