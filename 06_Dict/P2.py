d1 = {1:10, 2:20, 3:30, 4:40, 5:50}
print(d1)  # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50}
print(d1.keys())  # dict_keys([1, 2, 3, 4, 5])
print(d1.values())  # dict_values([10, 20, 30, 40, 50])
print(d1.items()) # dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50)])


d2 = {1:10, 2:20, 3:30, 4:40, 5:50}

del d2[1]
print(d2)  # {2: 20, 3: 30, 4: 40, 5: 50}

d3 = {'pizza': 5, 'quantity': 10}
print(d3)  #  {'pizza': 5, 'quantity': 10}
print(d3['quantity']+1)
print(d3)

d3['quantity'] = 20
print(d3)
print(d3)