# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


#Mô phỏng tung đồng xu 4 lần
np.random.seed(10)

#In 2 số ngẫn nhiên trong khoảng (0,1)
print(np.random.random())
print(np.random.random())


#Phát sinh 4 số ngẫn nhiên trong khoảng (0,1)
arr=np.random.random(size=4)
print(arr)

#Tạo mẫu mô phỏng 4 lần tung đồng xu với (True: Sấp, False: Ngửa)

coin_sample=arr<0.5
print(coin_sample)

'''
VD1: Sử dụng ước lượng điểm để ước lượng tham số của quần thể
'''
#Khởi tạo một quần thể cho trước thể hiện chiều cao(cm) của 5 thanh 
SMALL_POP = np.array([186, 182, 157, 158, 152])
print(SMALL_POP)
mean_of_SMALL_POP = np.mean(SMALL_POP)
print('Chiều cao trung bình của Quần Thể : {}'.format(mean_of_SMALL_POP))

#Lấy ngẫu nhiên một mẫu có kích thước là 4, và tính chiều cao trung bình và so sánh với giá trị của quần thể
np.random.seed(24)
sample1 = np.random.choice(SMALL_POP, size=4, replace=True)
sample1_mean = np.mean(sample1)
print('Mẫu ngẫu nhiên 1: ', sample1)
print('Chiều cao trung bình của mẫu 1: {}'.format(sample1_mean))
print('Sai số ước lượng: {}'.format(abs(sample1_mean - mean_of_SMALL_POP)))

#Nhận xét: Sai số ước lượng là: 3.75cm. Ta có thể chấp nhận được với bài toán đo chiều cao

'''
VD2: Để cho việc đo sai số khách quan, ta thử lặp lại việc lấy mẫu trên 10 lần, và tính sai số ước lượng
'''
mean_array = np.empty(10)
for i in range(10):
        random_sample = np.random.choice(SMALL_POP, size=4, replace=True)
        random_sample_mean = np.mean(random_sample)
        mean_array[i] = random_sample_mean
        
print('Chieu cao trung binh cua 10 mau thu duoc: ', mean_array) 
print('Sai so uoc luong: {}'.format(abs(np.mean(mean_array) - mean_of_SMALL_POP)))

#Nhận xét: Ta nhận thấy, khi thực hiện việc lấy mẫu nhiều lần, sai số trung bình có nhỏ hơn so với ví dụ trên.
#Câu hỏi: nếu ta có khả năng lấy mẫu được nhiều lần, liệu rằng ta có thể lấy mẫu 1 lần với mẫu có nhiều phần tử thì kết quả có khác không?

'''
VD3: Minh hoạ ảnh hưởng của cỡ mẫu đến độ chính xác của ước lượng
    - Để rõ ràng ta sẽ tạo một quần thể mới gồm 100 cá thể: MEDUIUM_POP
    - Lần lượt lấy mẫu với kích cỡ khác nhau sample_size = 1, 2, 3, ... và tính trung bình mẫu: mean_array
    - Trực quan bẳng đồ thị
'''
MEDIUM_POP = np.random.randint(130, 200, size=100)
mean_of_MEDIUM_POP = np.mean(MEDIUM_POP)
mean_array = np.empty(100)
mean_array[0] = 0

for sample_size in range(1, 100):
    temp = np.random.choice(MEDIUM_POP, size=sample_size)
    mean_array[sample_size] = np.mean(temp)

x = np.arange(100)
_ = plt.plot(x, mean_array, marker='.', color='black')

_ = plt.xlabel('Kích cỡ mẫu (0-100)')
_ = plt.ylabel('Chiều cao trung bình của mẫu (cm)')
_ = plt.title('Ảnh hưởng của kích cỡ mẫu đến độ chính xác của ước lượng điểm')
    
xx = np.array([0, 100])
yy = np.empty(2)
yy[0] = yy[1] = mean_of_MEDIUM_POP

_ = plt.plot(xx, yy, color='green')
print(mean_array)
plt.show()

#Nhận xét: Qua ví dụ trên ta có thể nhận thấy kích thước mẫu có liên quan đến độ chính xác của ước lượng điểm
#Kết luận: Để tăng độ chính xác của ước lượng ta có thể tăng kích thước của quần thể
