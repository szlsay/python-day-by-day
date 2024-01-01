'''
函数中存在多个Return语句
'''

def get_num():
    return 1
    return 2
    return 3

# print(1)
#  pirnt(2)  #IndentationError: unexpected indent


print(get_num())
