# adding the frozenset data in set
f3 = frozenset({10, 20, 30, 40, 50})

s2 = {"NameOne"}
s2.add(f3)
print(s2) # {frozenset({50, 20, 40, 10, 30}), 'NameOne'}

f4 = frozenset({10, 20, 30, 40, 50})
s2 = {"NameOne"}
s2.update(f4)
print(s2)  # {50, 'NameOne', 20, 40, 10, 30}

