'''
格式 化字符串并输出
'''

# 占位符形式的字符串

# 1
a = 10
print('现在要打印一个数字，值是 %d' % a)

# 2
print('name: %s age: %d' % ('Tom', 12))

# 占位符的常用 格式
print('%d' % 1)
print('%5d' % 1)
print('%05d' % 1)
print('%-5d' % 1)
print('%3d' % 12345)

print('%.2f' % 3.1415926)
print('%.3f' % 1)


# f-string
name = 'Tom'
age = 11
print(f'name: {name} age：{age} score: {99}')

s = f'name: {name} age：{age} score: {99}'
print(s)

