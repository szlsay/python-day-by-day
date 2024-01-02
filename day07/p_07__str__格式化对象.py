'''
__str__（） 方法

'''

class Cat(object):
    def __init__(self,name, age, height):
        # 将三个属性绑定给对象
        self.username = name
        self.age = age
        self.height = height


    # 默认没有实现 __str__方法，那么会打印　<模块名．类名　object at 0x...>
    # 如果想按自己的格式 显示，需要在类中实现 该 方法
    def __str__(self):
        print('String Run ..',self.username)
        # print(self.username, self.age, self.height)
        # 该 函数必须 有一个返回值
        # 并且这个返回值 必须 是一个字符串
        #　如果需要将对象的信息按照一定的格式进行格式　化，那么可以在这里进行格式修饰　，
        # 修饰完后，可以将这个格式 化字符串返回，让str（） 方法在执行时，得到该 对象转换的字符串类型
        s = self.username.ljust(10) + str(self.age).ljust(5) + self.height.ljust(5)
        return s




tom = Cat('Tom',1,'50cm')
jack = Cat('Jack',2,'50cm')

# print(tom.username)
# print(tom.age)
# print(tom.height)

print(tom)
print(jack)


# c_lsit = list('hello')
#
# print(c_lsit)

tom_s = str(tom)
print('|' + tom_s + '|')
