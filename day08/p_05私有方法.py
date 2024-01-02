'''
私有方法的使用
'''

class ThunderBird(object):

    # 实现一个初始方法，用来保存下载任务
    def __init__(self):
        self.__list = []

    # 实现一个公有的方法，用来添加任务
    def add_task(self,url):
        self.__list.append(url)
        # 在类的内部，直接 访问私有方法
        self.__download_data(url)


    # 核心代码 ，用来下载数据的算法
    def __download_data(self,url):
        print(f'通过地址 {url} 下载数据中。。。。')


# 测试
tb = ThunderBird()
# 通过一个公有方法，间接 访问的了对象的私有方法，下载数据
tb.add_task('http://www.dytt88.net/复联4.mp4')

# 私有方法在类的外部是不能拼接访问的。
# tb.__downoad_data('http://www.dytt88.net/复联4.mp4')




