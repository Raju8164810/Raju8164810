# empty list
l1 = []
print(l1)

# append(element)
# append() method will add the data ath end of the list
l1.append(10)
l1.append(20)
l1.append("NameThree")
l1.append(40)
print(l1)  #  [10, 20, 'NameThree', 40]

l2 = ["NameOne", "NameTwo", "NameThree"]
l2.append("NameFour")
print(l2)  # 'NameOne', 'NameTwo', 'NameThree', 'NameFour']

# extend(elements) 
# extends() method will add multiple elements at the end of the list
l3 = []
l3.extend([10, 20, 30, 40, 50])
print(l3) 
# TypeError: list.extend() takes exactly one argument (5 given)
# [10, 20, 30, 40, 50]

l4 = []
l4.extend("Sai Kiran")
print(l4)  #  ['S', 'a', 'i', ' ', 'K', 'i', 'r', 'a', 'n']


l5 = []
l5.extend(["Sai Kiran", "Sai Ram", "Sai Krishna"])
print(l5)
# TypeError: list.extend() takes exactly one argument (3 given)
# ['Sai Kiran', 'Sai Ram', 'Sai Krishna']

# insert(index, element)
l6 = ["NameOne", "NameTwo", "NameThree", "NameFour", "NameFive"]
#         0         1            2           3         4
print(len(l6)) #  5
l6.insert(2, "NameZero")
print(l6)  # ['NameOne', 'NameTwo', 'NameZero', 'NameThree', 'NameFour', 'NameFive']
print(len(l6))  # 6

