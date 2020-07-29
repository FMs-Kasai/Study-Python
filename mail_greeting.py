#! python3

import sys
import pyperclip

greeting = {"greeting1": "初めてメールを送らせていただきます。「」の「」と申します",
            "greeting2": "突然のご連絡失礼いたします。「」の「」と申します",
            "greeting3": "お世話になっております。「」の「」と申します"}

if len(sys.argv) < 2:
    print("使い方：mail_greeting.py [greeting1or2or3]")
    print("定型文をクリップボードにコピーしました")
    sys.exit()

message = sys.argv[1]

if message in greeting:
    pyperclip.copy(greeting[message])
    print("定型文をクリップボードにコピーしました")
else:
    print("指定した定型文は存在しません。")

