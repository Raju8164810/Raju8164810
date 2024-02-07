# index(element)
# index(element, start, end)
t1 = (10, 20, 30, 40, 50, 60, 10, 80, 90, 100, 10)
#      0   1   2   3  4   5    6   7   8   9   10

print(t1.index(10)) # 0
print(t1.index(40)) # 3
print(t1.index(10,5,7)) # 6
print(t1.index(10,9,11)) # 10

print(t1[11:22])  # ()
print(t1[2:])  # (30, 40, 50, 60, 10, 80, 90, 100, 10)

