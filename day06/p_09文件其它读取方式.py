'''
文件其它 读取方式

'''
# 以行的形式读取文件

# 打开文件
file = open('day06/b.txt','r')

# 以行读取 readline()
# while True:
#     content = file.readline()
#     if content == "":
#         break
#     print(content)


# 以行的方式 读取整 个文件 readlines

content_list = file.readlines()
print(content_list)
for line in content_list:
    print(line)
    print(line.upper())

# 关闭文件
file.close()