class Student(object):
#    __slots__=('name','age','score')
    def __init__(self,name,age,score):
        self.__name=name
        self.__age=age
        self.__score=score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value<0 or value>100:
            raise ValueError('score must between 0~100!')
        self.__score=value
    def __str__(self):
        return self.__name+','+str(self.__age)+','+str(self.__score)
if __name__ == '__main__':
    s=Student('Jesscal',18,99)
#    s.name='Michael'
    print(s.__str__())
    s.score=10
    print(s.score)
#    print(s.name)
        