'''
打印99乘法表
'''


def nine_nine_table():
    i = 1
    while i <= 9:
        j = 1
        while j <= i:
            print('%d*%d=%-3d' % (j, i, j*i), end=' ')
            j += 1
        print()
        i += 1



nine_nine_table()