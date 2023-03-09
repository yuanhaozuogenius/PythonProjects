import numpy as np
from utils import Common

""" help() 函数用来查看某个函数或者模块的帮助文档,help() 查看某个函数的用法时，函数名后边不能带括号,查看其用法和返回类型"""
help(max)
print(dir(pow))
help(pow)
help(str.count)
help(sorted)

print(sorted(Common.areasName), sorted(Common.areasName, reverse=True))

print("areasNum:", Common.areasNum, Common.areasNum[::-1])
Common.areasNum.reverse()
print("areasNum after reverse():", Common.areasNum)

# numpy array
npBaseball = np.array(Common.baseball)
print(npBaseball)



