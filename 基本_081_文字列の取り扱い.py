# 文字列の和
x01 = "フォルダ名" + "_20230611"
print(x01)

x02 = "TEST" + "_20230611" + ".xlsx"
print(x02)

# 文字のスライス
str_11 = "一二三四五六七八九〇"  # 元の文字列

print(str_11[0:10])  # 1文字から10文字目
print(str_11[0:3])  # 1文字から3文字目
print(str_11[:3])  # 1文字から3文字目
print(str_11[4:10])  # 5文字から10文字目
print(str_11[4:])  # 5文字から10文字目
print(str_11[4:6])  # 5文字から6文字目
print(str_11[:-4])  # 後ろから5文字目まで

# 文字列の置換
# ＜列：台所をキッチンに変更＞
str03 = "僕は台所にいます。"
str03_2 = str03.replace("台所", "キッチン")
print(str03_2)

# 03-XXXX-YYYY　を　03XXXXYYYYに変更
str04 = "03-XXXX-YYYY"
str04_2 = str04.replace("-", "")
print(str04_2)

# 151-ZZZZ　を　151ZZZZに変更
str05 = "151-ZZZZ"
str05_2 = str05.replace("-", "")
print(str05_2)

# 32(数値)を0埋めして0032に変更

value_01 = 32
str_01 = str(value_01)
zfill_no = str_01.zfill(5)
print(zfill_no)

# 文字列の分解
# 2023-06-11 から リスト[2023,06,11]を作成
str03 = "2023-06-11"

str_list = str03.split("-")
print(str_list)

# 括弧で囲まれた文字列の取り出し

str06 = "RE:RE:[ご案内-005]新商品について"
print(str06)
str07 = str06.replace("[", "■")
print(str07)
str08 = str07.replace("]", "■")
print(str08)
str_list2 = str08.split("■")
print(str_list2)
print(str_list2[1])

# ファイル名に日付をつける
original_file = "月報フォーマット.xlsx"
print(original_file)
print(original_file[:-5])
new_file = original_file[:-5] + "_202306" + ".xlsx"
print(new_file)

# 大文字に変換する
str_21 = "python"
str_22 = str_21.upper()
print(str_22)

# 小文字に変換する
str_23 = "PYTHON"
str_24 = str_23.lower()
print(str_24)

# 先頭のみを大文字にする
str_15 = "japanease"
str_16 = str_15.capitalize()
print(str_16)
