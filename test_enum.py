# -*- coding: utf-8 -*-
from enum import Enum,unique

@unique
class Weekday(Enum):
    Sum = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
day=Weekday.Mon
print (day)
print(Weekday['Wed'])
print(Weekday['Wed'].value)

for name,member in Weekday.__members__.items():
    print(name,'=>',member.value)

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
print(Month.Jan.value)
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)