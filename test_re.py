import re

import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

m = re.match(r'(\w+) (\w+)(?P<sign>.*)','hello world!')
print('m.string:',m.string)#匹配时使用的文本
print('m.re:',m.re)#匹配时使用的Pattern对象
print('m.pos:',m.pos)#文本中郑州表达式开始搜索的索引
print('m.endpos:',m.endpos)#文本中正则表结束搜索的索引
print('m.lastindex:',m.lastindex)#最后一个被捕获的的分组在文本中索引
print('m.lastgroup:',m.lastgroup)#最后一个被捕获的的分组的别名 如果没有则返回None
print('m.group:',m.group(1,2))
print('m.group:',m.groups())#获得所有的分组字符串
print('m.groupdict():',m.groupdict())
print('m.start(group):',m.start(2))#返回指定的截取字串在string中的起始索引
print(m.end(2))#返回指定的截取字串在string中的末尾索引
print(m.span(2))#(start(group,end(group)))
print(m.expand(r'\1 \2 \3'))#获取分组 \id或者g<id> 编号从 0 开始