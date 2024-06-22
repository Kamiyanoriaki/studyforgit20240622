import os

# 以下にプログラム基準の作業用フォルダのパスを定義する。
folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

# 作業用フォルダのパス
working_folder_path = folder_path + os.sep + "作業用"
print("作業用フォルダのパス：", working_folder_path)

file_list = os.listdir(working_folder_path)
print(file_list)

for file_name in os.listdir(working_folder_path):
    print(file_name)
