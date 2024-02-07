# count() returns the number of same occurrence
l1 = [10, 20, 30, 40, 50, 60, 70, 10, 20, 10, 40]
print(l1.count(10))  # 3
print(l1.count(40))  # 2

# clear() method removes all the elements
l2 = [10, 20, 30, 40, 50, 60, 70, 10, 20, 10, 40]
l2.clear()
print(l2)

# copy() returns a shallow copy

l3 = [10, 20, 30, 40, 50, 60, 70, 10, 20, 10, 40]
print(l3)  # [10, 20, 30, 40, 50, 60, 70, 10, 20, 10, 40]
print(l3.copy())  # [10, 20, 30, 40, 50, 60, 70, 10, 20, 10, 40]



