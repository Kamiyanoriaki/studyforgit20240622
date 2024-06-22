x = "A"
y = 1
print("xの変数型は、", type(x))
print("yの変数型は、", type(y))

y2 = str(y)
print("y2の変数型は、", type(y2))

z = x + y2
print(z)

y3 = int(y2)    #整数型に戻す

z = x + y3
print(z)
