'''
	*
	**
	***
	****
	*****

'''


def test_func1():
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            print('*', end='')
            if j == i:
                break
            j += 1
        print()
        i += 1


def test_func2():
    i = 0
    while i < 5:
        j = 0
        while j <= i:
            print('*', end='')
            j += 1
        print()
        i += 1


def test_func3():
    i = 0
    while i < 5:
        # 定义一个空字符串，用来拼接使用
        s = ''
        j = 0
        while j <= i:
            s += '*'  # s = s + '*'
            j += 1
        print(s)
        i +=1


'''
输出下列图形：
1
12
123
1234
12345

输出行数由参数控制
'''

# test_func1()
# test_func2()
test_func3()