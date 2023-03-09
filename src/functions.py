import numpy as np
from utils import Common
from utils.Common import height_in, weight_lb, baseball, baseball_2d

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

# numpy array 可以直接用作计算，元素间用空格分隔
npBaseball = np.array(Common.baseball)
print(npBaseball)

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Define the type of array 一个ndarray在被创建时，可以显式地指定其数据类型
# 指定数据类型后，不管输入的原列表的数据类型是什么，都会按照指定的类型进行输出
arr_float16 = np.array([1, 2, 3], dtype="float16")
arr_float16

# Create the subarray
print("subarray bmi[100:111]:", bmi[100:111])
print("bmi type is:", type(bmi), "shape of bmi:", bmi.shape)
print("baseball shape like:", baseball)
print("一维数组slice结构：[下限]:[上限]:[步长]，如baseball[:3]输出", baseball[:3])

# Create the 2d array
'''一维数组slice结构：[下限]:[上限]:[步长]
二维数组slice结构：[下限]:[上限]:[步长],[下限]:[上限]:[步长]'''
np_baseball_2d = np.array(baseball_2d)
print("baseball_2d.shape:", np_baseball_2d.shape)
# 二维数组的前十项
np_baseball_2d_first_ten_item = np_baseball_2d[:10, ]
print("baseball_2d.index[:10, :]:\n", np_baseball_2d_first_ten_item, "the shape like",
      np_baseball_2d_first_ten_item.shape)
print(np_baseball_2d_first_ten_item[1])
print(np_baseball_2d_first_ten_item[1, ])
print(np_baseball_2d_first_ten_item[0, 1])
''' bmiLightDic[0][0] = bmiTuple(0)
    bmiLightDic[0][1] = lightList(0)
    
    bmiLightDic[1][0] = bmiTuple(1)
    bmiLightDic[1][1] = lightList(1)
    
    bmiLightDic[2][0] = bmiTuple(2)
    bmiLightDic[2][1] = lightList(2)

for i in range(len(bmi)):
    print("bmi[i]:", bmi[i], "lightList[i]:", lightList[i])
    # bmiLightDic[i][0] = bmi[i]
    # bmiLightDic[i][1] = lightList[i]

print(type(bmiTuple), type(lightList), type(bmiLightDic))
print("np_height_m is:", np_height_m, "\nbmi and its' light are：", bmiLightDic)'''
