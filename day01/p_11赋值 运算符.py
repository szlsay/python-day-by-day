'''
赋值 和复合赋值 运算符

'''

# =
# 将等号右边的数据 赋值 到等号左边的变量中
a = 1
b = 'hello'


# 复合赋值 运算符
# 作用，简化 操作

a = 2
b = 3
a += b
print(a,b)

# 简化操作，等效于展开，但并不展开

a = 2
b = 3
a *= b + 5
print(a)