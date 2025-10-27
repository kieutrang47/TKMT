import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#from scipy.stats import norm


#Bài Nicotin câu a
data = pd.read_excel(r'C:\Users\PC\Desktop\Đang học\thống kê\DataSet\04_CIGARET.xls')
df = pd.DataFrame(data,columns=['KgTar','KgNic','KgCO','MnTar','MnNic','MnCO','FLTar','FLNic','FLCO'])
print(df)
N=df['KgNic'].count()
print('Tong dong:',N)
mean=df['KgNic'].mean()

print('Mean la:',mean)

print(mean)
s=df['KgNic'].std()
print('phuong sau mau s la:',s)

#là giá trị z mà tại đó xác suất <z là 0.025
#máy tính tính theo dạng xác suất tích lũy nghĩa là tính xác suất <1 giá trị

#nếu là phân phối t

#e=st.t.cdf(.05,10,0,1)*np.sqrt(p_mu*q_mu/N)

#alpha=0.05 vì độ tin cậy là 0.95 nên alpha=1-độ tin cậy
#alpha/2= 0.025, với bậc tự do là N-1, N là kích thước mẫu
t_alpha_chia2= (-1)*st.t.ppf(0.025,N-1,0,1)
print('T alpha/2 la:',t_alpha_chia2)


e=t_alpha_chia2*s/np.sqrt(N)
print("Loi la:",e)
print("Khoang tin cay la",mean-e,mean+e)




