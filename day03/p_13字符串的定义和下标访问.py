'''
字符串的定义和下标访问
'''

def defined_str():
    # 空字符串
    print('')
    print("")
    print('''''')
    print("""""")

def defined_str_space():
    # 带一个空格的字符串
    print(' ')
    print(" ")
    print(''' ''')
    print(""" """)


# 定义一个函数，用来使用下标访问字符串
def use_index_access_str():
    s1 = 'abcde'
    s2 = '01234'

    print(s1[0])
    print(s1[2])
    print(s1[4])

    print(s2[0])
    print(s2[2])
    print(s2[4])

    # print(s1[5]) # IndexError: string index out of range  # 字符串下标越界

    # 字符串不允许通过下标来修改字符串中的内容
    # 字符串是不允许修改的，因为字符串是一个不可变对象
    # s2[2] = '9'  # TypeError: 'str' object does not support item assignment






defined_str()
defined_str_space()
use_index_access_str()