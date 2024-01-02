'''
这个模块用来实现学生管理类
主要负责学生管理的增删改查等操作的逻辑实现
'''

from student import Student


class StudentManagerSystem(object):

    def __init__(self):
        # 定义一个容器属性,用来保存所有被管理的学生
        # 容器是一个字典类型
        # 容器的元素值  学生ID: 学生对象
        self.students = {}

        # 加载数据
        self.__load_data()


    # start() 方法是用来启动该管理系统的公有接口方法
    def start(self):
        print('系统启动成功')

        # 循环执行
        while True:
            # 打印菜单
            self.__print_menu()
            # 输入要执行的id
            selecd_id = input('请输入要选择功能的ID:')

            # 判断,如果输入的ID,不在范围内,那么执行输入
            if selecd_id.isdigit():
                # 如果是数字字符串,那么转换成数字,方便后面的判断
                n = int(selecd_id)
                # 判断是否在有效范围内
                if n >= 0 and n <= 5:
                    # 执行操作方法
                    self.__operator(selecd_id)
                else:
                    print('超出功能ID范围,重新输入')
            else:
                print('输入了非法功能,请重新输入')



    # 打印菜单的方法
    def __print_menu(self):
        print("*" * 30)
        print("欢迎使用【学生管理系统】 V1.0")
        print("1.添加学生")
        print("2.显示全部")
        print("3.查询学生")
        print("4.修改学生")
        print("5.删除学生")
        print("0.退出系统")
        print("*" * 30)


    # 用来执行操作的方法
    # 实现管理的代码逻辑
    def __operator(self, selecd_id):
        print('选择了功能 ',selecd_id)
        # 在这个功能里,需要根据接收的ID来选择相应功能执行
        # 将功能的ID和字典做一个映射关系,每一个ID和函数名做为键值对保存到字典中

        method_dict = {'1': self.__add_student,
                       '3': self.__search_stu_with_id,
                       '4': self.__modify_student_with_id,
                       '2': self.__show_all_info,
                       '5': self.__remove_student_with_id,
                       '0': exit}

        # 通过接收的ID,在字典中去找到相应的方法,并执行
        method = method_dict[selecd_id]

        # 判断,有id参数的方法,通过if后代码执行
        if selecd_id == '3' or selecd_id == '4' or selecd_id == '5':
            # 输入一个要操作的学生ID,并传给相应的学生
            stu_id = input('请输入要操作的学生ID:')
            method(stu_id)
        # 所有无参的方法,都在这里执行
        else:
            # 如果功能ID是0,表示要退出程序,
            # 退出程序前先要保存数据,写入文件
            if selecd_id == '0':
                self.__save_data()

            method()




    # 添加学生的方法
    def __add_student(self):
        print('添加学生')
        # 通过输入获取学生的信息
        stu_info = self.__input_stu_info()
        # 创建一个学生对象,保存学生的信息
        stu = Student(stu_info[0], stu_info[1],stu_info[2])
        # 加到学生字典中
        self.students[stu.stu_id] = stu
        # self.students[stu_info[0]] = stu

        # print(self.students)





    # 查找学生的方法
    # 方法有个返回值,返回查找到的学生
    def __search_stu_with_id(self, stu_id):
        print(stu_id)
        # 给学生定义一个默认值为空,默认是找不到学生
        stu = None

        # 通过参数id在字典中进行判断,如果id存在,那么就通过id找到这个学生
        if stu_id in self.students:
            stu = self.students[stu_id]

            # stu = self.students.get(stu_id)

            # 显示学生信息
            self.__show_stu_info(stu)
        else:
            print(f'ID为 {stu_id} 的学生不存在')

        # 将找到的学生返回
        return stu




    # 修改学生信息
    def __modify_student_with_id(self, stu_id):
        # 打印修改学生ID
        print('要修改的学生是 ',stu_id)

        # 先查找学生
        stu = self.__search_stu_with_id(stu_id)

        # 判断,如果找到学生就修改,没找到就不修改
        if stu != None:
            # 获取新数据
            new_stu_info = self.__input_stu_info()

            # 修改
            stu.stu_id = new_stu_info[0]
            stu.stu_name = new_stu_info[1]
            stu.stu_age = new_stu_info[2]
            print('修改完成')
            self.__show_stu_info(stu)
        else:
            print('要修改的学生', stu_id, '不存在')




    # 删除学生信息
    def __remove_student_with_id(self, stu_id):
        # 调用查找 方法查询 学生
        stu = self.__search_stu_with_id(stu_id)

        # 判断如果查找到学生就删除
        if stu:
            self.students.pop(stu_id)
        # else:
        #     print('没找着')


    # 显示单个学生的信息
    def __show_stu_info(self, stu):
        print(stu)


    # 显示所有学生信息
    def __show_all_info(self):
        # 遍历 打印
        for stu in self.students.values():
            # print(stu)
            self.__show_stu_info(stu)


    # 获取学生信息的方法
    # 返回一个学生的信息
    def __input_stu_info(self):
        stu_id = input('请输入学生的ID:')
        stu_name = input('请输入学生的姓名:')
        stu_age = input('请输入学生的年龄:')
        return stu_id, stu_name, stu_age


    # 添加两个方法,用来读取数据和退出程序时保存数据
    def __save_data(self):
        print('保存数据')
        # 以行的形式来保存每一个学生的信息

        # 以写的方式打开一个文件
        file_w = open('data','w')

        # 遍历所有的学生信息
        for stu in self.students.values():
            # 将学生转换成一个学生字符串对象
            # stu_s = str(stu)
            stu_s = stu.stu_id + ' ' + stu.stu_name + ' ' + stu.stu_age + '\n'
            # print(stu_s)

            # 将学生信息组织成一个固定格式的字符串,按行写入到文件中
            file_w.write(stu_s)

        # 关闭文件
        file_w.close()


    # 加载数据
    def __load_data(self):
        print('加载数据')
        # 打开文件,并要处理文件不存在的异常
        file_r = None
        try:
            file_r = open('data','r')
        except Exception as e:
            print(e, '文件不存在')
        else:
            # 读取文件内容,按行读取
            content = file_r.readlines()

            # 遍历每一行数据
            for stu_s in content:
                split_info = stu_s.split()

                # 创建一个学生对象,然后保存到字典里
                stu = Student(split_info[0], split_info[1], split_info[2])
                # 加到字典里
                self.students[stu.stu_id] = stu
        finally:
            if file_r != None:
                file_r.close()




