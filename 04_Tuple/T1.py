# diff b/w list and tuple

# list is unsafe (mutable)
l1 = [10, 20, 30, 40, 50]
l1[0] = 100
print(l1)

# tuple is safe (immutable)
t1 = (10, 20, 30, 40, 50)
t1[0] = 100
print(t1)  # TypeError: 'tuple' object does not support item assignment


