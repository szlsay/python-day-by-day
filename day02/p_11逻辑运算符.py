'''
逻辑运算符
'''

def test_func():
    # 逻辑与 and   理解成乘法  ture 表示1  false 表示 0
    print(True and True)  # True
    print(True and False)  # False
    print(False and True)  # False
    print(False and False)  # False


    # 逻辑或 or  理解成加法
    print(True or True)  # True
    print(True or False)  # True
    print(False or True)  # True
    print(False or False)  # False

    # 逻辑非
    print(not True)  # False
    print(not False)  # True

    print('*' * 10)

    # a = int(input('number:'))
    # print(a > 0 and a > 10)  # True and False  - > False

    print(1 and 2 and 3)
    print(0 and 2 and 3)

    print(1 or 2 or 3)
    print(0 or 2 or 3)
    print(0 or 0 or 3)






test_func()