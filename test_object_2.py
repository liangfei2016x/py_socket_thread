#test_object_2.py
class Date_test(object):
    """docstring for Data_test"""
    day = 0
    month = 0
    year = 0

    def __init__(self,day,month,year, *arg):
        self.day = day
        self.month = month
        self.year = year
    @classmethod
    #classmethod用来指定一个类方法，没有此参数指定的类的方法为实例方法
    def date_int2str(cls,day,month,year):
        date1 = cls(str(day), str(month), str(year))
        return date1
    
    @staticmethod
    #类的静态方法，可以直接用类名调用 不用实例化
    def int2str(*args):
        day,month,year=map(str,args)
        print(day+'-'+month+'-'+year)


    def out_date(self):
        print(self.day+'-'+self.month+'-'+self.year)

if __name__ == '__main__':
    """
    在Date_test类里面创建一个成员函数，前面用classmethod装饰，他的作用有点像静态类，跟静态类不一样的是
    他可以传入一个当前类作为第一个参数
    """
    #t = Date_test.date_int2str(2016,8,12)
    Date_test.int2str(2016,8,12)
