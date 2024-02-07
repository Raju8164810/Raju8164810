# frozenset 
f1 = frozenset()
print(f1, type(f1))  # frozenset() <class 'frozenset'>


# adding the set data in frozenset
s1 = {10, 20, 30, 40, 50}
f2 = frozenset(s1)
print(f2)  # frozenset({50, 20, 40, 10, 30})


# adding the frozenset data in set
f3 = frozenset({10, 20, 30, 40, 50})
s2 = {"NameOne"}
s2.update(f3)
print(s2) # {50, 20, 40, 10, 'NameOne', 30}

f2 = frozenset({10, 20, 30, 40, 50})
print(f2) # frozenset({50, 20, 40, 10, 30})

s1 = {100,200,300,400,500}
s1.add(f2) 

print(s1)  # {400, 100, 500, 200, 300, frozenset({50, 20, 40, 10, 30})}
s1.remove(f2)
print(s1)

print(f2)