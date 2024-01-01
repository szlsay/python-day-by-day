'''
字符串的遍历
遍历：依次取到字符串中的每一个字符
'''


s = 'Hello World'

# 遍历方式一 for-in
for c in s:
    print(c, c.upper())

print('*' * 20)

# 遍历方式二 - for-in-range-配合下标

# len() 函数  是 length 的简写， 用来获取参数的长度（元素个数）
length = len(s)
for i in range(0, length):
    c = s[i]
    print(c, c.upper())


print('*' * 10)
# 遍历方式三 while-配合下标

i = 0
while i < length:
    c = s[i]
    print(c, c.upper())
    i += 1



# s = 'ab'cd'ef'
# s = 'ab\'cd\'ef'
# s = 'ab"cd"ef'
# s = 'ab """cd""" ef'
s = 'ab \'''cd''\' ef'

sql = '''select * from table while name = "tom"''';
print(s)
