'''
格式 化字符串
'''

print(1)
print(1,2,3,4)

a = 1
b = 2.1123
c = 'hello'
s = 'a = %d b = %f  c = %s' % (a,b,c)

s += ' -- world'

print(s)

s = f'a = {a} b = {b} c = {c}'
print(s)

s = 'a = {0:5d} b = {1:.2f} c = {0}'.format(a,b,c)
print(s)