'''
私有属性
'''

'''
java:
 public  公有
 private 私有
 protected 保护
 
python:
    定义属性时，没有任何修饰 的都 是公有的
    如果在属性或方法前，加两个下划线前缀，那么这个属性或方法，python 解释 器就认为是私有的
'''


class Account(object):
    def __init__(self,name,balance):
        # 定义了两个公有属性，这两个属性在类的外部也是可以访问的
        # self.name = name
        # self.balance = balance

        # 因为公有的属性破坏程序的封装性，导致数据不安全，所以将属性定义私有的
        # 当一个类中的属性或方法，全部是私有时，这个类是无意义 的
        self.__name = name
        self.__balance = balance

    # 私有属性定义好后，可以保证数据 的访问安全
    # 但是还有需求去属性进行访问，可以通过 公有接口方法进行间接 访问
    # 一般对私有属性会提供 一种 称为 存取器方法的 公有方法
    # set/ get方法
    # set_属性名  get_属性名

    # 因为帐户名一旦确认后无需修改，所以可以不提供 set 方法
    # def get_name(self):
    def get_username(self):
        return self.__name


    # 给余额提供 存取方法
    def set_balance(self,new_balance):
        if isinstance(new_balance,int):
            self.__balance = new_balance
        else:
            print('不能存玉皇大帝的钱')

    def get_balance(self):
        return self.__balance




    # 定义一个查看信息的方法
    def show_info(self):
        # # 在类的内部，访问对象的公有属性
        # print(self.name + ' 有 ',self.balance ,'元')

        # 在类的内部，访问对象的私有属性
        print(self.__name + ' 有 ', self.__balance, '元')



jack = Account('JackMa',9999999)
# 在类的外部，访问对象的公有属性
# print(jack.name)
# print(jack.balance)
#
# jack.name = '郭'
# print(jack.name)
# print(jack.balance)

# 访问私有属性
# print(jack.__name)
# print(jack._Account__name)  # 只是让你了解私有的原理，但是不能这么使用

# 通过 接口方法来访问私有属性
print(jack.get_username())
print(jack.get_balance())

jack.set_balance(88888888)
print(jack.get_balance())
# jack.set_name('郭')
# print(jack._Account__username)

jack.set_balance('十个亿')
money = jack.get_balance()
print(money)
money -= 999999999

