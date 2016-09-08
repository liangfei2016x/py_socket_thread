import os
import glob
import io
import sys    
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
g=glob.glob(r'..\My Documents\Downloads\b\*.png')
print(g)
a=os.path.abspath(__file__)
print(a)
b=os.path.dirname(__file__)
print(b)
c=os.path.basename(__file__)
print(c)

#c=[]
#for name  in b:
#    namelist=os.path.basename(name)
#   c.append(namelist)
#    print()
"""    
a=os.listdir(r'D:\My Documents\Downloads\b')
print(b)
for img in a:
    with open(r"D:\My Documents\Downloads\b\\"+img,'rb') as f:
        print(f.read())
"""