#!/usr/bin/env python3
# by ysan

'''
    python 类（class）的运用
    其实self,就是实例本身！你实例化时python会自动把这个实例本身通过self参数传进去
    __init__()叫做初始化方法(或构造方法)， 在类被调用时，这个方法(虽然它是函数形式，但在类中就不叫函数了,叫方法)会自动执行，进行一些初始化的动作
    类变量的用途，大家共用的属性，节省内存开销
    __del__()在实例释放、销毁的时候自动执行的，通常用于做一些收尾工作，如关闭一些数据库连接，打开的临时文件
    私有方法，私有属性 在变量名前面加两个下划线
    多继承， 构造方法只走第一个继承类的构造方法
    多继承的查询策略
        1. 广度优先 （横向的类查完，再往上一层查）     python3中用的就是广度优先继承
        2. 深度优先  (深度类查完， 再往横向查找)      python2 经典类 --> 用的是深度优先继承  新式类 --> 用的是广度优先继承
'''


class People(object):
    def __init__(self, name, age, sex, salary):
        self.name = name
        self.age = age
        self.sex = sex
        self.__salary = salary

    def say_hello(self):
        print("hello, my name is %s, I have %s years old" % (self.name, self.age))

    def go_shooping(self):
        print("My salary is %s, and I will shopping at once" % self.__salary)

    def __ge_salary(self):
        return self.__salary

    def __del__(self):
        print("bye bye %s " % self.name)


class Man(People):
    def __init__(self, name, age, sex, salary, money):
        People.__init__(name, age, sex, salary)
        self.money = money
        print("%s birthday has money %s" % (self.name, self.money))

    def sleeping(self):
        print("Man go to sleeping")

    def say_hello(self):
        People.say_hello(self)
        print("Man say hello")


class Woman(People):
    def __index__(self, name, age, sex, salary, find):
        super(Woman, self).__index__(name, age, sex, salary)
        self.find = find

    def say_hello(self):
        super(Woman, self).say_hello()
        print("Woman say hello")


p1 = People('ysan', '25', 'm', '7000')
p1.say_hello()
p1.go_shooping()