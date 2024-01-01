'''
定义字典
'''

d = {}  # dictionary -> dict
print(d)
print(type(d))

# 理论，所以不可变的类型都可以做为key，
# 只要是可hash的的对象都 可以做为key
# key一般情况下使用字符串类型的数据充当，
d = {1: 'one', '2': 'two'}
print(d)

d = {'one': '星期一', 'two': '星期二', 'three': '星期三'}
print(d)

