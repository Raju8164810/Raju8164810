s1 = {"NameOne", "NameTwo", "NameThree", "NameFour", "NameFive"}
s1.remove("NameOne")
print(s1)  # {'NameFive', 'NameThree', 'NameFour', 'NameTwo'}
print(s1)  # {'NameFive', 'NameThree', 'NameFour', 'NameTwo'}

s2 = {"NameOne", "NameTwo", "NameThree", "NameFour", "NameFive"}
s2.discard("NameOne")
print(s2) # {'NameFour', 'NameThree', 'NameTwo', 'NameFive'}
print(s2) # {'NameFour', 'NameThree', 'NameTwo', 'NameFive'}

# s1.remove("Sai Kiran")
# print(s1)  # KeyError: 'Sai Kiran'

s2.discard("Sai Kiran")
print(s2) # {'NameFive', 'NameFour', 'NameThree', 'NameTwo'}

