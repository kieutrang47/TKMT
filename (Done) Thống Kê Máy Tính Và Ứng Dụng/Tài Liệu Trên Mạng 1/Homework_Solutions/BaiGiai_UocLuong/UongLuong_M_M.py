import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#from scipy.stats import norm

#Bài 1.	Green M&M Candies 
data = pd.read_excel(r'C:\Users\PC\Desktop\Đang học\thống kê\DataSet\18_M&M.xls')
print(data)
df = pd.DataFrame(data, columns= ['Red','Orange','Yellow','Brown','Blue','Green'])
#n: kích thước mẫu kẹo có màu xanh lá
#N kích thước mẫu kẹo có các màu bất kỳ
n=df['Green'].count()
N=df['Blue'].count()+df['Red'].count()+df['Orange'].count()+df['Yellow'].count()+df['Brown'].count()+df['Green'].count()
#n=19
#N=100
#ti le la 0.19
print('Ti le là:',n/N)
p_mu=n/N
q_mu=1-p_mu

#là giá trị z mà tại đó xác suất <z là 0.025
#máy tính tính theo dạng xác suất tích lũy nghĩa là tính xác suất <1 giá trị z nào đó
Z_alpha_chia2= (-1)*st.norm.ppf(.025,0,1)

print("Z_alpha_chia2:",Z_alpha_chia2)
e=Z_alpha_chia2*np.sqrt(p_mu*q_mu/N)
print("Loi la:",e)
print("Khoang tin cay la",p_mu-e,p_mu+e)

