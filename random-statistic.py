# coding=UTF-8
# 隨機模組
import random

#髓機選取
data = random.choice([1,2,3,5,6])
print(data)

data = random.sample([1,2,3,5,6], 3)
print(data)

#隨機調換順序
data = [1,2,3,5,6]
random.shuffle(data)
print(data)

#隨機取的亂數
data = random.random()
print(data)

data = random.uniform(0.0, 1.0)
print(data)

#取得常態分佈亂數
#平均數100標準差5
data = random.normalvariate(100,5)
print(data)
# 統計模組

import statistics as sta

#平均數
data = sta.mean([1,2,3,5,6])
print(data)

#中位數
data = sta.median([1,2,3,5,6])
print(data)

#標準差
data = sta.stdev([1,2,3,5,6])
print(data)
