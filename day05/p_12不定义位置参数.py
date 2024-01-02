'''
不定长位置参数
'''

def my_sum(*args):
    print(args)
    s = 0
    for i in args:
        s += i
    print(s)

my_sum(1,2)
my_sum(1,2,3)
my_sum(1,2,3,4)
my_sum(1,2,3,4,5)

