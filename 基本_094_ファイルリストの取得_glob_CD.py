import os
import glob

os.chdir("作業用")
print(os.getcwd())

# すべてのファイルのファイル名の取得
file_list_all = glob.glob("*")
print(file_list_all)

# 拡張子(pptx)のファイルのファイル名の取得
file_list_pptx = glob.glob("*.pptx")
print(file_list_pptx)

os.chdir("..")
print(os.getcwd())