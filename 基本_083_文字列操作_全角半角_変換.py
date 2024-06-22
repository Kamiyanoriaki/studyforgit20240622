import zenhan

# 全角から半角へ ========
print("全角から半角へ")
test_text_1 = "TEST123アイウエオガギグゲゴ　カード：＊／＜＞？￥"
print("元データ", test_text_1)
hankaku_test_1_0 = zenhan.z2h(test_text_1)
print(hankaku_test_1_0, "　　　指定なし、すべて変換")

# 半角から全角へ ========
print("半角から全角へ")
test_text_2 = "TEST123ｱｲｳｴｵｶﾞｷﾞｸﾞｹﾞｺﾞ ｶｰﾄﾞ:*/<>?¥¥"
print("元データ", test_text_2)
zenkakutest_text_2_0 = zenhan.h2z(test_text_2)
print(zenkakutest_text_2_0, "　　　指定なし、すべて変換")
