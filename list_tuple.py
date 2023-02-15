# list test
import sys

classmates = ['Michael', 'Bob', 'Tracy']
print("列表 list =", classmates)
print(classmates[-1])
classmates.append("123123")
a = classmates.__str__()
print("a", a)
classmates.sort()
print("sort列表 list =", classmates)
classmates.pop(2)
print("sort列表 list =", classmates)
classmates.pop()
print("sort列表 list =", classmates)
classmates.insert(1, 3333)
print("sort列表 list =", classmates)
classmates[2] = ['asp', 'php']
print("sort列表 list =", classmates)
print(type(classmates[2][0]))

# tuple元组 test
roommates = ('Michael', 'Bob', 'Tracy')
t = (1,)
print("\ntype is ", type(t))
print(roommates[1], "\n")
# exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1], "\n")

# iter method1
for person in L:
    for name in person:
        print(name, "\t")

# print 1-100
print("list:", list(range(100)))
x = 0
for i in range(101):
    x = x + i
print(x)

# if elif test
age = 20
if age >= 6:
    print('teenager')
elif 6 <= age <= 18:
    print('adult')
else:
    print('kid')

# iter exerise
persons = ['bart', 'lisa', 'adam']
for person in persons:
    print("hello,", person.title())

if hasattr(sys, "set_int_max_str_digits"):
    upper_bound = 68000
    lower_bound = 4004
    current_limit = sys.get_int_max_str_digits()
    if current_limit == 0 or current_limit > upper_bound:
        sys.set_int_max_str_digits(upper_bound)
    elif current_limit < lower_bound:
        sys.set_int_max_str_digits(lower_bound)
