'''
不定长关键字参数
'''

def show(**kwargs):
    print(kwargs)

show(a=1)
show(a=1,b=2)
show(a=1,b=2,c=3)


# 定义一个可以接收任何参数的函数
def display(*args,**kwargs):
    print(f'args:{args}')
    print(f'kwargs:{kwargs}')


display()
display(1,2,3)
display(a=1,b=2)
display(1,2,3,4,a=1,b=2)
# display(a=1,b=2,2,3,4)

