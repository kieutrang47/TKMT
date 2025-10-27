#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 08:50:11 2019

@author: vinhlinh
"""

import numpy as np
import math
from scipy import stats as stats
import matplotlib.pyplot as plt

'''
VD4: Để tăng độ chính xác ta sử dụng ước lượng khoảng thay thế cho ước lượng điểm
Trước tiên, ta thực hiện ước lượng điểm 20 lần với cỡ mẫu mỗi lần là 40 để xem xét kết quả của mỗi lần ước lượng
'''
MEDIUM_POP = np.random.randint(130, 200, size=100)
mean_of_MEDIUM_POP = np.mean(MEDIUM_POP)

np.random.seed(24)

estimate_times = 20
mean_array = np.empty(estimate_times)
for i in range(estimate_times):
    a_sample = np.random.choice(MEDIUM_POP, size=40)
    mean_array[i] = np.mean(a_sample)

#Vẽ giá trị thực tế (mean của quần thể)
_ = plt.plot(np.asarray([0, estimate_times]), np.asarray([mean_of_MEDIUM_POP, mean_of_MEDIUM_POP]), color='blue')
    
#Vẽ các kết quả ước lượng
x = np.arange(20)
_ = plt.plot(x, mean_array, marker='.', color='black')

_ = plt.xticks(np.arange(0, estimate_times, step=1))
_ = plt.xlabel('Lần thí nghiệm (1-20)')
_ = plt.ylabel('Chiều cao trung bình của mẫu (cm)')
_ = plt.title('Kết quả các lần ước lượng (với POP_mean = {})'.format(mean_of_MEDIUM_POP))
plt.show()

'''
Nhận xét: Kết quả ước lượng nằm dao động xung quanh giá trị thực tế, có kết quả gần giá trị thực tế, nhưng cũng có kết quả rất 
    - Hạn chế của ước lượng điểm: kết quả mỗi lần khác nhau, và có kết quả có sai số rất lớn
    - Để tăng độ chính xác của ước lượng thay vì dủng điểm ước lượng ta dùng một khoảng
'''

'''
VD5: Ta vẽ lại biểu đồ trên nhưng thay vì dùng điểm ước lượng ta dùng khoảng ước lượng
Giả sử ta cho phép biên độ lỗi là error_margin = 3cm, như vậy khoảng ước lượng sẽ là [point_estimate - 3, point_estimate + 3]
Sau đó ta tỷ lệ chính xác của ước lượng bằng cách tìm tỷ lệ phần trăm kết quả ước lượng đúng
'''
#Vẽ giá trị thực tế (mean của quần thể)
_ = plt.plot(np.asarray([0, estimate_times]), np.asarray([mean_of_MEDIUM_POP, mean_of_MEDIUM_POP]), color='blue')

#Vẽ các kết quả ước lượng
x = np.arange(20)
_ = plt.plot(x, mean_array, marker='.', color='black')

#Vẽ khoảng ước lượng với biên độ lỗi là 3cm
error_margin = 3
true_result = 0;
for i in range(estimate_times):
    xx = np.asarray([i, i])
    lower = mean_array[i] - error_margin
    upper = mean_array[i] + error_margin
    yy = np.asarray([lower, upper])
    if (mean_of_MEDIUM_POP <= upper and mean_of_MEDIUM_POP >= lower):
        _ = plt.plot(xx, yy, color='green', alpha=0.4)
        true_result = true_result + 1
    else:
        _ = plt.plot(xx, yy, color='red', alpha=0.4)

_ = plt.xticks(np.arange(0, estimate_times, step=1))
_ = plt.xlabel('Lần thí nghiệm (1-20)')
_ = plt.ylabel('Chiều cao trung bình của mẫu (cm)')
_ = plt.title('Kết quả các lần ước lượng (với POP_mean = {}, error_margin={})'.format(mean_of_MEDIUM_POP, error_margin))
plt.show()

print('Tỷ lệ chính xác của ước lượng: {}'.format(true_result/estimate_times))
'''
Nhận xét:
    - Kết quả ước lượng khoảng vẫn có thể sai (không chứa giá trị thực tế)
    - Để tăng độ chính xác có thể tăng độ rộng của khoảng ước lượng (tăng error_margin) --> Xem như bài tập
    - Nếu khoảng ước lượng quá rộng thì ta khó tìm giá trị thực sự trong khoảng ấy. Vậy thì độ rộng của khoảng ước lượng bao nhiêu là đủ?
'''

'''
VD6: Như vậy, để thực hiện bài toán ước lượng, ta phải cân nhắc giữa 2 yếu tố là: độ rộng khoảng và độ chính xác của ước lượng.
    - Giả sử ta chấp nhận giảm độ chính xác của ước lượng xuống 95% để đổi lấy một khoảng ước lượng bé hơn
    - Điều này có nghĩa là xác suất có được một khoảng ước lượng chứa giá trị thực tế là 95%
    - Để làm điều này ta sử dụng định lý Giới Hạn Trung Tâm
    - Với độ tin cậy của ước lượng là 95%, ta sẽ tìm biên độ lỗi dựa vào một chọn ngẫu nhiên một mẫu có cùng kích cỡ
'''
#Tạo ngẫu nhiên một mẫu có kích thước 40 từ MEDIUM_POP
sample2 = np.random.choice(MEDIUM_POP, size=40)
mean_sample2 = np.mean(sample2)
#Chuẩn bị các thông số
n = sample2.size
degree_of_freedom = n - 1
confidence_value = 0.95
t_score = stats.t.ppf(confidence_value, degree_of_freedom)
standard_error = sample2.std() / math.sqrt(n)
error_margin = t_score * standard_error
print('Biên độ lỗi với độ tin cậy là 95%: {}'.format(error_margin))

'''
VD7: Chạy lại VD5 với biên độ lỗi mới, và kiểm tra tỷ lệ ước lượng chính xác
'''
#Vẽ giá trị thực tế (mean của quần thể)
_ = plt.plot(np.asarray([0, estimate_times]), np.asarray([mean_of_MEDIUM_POP, mean_of_MEDIUM_POP]), color='blue')

#Vẽ các kết quả ước lượng
x = np.arange(20)
_ = plt.plot(x, mean_array, marker='.', color='black')

#Vẽ khoảng ước lượng với biên độ lỗi mới
true_result = 0;
for i in range(estimate_times):
    xx = np.asarray([i, i])
    lower = mean_array[i] - error_margin
    upper = mean_array[i] + error_margin
    yy = np.asarray([lower, upper])
    if (mean_of_MEDIUM_POP <= upper and mean_of_MEDIUM_POP >= lower):
        _ = plt.plot(xx, yy, color='green', alpha=0.4)
        true_result = true_result + 1
    else:
        _ = plt.plot(xx, yy, color='red', alpha=0.4)

_ = plt.xticks(np.arange(0, estimate_times, step=1))
_ = plt.xlabel('Lần thí nghiệm (1-20)')
_ = plt.ylabel('Chiều cao trung bình của mẫu (cm)')
_ = plt.title('Kết quả (với POP_mean = {}, error_margin={})'.format(mean_of_MEDIUM_POP, error_margin))
plt.show()

print('Tỷ lệ chính xác của ước lượng: {}'.format(true_result/estimate_times))
'''
Nhận xét: Qua ví dụ trên ta thấy với biên độ lỗi được tính từ độ tin cậy mong muốn là 95%. Ta được tỷ lệ chính xác của ước lượng cũng là 95% (với số lần thực hiện là 20)
Bạn hãy thử tăng số lần thực hiện lên 100 hay 1000 lần xem tỷ lệ này còn chính xác không?
'''