'''
filter 过滤函数
'''

my_list = ['123','234','abc','@#$','  ','abc234','132abc']

# 过滤出所有的数字字符串

num_list = filter(lambda s: s.isdigit(), my_list)
print(num_list)

for s in list(num_list):
    print(s)

