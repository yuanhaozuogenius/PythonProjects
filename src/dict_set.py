# dict example
dic = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

print(dic['Tracy'])
print(dic.copy()['Bob'])
print(dic.get('Michael'))
print(dic.get('MichaelJack', -1))

dic['Adam'] = 67

print(dic)
print(dic.keys())
print(dic.values())
keys = list(dic.keys())
# 取dic中第n个键值的value
print(dic[keys[2]])
print(dic.pop('Bob'))
