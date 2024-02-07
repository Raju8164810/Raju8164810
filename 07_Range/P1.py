r1 = range(10)
print(r1)  #  range(0, 10)

print(list(r1))


r2 = range(0, 20, 2)
print(r2) 

print(tuple(r2))

print(set(r2))

# print(dict(r2))  # TypeError: cannot convert dictionary update sequence element #0 to a sequence

l1 = []
l1.extend(r2)
print(l1)