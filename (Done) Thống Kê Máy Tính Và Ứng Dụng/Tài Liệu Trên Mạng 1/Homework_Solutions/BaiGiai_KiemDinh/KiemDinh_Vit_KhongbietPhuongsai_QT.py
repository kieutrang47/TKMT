import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#from scipy.stats import norm

#Kiểm định giá trị trung bình khi biết phương sai của quần thể
col_names=['Dai']
data = pd.read_excel(r'D:\ThongKeMayTinh_UngDung\BaiTap_ThucHanh\DataSet\19_SCREWS.xls',names=col_names, header=None)
#print(data)
df = pd.DataFrame(data)
n=df['Dai'].count()
print('N là:',n)
#n: kích thước mẫu kẹo có màu xanh lá
#N kích thước mẫu kẹo có các màu bất kỳ

#n=19
#N=100
#ti le la 0.19

#ta đi kiểm định giả thuyết
#H0: mu=0.75
#Ha: mu#0.75

mu=0.75
x_gach=df['Dai'].mean()
print('X_gach là:',x_gach)

s=df['Dai'].std()
print('s là:',s)



t=(x_gach-mu)/(s/np.sqrt(n))
print('t là:',t)

alpha=0.05

Pvalues=2*st.t.cdf(t,n-1,0,1)
print('Pvalue:',Pvalues)
if(Pvalues>alpha):
    print('Fail to reject H0, không có bằng chứng để bác bỏ H0')
else:
    print('Bác bỏ H0')
    
