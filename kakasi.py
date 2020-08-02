from pykakasi import kakasi

text = u"暗黒神ラプソーン"
dict = {"red":red, "blue":blue, "yellow":yellow}

word = dict[red]

kakasi = kakasi()

kakasi.setMode("J", "K")
kakasi.setMode("H", "K")

conv = kakasi.getConverter()
result = conv.do(text)
result2 = conv.do(word)

print(result)
print(result2)