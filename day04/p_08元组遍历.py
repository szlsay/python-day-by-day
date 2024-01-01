'''
元组的遍历
'''

last_name = ('张','王')
first_name = ('博','三','四')


# for-in
t = (1,2,3,4,5,'hello')
for v in t:
    print(v)


# 循环配合下标方式 一
for i in range(len(t)):
    print(t[i])


# 循环配合下标方式 二
i = 0
while i < len(t):
    print(t[i])
    i += 1

