'''
列表 的排序和逆序
'''

cl = [9,2,5,7,1,8,4,3,0,6]

print(cl)
# 排序 默认升序排序（从小到大）
print(cl.sort())
print(cl)


cl = [9,2,5,7,1,8,4,3,0,6]
# 降序排序 （从大到小）
cl.sort(reverse=True)
print(cl)


# 逆序
cl = [9,2,5,7,1,8,4,3,0,6]

# 逆序是直接将原列表中的顺序进行逆转
cl.reverse()
print(cl)



# 实现列表逆序方法
def reverse_list(cl):
    # 定义一个空列表
    ret_l = []
    i = len(cl) - 1
    while i >= 0:
        ret_l.append(cl[i])  # s += c
        i -= 1

    return ret_l

print(reverse_list(cl))


'''
l = [1,2,3,4,5]
l[0]
l[4]
l = [5,2,3,4,1]
l[1]
l[3]
l = [5,4,3,2,1]





'''

