'''
字典元素的遍历
'''
# 方式 一

d = {'one': '星期一', 'two': '星期二', 'three': '星期三','haha':'周末'}

# 默认情况 下，使用for-in遍历时，会将所有的key遍历出来
for k in d:
    print(f'for-in:{k} --> {d[k]}')


# 方式二
# keys()方法
print(d.keys())
for k in d.keys():
    print(f'keys  :{k} --> {d[k]}')


# 方式三
# values() 方法
print(d.values())
for v in d.values():
    print(f'values: {v}')


# 方式 四
# items()
print(d.items())

for item in d.items():
    print(f'items: {item[0]}--》{item[1]}')

for k,v in d.items():
    print(f'item: {k}--> {v}')
    
    
# 解包
item = (1,2,3,4,5,6)
a,b,c,d,e,f = item

print(a)
print(e)