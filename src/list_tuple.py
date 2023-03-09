# list test
import sys

from utils.Common import areas

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
print("\ntype of t is ", type(t), "\tt :", t, "\n")
print("roommates are:", roommates, "\n")
print()
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

# Slicing and dicing
# Create the areas list
'''Use slicing to create a list, downstairs, that contains the first 6 elements of areas.
Do a similar thing to create a new variable, upstairs, that contains the last 4 elements of areas.
Print both downstairs and upstairs using print().'''

'''proper_slice的结构是"[下限]:[上限]:[步长]"'''

# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6::1]

# Print out downstairs and upstairs
print("downstairs:", downstairs, "upstairs:", upstairs, "\n")

print("the matrix slice:", [["a", "b", "c"],
                            ["d", "e", "f"],
                            ["g", "h", "i"]][-1][1], "\n")

# Extend a list

# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse", 24.5]
print("areas_1:", areas_1)
# Add garage data to areas_1, new list is areas_2
areas_1.append("garage")
areas_1.append(15.45)
areas_2 = areas_1
print("areas_2:", areas_2)
print("areas_2[:1]:", areas_2[:2])
# [下限]>[上限]时，无任何改变
del (areas_2[3:1])
del (areas_2[-2:-4])
# [下限]<[上限]时，操作有意义
del (areas_2[-4:-2])
print("areas_2:", areas_2)

# 精确copy和copy
# Create areas_copy， areas_copy的改变会影响areas的值
areas_copy = areas
areas_copy[0] = 5.0
# Create explicit areas_copy use list() or [::1]
areas_explicit_copy = list(areas)
areas_explicit_copy[0] = 6.0
print(areas_explicit_copy)
print("精确copy和copy test:", areas)

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
