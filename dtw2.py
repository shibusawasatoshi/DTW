import numpy as np
from scipy.spatial.distance import euclidean
from fastdtw import fastdtw
from matplotlib import pyplot as plt
import csv
with open("/Users/shibusawasatoshi/Downloads/DTW4.csv",newline='',encoding='utf-8-sig') as f:
  for row in csv.reader(f):
    print(f"{row}")
with open("/Users/shibusawasatoshi/Downloads/DTW3.csv",newline='',encoding='utf-8-sig') as f:
  for row2 in csv.reader(f):
    print(f"{row2}")
    
row_list = list(map(float, row))
row_list2 = list(map(float, row2))
print(row_list)
print(row_list2)
# 異なる2種類のデータを定義
x = np.array(row_list).reshape(-1, 1)
y = np.array(row_list2).reshape(-1, 1)
# DTWを計算
distance, path = fastdtw(x, y, dist=euclidean)
print("DTW距離:", distance)
plt.plot(x, label='tasaka')
plt.plot(y, label='koyama')
# 各点がどのように対応しているかを図示する
for x_, y_ in path:
  plt.plot([x_, y_], [x[x_], y[y_]], color='gray', linestyle='dotted', linewidth=1)
plt.legend()
plt.title('angular velocity in y-coordinate')
plt.show()