#coding=UTF-8
# x=input('請輸入數字: ') # 取得字串形式的使用者輸入
# x=int(x) # 將字串轉成數字型態
# if x>100:
#     print('True')
# else:
#     print('false')

n1 = int(input('請輸入數字 1: '))
n2 = int(input('請輸入數字 2: '))
op = input('請輸入運算符號: +, -, *, /: ')
if op == '+':
    print(n1+n2)
elif op == '-':
    print(n1-n2)
elif op == '*':
    print(n1*n2)
elif op == '/':
    print(n1/n2)
else :
    print('輸入錯誤')