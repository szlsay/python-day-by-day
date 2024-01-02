'''
函数递归调用
函数在函数体内，又调用 了自己，这种 形式就是递归调用
'''

# def func():
#     print('Func Start..')
#
#     func()
#     print('Func Stop..')
#
#
# func()

# 求阶乘
# 5！ = 1 * 2 *３ * 4 * 5

# factorial 阶乘
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)



print(factorial(3))
# print(factorial(5))

'''
factorial(5) -> 5 * factorial(4)            -> reutrn 5 * 24  -> 120

                -> 4 * factorial(3)         -> return 4 * 6
                
                    -> 3 * factorial(2)     ->  reutrn 3 * 2
                    
                        -> 2 * factorial(1)  -> return 2 * 1
                            
                            -> return 1
'''

s = 1
for i in range(1,6):
    s *= i
    print(s)

