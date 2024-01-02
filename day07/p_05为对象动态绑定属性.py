'''
实例 对象
'''

# 抽象一个人类

class Person(object):
    # 第一个方法
    def eat(self,food):
        print(self.name, ' 在吃',food)


    # 第二个方法
    def sleep(self,t):
        print(self.name, ' 睡了',t,'个小时')


#　实例对象
tom = Person()
jack = Person()
rose = Person()

# 为对象态动添加一个属性 name
tom.name = 'Tom'
# 动态为对象绑定属性时,给哪个对象绑定了属性,只能哪个对角有该 属性,其它对象是没有该 属性的
# 如果在方法中引用了该 属性,那么这时没有该 属性的对象,调用这个方法时,就会报错
jack.name = "Jack"
rose.name = 'Rose'



# 实例对象时，会在内存中分配一块内存空间，这个空间就是这个对象的位置，
# 然后将这个地址引用返回给对象名
print(tom)
print(jack)
print(rose)

#
# # 使用 对象来执行类中的方法
# tom.eat('饭')
tom.eat('海鲜')
tom.sleep(8)

jack.eat('土')
jack.sleep(2)

rose.eat('满汉全席')
rose.sleep(24)