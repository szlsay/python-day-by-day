'''
break 用来中断循环
'''


def test_func():
    i = 1
    print('enter loop')
    while i <= 100:
        print(i)
        if i % 2 == 0:
            break
        i += 1
        # break
    print('exit loop')





# break  #SyntaxError: 'break' outside loop

test_func()