'''
循环嵌套练习

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

'''

# test_func1
def test_func1():
    print('* * * * *')
    print('* * * * *')
    print('* * * * *')
    print('* * * * *')
    print('* * * * *')


def test_func2():
    i = 1
    while i <= 5:
        print('* ' * 5)
        i += 1



def test_func3():
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            print('*', end=' ')
            j += 1

        # 由于上面内循环中改变了输出函数的结束符号，所以不会换行
        # 在内循环外面，加入一个输出，让内循环执行完成后，加入一个换行
        print()

        i += 1



# 思考题目：不使用修改print结束标记的方式 ，实现图形的输出

# test_func1()
# test_func2()
test_func3()
