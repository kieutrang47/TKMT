import pandas as pd
import numpy as np
import scipy.stats as st


data = pd.read_excel(r'18_M&M.xls')
print(data)
df = pd.DataFrame(data, columns= ['Red','Orange','Yellow','Brown','Blue','Green'])
#n: kích thước mẫu kẹo có màu xanh lá
#N kích thước mẫu kẹo có các màu bất kỳ
n = df['Red'].count()
print('n là: ', n)

N = df['Blue'].count()+df['Red'].count()+df['Orange'].count()+df['Yellow'].count()+df['Brown'].count()+df['Green'].count()
print('N là: ', N)
#n=19
#N=100

print('Tỉ lệ kẹo màu đỏ:',n/N) # 0.19

#Kiểm định giả thuyết “ít hơn 20% kẹo M & M một màu có màu đỏ"
#H0: p <= 0.2
#Ha: p > 0.2

p0 = 0.2
p = n/N


z = ( p - p0 ) / np.sqrt( (p0*(1-p0)) / n )

alpha = 0.05
print('Z=', z)

Pvalues = 2*st.norm.cdf(z,0,1)
print('P-value là:', Pvalues)

if(Pvalues < alpha):
    print('Fail to reject H0, không có bằng chứng để bác bỏ H0')
else:
    print('Bác bỏ H0')
