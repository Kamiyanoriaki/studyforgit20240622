def keisan(value_1, value_2):
    """足し算と掛け算の関数"""
    tashizan = value_1 + value_2
    kakezan = value_1 * value_2

    return tashizan, kakezan


# 結果の表示
print(keisan(2, 10))  # ダブルとして得られる
print(keisan(value_1=2, value_2=10))  # キーワード付き引数
print(type(keisan(2, 10)))  # ダブルを確認
print(keisan(2, 10)[0])  # ダブルをスライスして表示
print(keisan(2, 10)[1])  # ダブルをスライスして表示

# 結果の表示と変数への取得
result_tashizan_1, result_kakezan_1 = keisan(2, 10)  # 結果の変数への代入
print(result_tashizan_1, result_kakezan_1)  # 変数の値の表示

result = keisan(3, 20)

# 関数の結果のタプルからの取り出し
print(result)  # ダブルとして得られる
print(type(result))  # ダブルを確認
print(result[0])  # ダブルをスライスして表示
print(result[1])  # ダブルをスライスして表示

# 結果の表示と変数への取得
result_tashizan_2, result_kakezan_2 = result  # 結果の変数への代入
print(result_tashizan_2, result_kakezan_2)  # 変数の値の表示

# 引数に変数を用い、結果を変数に入れる
x = 4
y = 40

# 結果の表示と変数への取得
result_tashizan_3, result_kakezan_3 = keisan(x, y)  # 結果の変数への代入
print(result_tashizan_3, result_kakezan_3)  # 変数の値の表示
