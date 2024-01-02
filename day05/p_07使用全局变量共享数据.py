'''
使用全局变量，共享数据
'''

# 全局变量
num = 0

c_list = []

# 定义一个用来上传数据的函数
def upoad_data():
    # 如果想修改全局变量，需要声明
    global num

    num = 100
    print(num)
    c_list.append(1)

# 定义一个用下载数据的函数
def download_data():
    print(num,c_list)




# 测试
download_data()
upoad_data()
download_data()

