d1 = {'a':10, 'b':  20, 'c': 30, 'd': 40}
print(d1.pop('c'))
print(d1)

del d1['a']
print(d1)

d2 = {'a':10, 'b':  20, 'c': 30, 'd': 40}
d2['x'] = d2.pop('a')
print(d2)