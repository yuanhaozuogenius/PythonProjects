# list test
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

# exercise
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print("\n", L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[-1][-1])


# 创建学生类
class Stu():
    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Stu("张三", 18)
print(type(s))
print(str(s))
print(s)
