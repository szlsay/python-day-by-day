'''
函数的默认值 参数
'''

def show(a=0,b=0):
    print(f'a:{a},b:{b}')
    print(a + b)


show()
show(1)
show(1,2)


# 使用默认值 参数时，需要注意：
# 在默认值 参数的右侧，不能再出现没有默认值 参数


def display(a,b=0,c=0):
    print(a,b,c)

display(1)
display(1,2)
