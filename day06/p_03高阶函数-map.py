'''
map 函数
作用：是对参数列表中的元素做一个映射
'''

my_list = [1, 2, 3, 4, 5]

# 这个函数是为了给map的参数一进行传参
# 因为map函数需要使用这个函数来计算每一个元素的映射值 ，
# 所以该函数有且必须只能有一个参数
def f(x):
    return x ** 3

# result_list = map(f, my_list)

# 利用lambda 来替代函数进行传参
result_list = map(lambda n: n ** 4, my_list)
for i in result_list:
    print(i)


print(type(result_list))


# map实现原理
def my_map(func, c_list):
    # 定义一个新空列表 ，保存映射结果
    new_list = []
    # 遍历源列表 中的数据
    for i in c_list:
        # 调用函数计算映射值 ，并保到新列表中
        # new_list.append(func(i))
        n = func(i)
        new_list.append(n)

    return new_list


print('*' * 10)
result_list = my_map(lambda n: n ** 4, my_list)
for i in result_list:
    print(i)


