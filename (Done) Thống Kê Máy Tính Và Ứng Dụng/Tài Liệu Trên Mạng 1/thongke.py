# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:28:50 2021

@author: PC
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("babies.txt", sep='\s+')
df.info() #thong tin bảng
print(df.head(5))
print(df.tail(5))

#Lấy cột smoke = 0, tức không hút thuốc
df_khonghutthuoc = df[df['smoke'] == 0] #Cách 1
#df_khonghutthuoc = df[df.smoke == 0] #Cách 2
print("Những bà mẹ không hút thuốc")
print(df_khonghutthuoc)
print(df_khonghutthuoc.describe()) #Thống kê mô tả
print("Độ lệch Skewness")
print(df_khonghutthuoc.skew())
print("Độ nhọn Kurtosis:")
print(df_khonghutthuoc.kurtosis())

print("###############################")
      
#Lấy cột smoke = 1, tức có hút thuốc
#df_cohutthuoc = df[df['smoke'] == 1] #Cách 1
df_cohutthuoc= df[df.smoke == 1] #Cách 2
print("Những bà mẹ có hút thuốc")
print(df_cohutthuoc)
print(df_cohutthuoc.describe()) #Thống kê mô tả
print("Độ lệch Skewness")
print(df_cohutthuoc.skew())
print("Độ nhọn Kurtosis:")
print(df_cohutthuoc.kurtosis())

#lay du lieu mot cot
coHutThuoc=np.array(df_cohutthuoc['bwt'])
khongHutThuoc=np.array(df_khonghutthuoc['bwt'])

#Vẽ boxplot
df.boxplot(by ='smoke', column =['bwt'], grid = False)
plt.show()

plt.boxplot(coHutThuoc, sym='*')
plt.ylabel('Cân nặng')
plt.title('Boxplot trong trường hợp bà mẹ có hút thuốc')
plt.show()


plt.boxplot(khongHutThuoc, sym='*')
plt.ylabel('Cân nặng')
plt.title('Boxplot trong trường hợp bà mẹ không hút thuốc')
plt.show()





