import numpy as np
from matplotlib import pyplot as plt


from utils.Common import gdp_cap, life_exp, pop, col

# plt.plot(gdp_cap, life_exp)
# scatter 散点图
plt.scatter(gdp_cap, life_exp, s=np.array(pop), c=col)
# 显示网格 默认False
plt.grid(True)
# x轴的比例设置为对数
plt.xscale('log')
plt.xlabel("gdp_cap")
plt.ylabel("life_exp")
plt.title("Log scatter for gdp_cap & life_exp")
# Additional customizations
plt.text(1550, 71, 'India')
plt.text(5700, 80, 'China')
plt.show()
# clean the plot shown
plt.clf()

# Histogram 柱状图 , bin:宽度，默认为10
plt.hist(life_exp, bins=5)
''' 获取或设置当前x轴刻度位置和标签，即把坐标轴改成自己要的样子。
    ticks：x轴刻度位置的列表，若传入空列表，即不显示x轴
    labels：放在指定刻度位置的标签文本。当ticks参数有输入值，该参数才能传入参数
    **kwargs：文本属性用来控制标签文本的展示，例如字体大小、字体样式等'''
plt.xticks()
plt.show()
plt.clf()
