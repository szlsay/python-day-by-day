'''
列表推导 式
创建一个具有一百个数字的列表
'''

# c_l = []
# for i in range(100):
#     c_l.append(i)


# 使用列表推导式来完成列表的创建
c_l = [i for i in range(100)]
# c_l = [x for i in range(100)] # 注意，表达的变量使用要和循环中的变量一致

print(c_l)
print(len(c_l))


# 列表推导 式，带条件的
# 实现列表 中所有的值 都 是3的倍数

c_l = [x for x in range(1,101) if x % 3 == 0]
print(c_l)


# 创建一个列表 ，列表 中的每个元素都 是具有两个值 的元组
# c_l = [(x,x) for x in range(10)]
# c_l = [(x,) for x in range(10)]
c_l = [(x,y) for x in range(10) for y in range(3)]
print(c_l)


