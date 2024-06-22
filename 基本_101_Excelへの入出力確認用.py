import win32com.client as com
import os

# サンプルプログラム基準のエクセルファイルパスを定義しています。
# プログラムファイルのディレクトリパス(folder_path)の取得
folder_path = os.path.dirname(__file__)
# エクセルファイルのパス
excel_file_path = folder_path + os.sep + "Excel_アプリの入出力確認用.xlsx"

app = com.Dispatch("Excel.Application")
app.Visible = True
app.DisplayAlerts = False

wb = app.Workbooks.Open(excel_file_path)
# wb = app.Workbooks.Open("C:\Users\kamiy\OneDrive\ドキュメント\MyPython\Automation\Excel_Test_01.xlsx")

sheet = wb.Worksheets("Sheet1")

# 固定セルに固定値で入力（A1形式）
sheet.Range("B3").Value = 1
sheet.Range("B4").Value = 0.01
sheet.Range("B5").Value = "固定セルに固定値で入力（A1形式）"

# 固定セルに固定値で入力（R1C1形式）
sheet.Cells(7, 2).Value = 2
sheet.Cells(8, 2).Value = 0.02
sheet.Cells(9, 2).Value = "固定セルに固定値で入力（R1C1形式）"

# 変数を用いて入力
int_01 = 3
float_01 = 0.03
str_01 = "セルも値も変数を用いて入力"

y1 = 11
y2 = 12
y3 = 13
x1 = 2

sheet.Cells(y1, x1).Value = int_01
sheet.Cells(y2, x1).Value = float_01
sheet.Cells(y3, x1).Value = str_01

# Excelから値を取得し、Pythonのターミナル画面に表示
int_02 = sheet.Cells(17, 2).Value
float_02 = sheet.Cells(18, 2).Value
str_02 = sheet.Cells(19, 2).Value

print(int_02)
print(float_02)
print(str_02)

print(type(int_02))
print(type(float_02))
print(type(str_02))
