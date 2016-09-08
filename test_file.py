import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
#读文件 二进制的用 rb
with open(r"D:\fuxi\一段文字.txt",'r',encoding='gbk',errors='ignore') as f:
    #print(f.readlines())
    for line in f.readlines():#readlines()返回一个list
        print(line.strip())

with open(r"D:\fuxi\test.txt",'w') as f:
    f.write("第一次，它把成功寄希望于侥幸；")
f.close()
#从内存中读数据
#str
from io import StringIO
f=StringIO()
f.write('Hello')
print(f.getvalue())
#bytes
from io import BytesIO
f=BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

import os
print(os.environ.get('path'))
print(os.path.abspath('.'))
print(os.path.split(r'D:\fuxi\test_file.py'))