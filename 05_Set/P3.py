# add()
s1 = set()
print(s1, type(s1))  # set() <class 'set'>

s1.add(10)
s1.add(20)
s1.add(30)
s1.add(40)

print(s1, type(s1))  # {40, 10, 20, 30} <class 'set'>

# AttributeError: 'dict' object has no attribute 'add'

print("pop method")
s2 = {10, 20, 30, 40, 50}
print(s2)
s2.pop()  # {50, 20, 40, 10, 30}
print(s2)  # {20, 40, 10, 30}

s2.pop()  # {20, 40, 10, 30}
print(s2) # {40, 10, 30}

s2.pop()  # {40, 10, 30}
print(s2) # {10, 30}

s2.pop()  # {10, 30}
print(s2) # {30}

s2.pop()
print(s2) # set()

# s2.pop()
# print(s2)  # KeyError: 'pop from an empty set'

s1 = {10, 20}
s2 = {20, 30}
s1.update(s2)
print(s1)

# s1 = {10, 20}
# s2 = {20, 30}
# s1.add(s2)
# print(s1)  # TypeError: unhashable type: 'set'

# no index call, no slicing, no concat, no repetition 

