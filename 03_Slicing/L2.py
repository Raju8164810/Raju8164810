# slicing
# start : end(-1) : defaultstepover(1)
# start : end(-1) : defaultstepover(-1)
l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
#      0   1   2   3   4   5   6   7   8   9    10   11 
#     -12 -11 -10  -9  -8  -7  -6 - 5  -4  -3   -2    -1 
print(l1)
print(l1[:])
print(l1[0:])
print(l1[0:12])
print(l1.copy())
print(l1[0:len(l1)])

print('neg')
print(l1[-11:-1:1])
print(l1[-1:-11:1])

print(l1[::-1])

print(l1[::-2])
print(l1[::2])

print(l1[-8:-11:1])
print(l1[-8:-11:-1])