'''
__init__方法
该 方法会在创建 对象时自动调用 ，
并对该 对象进行初始化操作
'''

class Cat(object):
    # 实现 魔法方法 __init__ ，准备为对象初始化属性
    def __init__(self,name, age):
        print('Init Run ...',self)
        # 绑定属性时，使用 self.属性名 = 值
        self.name = name
        self.age = age


    def show(sealf):
        print(sealf.name, sealf.age)



tom = Cat('Tom',1)
print(tom)

# 使用属性
print(tom.name)
print(tom.age)

jack = Cat('Jack',2)
print(jack)
print(jack.name)
print(jack.age)


# 在调用 方法时，方法的第一个参数 self 是不用手动传参的
# 这个参数会由解释 器自动将调用 该 方法的对象传递过去
tom.show()  # self = tom
jack.show() # self = jack

# rose = Cat()



def show():
    a = 1
    print(id(a))
    return a

b = show()
print(b)
print(id(b))