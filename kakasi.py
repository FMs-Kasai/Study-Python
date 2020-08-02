from pykakasi import kakasi

text = u"暗黒神ラプソーン"

kakasi = kakasi()

kakasi.setMode("J", "K")
kakasi.setMode("H", "K")

conv = kakasi.getConverter()
result = conv.do(text)

print(result)