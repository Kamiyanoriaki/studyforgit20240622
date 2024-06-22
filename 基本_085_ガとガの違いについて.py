import unicodedata

original_text = "ｶﾞ"

text_one_code = unicodedata.normalize("NFKC", original_text)
text_two_code = unicodedata.normalize("NFKD", original_text)

print(text_one_code)
print(text_two_code)

if text_one_code == text_two_code:
    print(text_one_code, "と", text_two_code, "は同じです。")

else:
    print(text_one_code, "と", text_two_code, "は違います。")

encode_text_one_code = text_one_code.encode("utf-8")
encode_text_two_code = text_two_code.encode("utf-8")

print(encode_text_one_code)
print(encode_text_two_code)

f = open("ガの比較.csv", "w", encoding="utf-8")
f.write(text_one_code)
f.write(text_two_code)
f.close()
