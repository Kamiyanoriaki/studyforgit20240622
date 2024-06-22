import os
import glob

# すべてのファイルのファイル名の取得
file_list_all = glob.glob("作業用/*")
print(file_list_all)

# 拡張子(pptx)のファイルのファイル名の取得
file_list_pptx = glob.glob("作業用/*.pptx")
print(file_list_pptx)

# 拡張子(pptx)のファイルのファイルパスの取得
folder_path = os.path.dirname(__file__)
target_path = folder_path + os.sep + "作業用/*.pptx"
path_list = glob.glob(target_path)
print(folder_path)

for i in path_list:
    print(i)
