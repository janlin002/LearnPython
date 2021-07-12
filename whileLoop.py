#coding=UTF-8
n = 0
while n < 5:
    n+=1
    print(n)

for item in [1,2,3]:
    print(item, 'item')

for item in range(3): #連續得數字列表
    print(item, 'range')

for item in range(3,6):
    print(item, '3-6') # [3, 4, 5]

n=0
x=0
while n<10:
    n+=1
    x+=n
    print(x)