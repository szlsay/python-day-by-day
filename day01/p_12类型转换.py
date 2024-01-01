'''
类型转换
'''

# 转换成整数类型
print(int(1))
print(int(1.1))
print(int('1'))
# print(int('1.1')) # 转换错误
# print(int('abc')) # 转换错误

# 转换成浮点类型
print(float(1))
print(float(1.1))
print(float('1.1'))
print(float('1'))
# print(float('abc')) # 转换错误


# 转换成字符串类型
print('| ' + str(1) + ' |')
print('| ' + str(1.1) + ' |')
print('| ' + str('1') + ' |')
print('| ' + str('1.1') + ' |')
print('| ' + str('abc') + ' |')
print('| ' + str(True) + ' |')


# chr 函数
# 将一个数字转换成字符
print(chr(48))  # '0'
print(chr(65))  # 'A'
print(chr(97))  # 'a'

# ord 函数
# 转换一个字符转换对应的数字编码
print(ord('0'))
print(ord('A'))
print(ord('a'))


