employee = {
    'name' : {'firstName' : "Sai", 'secondName' : 'Kiran'},
    'job' : ['developer', 'devops'],
    'salary' : 20000.00,
    'age' : 28
}

print(employee['name'])  # {'firstName': 'Sai', 'secondName': 'Kiran'}
print(employee["name"]["secondName"])  # Kiran
print(employee["job"][1])  # devops
print(employee["age"]) # 28

d1 = {'a':10, 'b':  20, 'c': 30, 'd': 40}
d2 = {'e':20, 'f':  40, 'g': 60, 'h':  80}  
d1.update(d2)
print(d1)  # {'a': 10, 'b': 20, 'c': 30, 'd': 40, 'e': 20, 'f': 40, 'g': 60, 'h': 80}

d1.update({'x':1000})
print(d1)

d1.update({'y':2000})
print(d1)
 
 