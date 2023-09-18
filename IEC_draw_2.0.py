import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os
import pandas as pd

brand = "biorad"
name = "20230620-UB6466A-SOURCES-0-50%-40MIN-ACNA-PH4.5" #希望的图片名称
filename = "20230620-UB6466A-SOURCES-0-50%-40MIN-ACNA-PH4.5" #读取的文件名
y0 = -10
y1 = 1000
x0 = 50
x1 = 110
y_cond0 = 0
y_cond1 = 50
filepath = os.path.abspath(os.path.dirname(__file__)) #读取文件路径，因为绘图时把绘图程序和原始数据会放在同一文件夹下，不能用os.cwd()
file = filepath +'/'+filename + '.csv' #将路径和文件名组装


if brand == "GE":
    data = pd.read_csv(file, header=2)
    # read x,y by col
    A260_mL = data.iloc[:, 2]
    A260_mAu = data.iloc[:, 3]
    A280_mL = data.iloc[:, 0]
    A280_mAu = data.iloc[:,1]
    Cond_mL = data.iloc[:, 4]
    Cond_value = data.iloc[:, 5]

if brand == "biorad":
    data = pd.read_csv(file, header=1) #pandas read csv
    A260_mL = data.iloc[:, 0]
    A260_mAu = data.iloc[:, 1]
    A280_mL = data.iloc[:, 2]
    A280_mAu = data.iloc[:,3]
    Cond_mL = data.iloc[:, 4]
    Cond_value = data.iloc[:, 5]



#第一张图画absorb（260+280）
fig,ab = plt.subplots()

plt.title(name)

A260 = ab.plot(A260_mL, A260_mAu, color='red', label = 'A260')
A280 = ab.plot(A280_mL, A280_mAu, color = 'blue', label = 'A280')
ab.set_xlabel('Volume (mL)')
ab.set_ylabel('Absorbtion (mAu)')
plt.ylim((y0,y1))
plt.xlim((x0,x1))
#plt.legend()

#第二张画电导，因为需要单独的y轴
cond = ab.twinx()
conds = cond.plot(Cond_mL, Cond_value, color = 'brown', label = 'Cond')
cond.set_ylabel('Cond (mS/cm)')
plt.ylim((y_cond0,y_cond1))
#plt.xlim((40,85))

#图例
lns = A260+A280+conds
labels = [l.get_label() for l in lns]
plt.legend(lns, labels)

plt.savefig(filepath + '/' + name + ".png")

plt.show()