# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:47:58 2021

@author: PC
"""
"""
LAB 2
"""
import pandas as pd
import numpy as np
import scipy.stats as st

#Xây dựng histogram
data = pd.read_excel(r'C:\Users\PC\Desktop\Đang học\thống kê\DataSet\15_OLDFAITH')
print(data)

plt.hist(data, bins=12)
plt.title('Histogram truong hop nhung ba me co hut thuoc')
plt.xlabel('Can nang')
plt.show()