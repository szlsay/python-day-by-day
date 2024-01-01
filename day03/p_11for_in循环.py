'''
for-in 循环使用方式
'''

def test_func1():

    # 得到字符串中的所有字符
    for c in 'abcdefg':
        # 将小写字母变成大写输出
        print(c.upper())


# for-in 循环如果需要计数，需要配合 range() 实现
# range 有两个参数，参数一是起始值 ，参数二是终止值
# 得到一个数字区间，是一个左闭右开区间， [start, end)
# 如果只给一个参数，那么默认是终止值 ，起始值默认是 0

def test_func2():
    for i in range(10, 20):
        print(i)

def test_func3():
    # 如果需 要计数，但又不需 要用到这个数字时，可以没有循环变量
    for _ in range(5):
        print('hello', _)


test_func1()
test_func2()
test_func3()

