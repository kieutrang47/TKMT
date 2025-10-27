import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#from scipy.stats import norm


#Bài Nhiptim câu a
data = pd.read_excel(r'D:\ThongKeMayTinh_UngDung\BaiTap_ThucHanh\DataSet\01_MHEALTH.xls')
df = pd.DataFrame(data)
#n: kích thước mẫu kẹo có màu xanh lá
#N kích thước mẫu kẹo có các màu bất kỳ
print(df)
N=df['PULSE'].count()
print('Tong dong:',N)
mean=df['PULSE'].mean()

print('Mean la:',mean)
#df_tang = df.query('BMISP>BMIAP')

print(mean)
s=df['PULSE'].std()
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

#Bài Nhiptim câu b
data = pd.read_excel(r'D:\ThongKeMayTinh_UngDung\BaiTap_ThucHanh\DataSet\01_FHEALTH.xls')
df = pd.DataFrame(data)

print(df)
N=df['PULSE'].count()
print('Tong dong:',N)
mean=df['PULSE'].mean()

print('Mean la:',mean)
#df_tang = df.query('BMISP>BMIAP')

print(mean)
s=df['PULSE'].std()
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


#Kết quả câu a)......b)....
#kết quả không khác nhau vì Confidence Intervals overlap 



