'''
循环后面有else的场景
'''

def test_func1(s):
    for c in s:
        print(c)
        if c == 'A':
            print('字符串里有A')
            break
    else:
        print('没有A')


def test_func2():
    i = 0
    while i < 10:
        print(i)
        if i == 50:
            print('中断结束循环')
            break
        i += 1
    else:
        print('程序没有被中断，正常结束')



test_func1('helAlo')
test_func2()

