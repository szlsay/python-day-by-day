'''
循环嵌套
'''


def test_func():
    i = 1
    while i < 3:

        # 被嵌套的循环
        j = 1
        while j < 5:
            print(f'{i} --- {j}')
            # break
            continue
            j += 1

        i += 1



test_func()