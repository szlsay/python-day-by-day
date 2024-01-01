'''
实现 传入一个数字，来控制输出的次数，倒序输出数字
'''


# 定义一个函数
def test_func(n):
    i = n
    while i > 0:
        print(i)
        i -= 1


test_func(10)
