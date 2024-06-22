import unicodedata

text_1 = "ｽｽﾞｷ123 ①②③　ＡＢＣ"
text_2 = unicodedata.normalize("NFKC", text_1)
print(text_2)
