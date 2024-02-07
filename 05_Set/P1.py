# list is ordered and it prints duplicate values (mutable)
# tuple is ordered and it prints duplicate values (immutable)
# set is unordered and it will not print duplicate values (mutable)
# frozenset is immutable 

# l1 = []  # list
# t1 = ()  # tuple
# s1 =set() # set
# d1 = {} # dict

# passing data
d1 = {}
print(d1, type(d1))  # {} <class 'dict'>

s1 = {10}
print(s1, type(s1))  # {10} <class 'set'>

s2 = {10, 20, 30, 40, 50, 60, 70, 80, 90, 10, 20, 30, 40}
print(s2, type(s2)) # {70, 40, 10, 80, 50, 20, 90, 60, 30} <class 'set'>

s4 = {10, 20, 30, 40, 50, 60, "NameOne", "NameTwo", "NameThree"}
s4.update([100, 200, 300, 400, 500])
print(s4)  # {200, 10, 400, 20, 30, 100, 40, 300, 50, 500, 60}

l1 = [100, 200, 300, 100, 200]
print(l1)

s1 = set(l1)
print(s1)

l2 = list(s1)
l2.sort()
print(l2)

empSalary = 10000.00
i = int(empSalary)
print(i)
