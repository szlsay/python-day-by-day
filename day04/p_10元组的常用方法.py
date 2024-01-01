'''
元组的常用 方法
'''

t = (1,2,3,4,55,5,5,6,6,2,3,2)

# 提示中方法名前面的 m 表示 是一个方法， method
print(t.count(2))
print(t.index(2))
print(t.index(2,3,5)) # ValueError: tuple.index(x): x not in tuple

