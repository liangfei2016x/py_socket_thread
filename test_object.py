#coding=utf-8
import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def say(self):
        print('Hello %s' % self.name)

    def say_twice(per):
        per.say()
        per.say()


class Student(Person):
    def __init__(self,name,age,hight,weight):
        self.name=name
        self.age=age
        self.hight=hight
        self.weight=weight

    def get_age(self):
        if 0<self.age<18:
            return '未成年'
        elif self.age<30:
            return '青年'
        elif self.age<50:
            return '中年'
        else:
            return '老了'

    def print_student(self):
        print('%s,%s,%s,%s'%(self.name,self.age,self.hight,self.weight))

class Animal(object):
    """docstring for Animal"""
    #属性私有
    def __init__(self,name,color):
        self.__name=name
        self.__color=color
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
        
        
if __name__ == '__main__':
    tom=Person('tom',11)
    print(tom.age)
    tom.score=99
    print(tom.score)
    dell=Student('dell',25,175,130)
    print(dell.name)
    dell.say()
    dell.print_student()
    dell.say_twice()
    print(dell.get_age())
    cat=Animal('cat','red')
    print(cat.get_name())
    cat.set_name('Dog')
    print(cat.get_name())