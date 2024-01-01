'''
关系比较运算符
'''

def test_func():
    # ==
    print(1 == 2)  # False
    print(1 == 1)  # True

    print('*' * 10)
    # !=
    print(1 != 2)  # True
    print(1 == 2)  # False


    print('*' * 10)
    # >
    print(1 > 2) # False
    print(2 > 1) # True

    # <
    print(1 < 2) # True
    print(2 < 1) # False

    # >=  <=
    print('*' * 10)
    # >=
    print(1 >= 2)  # False
    print(2 >= 1)  # True
    print(1 >= 1)  # True

    # <=
    print(1 <= 2)  # True
    print(2 <= 1)  # False
    print(1 <= 1)  # True

test_func()