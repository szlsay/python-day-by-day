'''
这个是学生模块,用来实现学生模型类的定义
保存学生信息
'''


class Student(object):

    # 定义一个初始化方法,定义学生信息属性
    def __init__(self,stu_id,stu_name,stu_age):
        self.stu_id = stu_id
        self.stu_name = stu_name
        self.stu_age = stu_age

    # 格式化对象
    def __str__(self):
        return '| ' + self.stu_id.ljust(5) + self.stu_name.ljust(10) + self.stu_age.ljust(3) + ' |'



# 当前模块的测试代码
if __name__ == '__main__':

    tom = Student('1', 'Tom', '12')
    print(tom)

