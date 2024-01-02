'''
os 模块
	rename(）
	remove()
	mkdir()
	getcwd()
	chdir()
	listdir() 掌握
	rmdir()
'''

# 导入 os 模块
# os -> operator system  -> 操作系统
import os

# rename 重命名
# os.rename('a.txt','b.txt')

# mkdir 创建目录  make directory
# 如果当前目录 存在，会报错
# os.mkdir('test_dir')


# getcwd 获取当前工作目录  get current work directory
cwd = os.getcwd()
print(cwd)

# listdir () 获取当目录下的文件列表
file_list = os.listdir('.')
print(file_list)
for file in file_list:
    print(file)

print('*' * 10)

# chdir() 改变当前目录 到指定 的路径 上去。 change directory
os.chdir('day06')
print(os.getcwd())
print(os.listdir('.'))


# remove() 删除一个文件
# os.remove('aaa.txt')


# rmdir() 删除一个文件夹 remove directory
# os.rmdir('PycharmProjects/Day06/test_dir')
# 当目录 不为空，不能删除
os.rmdir('b')
