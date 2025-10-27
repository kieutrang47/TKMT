import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
#from scipy.stats import norm



data = pd.read_excel(r'D:\ThongKeMayTinh_UngDung\BaiTap_ThucHanh\DataSet\09_MOVIES.xls')
print(data)
df = pd.DataFrame(data, columns= ['Title','MPAA','Budget','Gross','Length','Rating'])

N=df['Gross'].count()
print('Tong dong:',N)
mean=df['Gross'].mean()
#df_tang = df.query('BMISP>BMIAP')
print(mean)

xichma=100

#là giá trị z mà tại đó xác suất <z là 0.025
#máy tính tính theo dạng xác suất tích lũy nghĩa là tính xác suất <1 giá trị
Z_alpha_chia2= (-1)*st.norm.ppf(.025,0,1)

print("Z_alpha_chia2:",Z_alpha_chia2)
e=Z_alpha_chia2*xichma/np.sqrt(N)
print("Loi la:",e)
print("Khoang tin cay la",mean-e,mean+e)

