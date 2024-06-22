import unicodedata
import sys

# getdefaultencoding() 文字コードを確認
print("VSCodeの文字コードを確認：", sys.getdefaultencoding())

text_nbsp = ""
text_nbsp_normalize = unicodedata.normalize("NFKC", text_nbsp)

print(text_nbsp, "←変換前の文字")
print(text_nbsp_normalize, "←変換後の文字")

print(text_nbsp.encode("utf-8"), "←返還前の文字コード")

if text_nbsp == text_nbsp_normalize:
    print(text_nbsp, "と", text_nbsp_normalize, "は同じです。")
else:
    print(text_nbsp, "と", text_nbsp_normalize, "は違います。")

text_space = ""
if text_nbsp_normalize == text_space:
    print("正規化出来てスペースに変換しました。")
else:
    print("スペースではありません。")
