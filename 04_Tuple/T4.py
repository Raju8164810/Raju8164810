# unpacking
a, b, c, d, e = 10, 20, 30, 40, 50
# print(a, b, c)  # ValueError: too many values to unpack (expected 3)
print((a, b, c, d, e))  # (10, 20, 30, 40, 50)

a, *b, c = 10, 20, 30, 40, 50
print(a, b, c) # 10 [20, 30, 40] 50


*a, b, c = 10, 20, 30, 40, 50, 60, 70, 80
print(a, b, c)  # [10, 20, 30, 40, 50, 60] 70 80

a, b, c, d, e = 10, 20, 30
print(a, b, c, d, e) # ValueError: not enough values to unpack (expected 5, got 3)





