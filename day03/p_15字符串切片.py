'''
字符串切片


现有一个字符串，想得到 该字符串的第3到5个字符

'''

def str_slice(src_s, start,stop):
    # 要返回的切片后的结果
    s = ''
    i = 0
    while i < len(src_s):
        if i >= start and i < stop:
            s += src_s[i]
        i += 1

    return s


# print(str_slice('0123456789', 3, 5))



# 字符串切片
s = '0123456789'

print(s[0:5:1])
print(s[0:5:2])
print(s[3:6])   # 默认步长可以不写，默认为1
print(s[:5])    # 开始索引也可以不写，默认从头开始
print(s[5:])    # 结束也可以不写，默认到最后
print(s[:])     # 全默认，默认截取整串
print(s)
print(s[10:20])     # 切片时不会出现下标越界错误


# 切片的下标还可是以负数
# 负数是，是从右向左切片，起始下标为 -1
print(s[-1:-5])
print(s[-1:-5:-1])

# 特殊需要记住的切片方式
# 使用切片实现字符串逆序
print(s[::-1])

'''
练习作业：
自己实现字符串逆序
'''


