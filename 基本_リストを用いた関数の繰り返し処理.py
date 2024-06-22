def keisan(value_1, value_2):
    """足し算と掛け算の関数"""
    tashizan = value_1 + value_2
    kakezan = value_1 * value_2

    return tashizan, kakezan


data_x_list = [1, 3, 5]

print("変数と結果")
for x in data_x_list:
    # 引数に変数を用い、結果を変数に入れる
    y = 40
    # 結果の取得と表示
    result_tashizan_4, result_kakean_4 = keisan(x, y)  # 結果を変数に代入
    print("x=", x, "y=", y, "足し算：", result_tashizan_4, "掛け算：", result_kakean_4)

data_x_list = [1, 3, 5]
data_y_list = [10, 20, 30]

print("変数と結果")
for x, y in zip(data_x_list, data_y_list):
    # 結果の取得と表示
    result_tashizan_5, result_kakezan_5 = keisan(x, y)  # 結果を変数に代入
    print("x=", x, "y=", y, "足し算：", result_tashizan_5, "掛け算：", result_kakezan_5)
