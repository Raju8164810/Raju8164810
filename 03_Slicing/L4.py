# remove(element/item), pop(index), pop(), del 

l1 = [10, 20, 30, 40, 50]

l1.remove(40)
print(l1)

l1 = [10, 20, 30, 40, 50]
l1.pop(3)
print(l1)

l1 = [10, 20, 30, 40, 50]
del l1[3]
print(l1)

l1 = [10, 20, 30, 40, 50]
del l1[3]

l1 = [10, 20, 30, 40, 50]
#      0   1   2   3  4

# del l1[0:5]
# print(l1[0:4])
l1  = l1[:3] + l1[4:]
print(l1)