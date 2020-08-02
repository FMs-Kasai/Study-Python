from pykakasi import kakasi
import re

text = u"暗黒神ラプソーン"
dict = {'アークデーモン': 'アークデーモン', 'アークバッファロー': 'アークレートジンガー', '暗黒神ラプソーン': '暗黒神ラプソーン','クローハンズ': 'クローハンズ'}
dict2 = {}
kakasi = kakasi()
kakasi.setMode("J", "K")
kakasi.setMode("H", "K")
conv = kakasi.getConverter()

re_hiragana = re.compile(r'^[あ-ん]+$')
re_kanji = re.compile(r'^[\u4E00-\u9FD0]+$')

for i in dict:
    dictword = i
    status_hira = re_hiragana.fullmatch(dictword)
    status_kanji = re_kanji.fullmatch(dictword)

    if status_hira == True or status_kanji == True:
        word = conv.do(i)
        dict2.setdefault("word",word)



result = conv.do(text)
#result2 = conv.do(word)

#print(result)
#print(result2)
print(dict2)