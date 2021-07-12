#coding=UTF-8
# break
n=0
while n < 5:
    if n == 3:
        break # 當符合條件就強制結束回圈
    n+=1
print(n)

#continue
# n=0
# for x in [0, 1, 2, 3, 4]:
#     if x%2 == 0:
#         continue
#     n+=1
#     print("最後的n: " ,n)

#else

# x = int(input('請輸入數字: '))
# for i in range(x):
#     if i*i == x:
#         print('i')
#         break
#     else:
#         print('沒有平方根')

# n=0
# while n<5:
#     n+=1
#     print(n)