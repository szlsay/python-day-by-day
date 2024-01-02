'''
可变参数的的二次传递
'''


def show(a,*args,**kwargs):
    print(a)
    print(args)
    print(*args)
    display(*args) # *arsg 手动解包


def display(a,b,c,d):
    print(a,b,c,d)


show(1,2,3,4,5)