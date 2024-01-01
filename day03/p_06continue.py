'''
continue 使用
'''


def test_func():
    i = 1
    while i <= 5:
        i += 1
        print('hello')
        continue
        print('world')


test_func()