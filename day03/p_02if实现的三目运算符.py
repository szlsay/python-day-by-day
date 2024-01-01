'''
if 实现的三目运算符

'''

def test_func():

    # 输入一个数,判断奇偶
    n = int(input('number:'))

    # s = '偶数' if n % 2 == 0 else '奇数'
    s = '奇数' if n % 2 != 0 else '偶数'

    print(s)



test_func()
