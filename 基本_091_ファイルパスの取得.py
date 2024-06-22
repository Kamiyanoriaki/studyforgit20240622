from pathlib import Path
import os

# いかにサンプルプログラム基準のExcelファイルパスを定義する。
# プログラムファイルのディレクトリパス(folder_path)の取得
folder_path = os.path.dirname(__file__)
print("プログラムファイルのディレクトリパス：", folder_path)

# エクセルファイルのパス
excel_file_path_B = folder_path + os.sep + "フォルダB" + os.sep + "Test_2.xlsx"
print("エクセルファイルのパス：", excel_file_path_B)

excel_file_path_B_2 = os.path.join(folder_path, "フォルダB", "Test_2.xlsx")
print("エクセルファイルのパス：", excel_file_path_B_2)

excel_file_path_B_3 = Path(folder_path, "フォルダB", "Test_2.xlsx")
print("エクセルファイルのパス：", excel_file_path_B_3)
