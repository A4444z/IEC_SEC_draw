import numpy as np
import matplotlib.pyplot as plt
import xlrd
import os

name = "Smurf1-Heparin-20230321"
filename = "202303201-SMURF1-heparin-0-50%-50min"
y0 = -10
y1 = 50
x0 = 60
x1 = 110
file = os.getcwd()+filename

#读取Excel，将A260放在原sheet，A280复制到sheet1，cond到sheet2，否则因为数据长度不同坐标会被压缩
workbook = xlrd.open_workbook('/Users/zhangtianyi/T/Liu Lab/课题/Smurf1/purification/202303201-SMURF1-heparin-0-50%-50min.xls')
sheet0 = workbook.sheet_by_name(u'Sheet0')
sheet1 = workbook.sheet_by_name(u'Sheet1')
sheet2 = workbook.sheet_by_name(u'Sheet2')

#按列读取x、y轴的数据
A280_mL = sheet0.col_values(0)
A280_mAu = sheet0.col_values(1)

A260_mL = sheet1.col_values(0)
A260_mAu = sheet1.col_values(1)

Cond_mL = sheet2.col_values(0)
Cond_value = sheet2.col_values(1)

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
plt.ylim((0,50))
#plt.xlim((40,85))

#图例
lns = A260+A280+conds
labels = [l.get_label() for l in lns]
plt.legend(lns, labels)

plt.savefig("./i.png")

plt.show()