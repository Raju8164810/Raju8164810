d1 = {}
print(d1, type(d1))  # {} <class 'dict'>

l1 = [10, 20, 30, 40, 50]
#      0   1   2   3   4
print(l1[0]) # 10
print(l1[3]) # 40


d2 = {}
d2[0] = 10
d2[1] = 20
d2['name'] = "Sai Kiran"
print(d2)  # {0: 10, 1: 20, 'name': 'Sai Kiran'}

d3 = {0: 10, 1: 20, 'name': 'Sai Kiran'}
print(d3[0], d3[1], d3['name'])  # 10 20 Sai Kiran

l1 = [10, 20, 40, 50]
#     0    1   2   3   4
print(len(l1)) # 4
# l1[4] = 60
# print(l1)  # IndexError: list assignment index out of range

d1 = {'a':10, 'b' : 20, 'c': 40, 'd': 50}
print(d1['a'], d1['b'], d1['c'],d1['d'])

d1["e"] = 60
print(d1)


