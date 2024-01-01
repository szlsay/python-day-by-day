'''
练习 ：
定义一个函数
接收一个数字参数，判断该 数字是否是偶数
'''

# 定义一个函数，判断 是否是偶数
def is_even(n):
    if n % 2 == 0 :
        print(f'{n} 是偶数')
    else:
        print(f'{n} 是奇数')


m = int(input('please input number:'))
is_even(m)