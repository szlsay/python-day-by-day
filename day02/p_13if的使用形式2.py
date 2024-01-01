'''
if 的使用格式
'''

def is_net(age):
    if age >= 18:
        print('可以上网')
    else:
        print('年龄不够，上什么网，滚去学习')



age = int(input('请输入你的年龄 ：'))
is_net(age)
