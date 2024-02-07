t1 = 10
print(t1, type(t1))  # 10 <class 'int'>

t2 = 10,
print(t2, type(t2)) # (10,) <class 'tuple'>

t2 = 10,20,30,40,50
print(t2, type(t2))  # (10, 20, 30, 40, 50) <class 'tuple'>

t3 = (10,20,30,40,50)
print(t3, type(t3)) #(10, 20, 30, 40, 50) <class 'tuple'>

# default value
t4  = tuple()
print(t4, type(t4))  # () <class 'tuple'>

t5 = (10,20,30,40,50)
print(t5[2]) # 30
print(t5[2:4]) # (30, 40)

t6 = (10,20,30,40,50, 10, 30, 30, 10)
print(t6.count(10))  # 3

