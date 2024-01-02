'''
主程序文件,用来实现程序的入口
'''


# 导入学生管理模块
from student_manager import *


if __name__ == '__main__':

    # 使用学生管理类创建一个学生管理对象
    sms = StudentManagerSystem()
    # 通过start() 方法,启动程序
    sms.start()