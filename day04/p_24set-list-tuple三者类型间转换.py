'''
set-list-tuple三者类型间转换
'''

s = 'hello'

l = list(s)
print(l)

print(set(l))

print(set(s))

l1 = str(l) # __str__
print(l1,'-----',type(l1))
print(''.join(l))
