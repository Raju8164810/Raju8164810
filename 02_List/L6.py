# # pop()
# # pop() methods deleted the element from the end of the list
# l1 = [10, 20, 30, 40, 50, "NameOne", "NameTwo", "NameThree"]
# print(l1.pop())  # NameThree
# print(l1)  # [10, 20, 30, 40, 50, 'NameOne', 'NameTwo']

# # pop(index)
# l2 = [10, 20, 30, 40, 50, "NameOne", "NameTwo", "NameThree"]
# #      0   1   2   3   4     5           6          7
# print(l2.pop(4))  # 50
# print(l2)  # [10, 20, 30, 40, 'NameOne', 'NameTwo', 'NameThree']

# # index(element)
# # index(element) method finds the index position
# l3 = [10, 20, 30, 40, 50, "NameOne", "NameTwo", "NameThree"]
# #      0   1   2   3   4     5           6          7
# print(l3.index(40)) # 3
# print(l3.index(20)) # 1

# # remove(element)
# # remove(element) method removes the given element
# l4 = [10, 20, 30, 40, 50, "NameOne", "NameTwo", "NameThree"]
# l4.remove(10)
# print(l4)  # [20, 30, 40, 50, 'NameOne', 'NameTwo', 'NameThree']

l5 = [30,40,50,"name0ne","NameTwo"]
print(l5.pop())
print(l5)
print(l5.index(50))
print(l5.index("name0ne"))
l5.remove(40)
print(l5)