#test_coroutine.py
def product(c):
    #启动生成器
    c.send(None)
    n=0
    while n<5:
        n= n+1
        print('[PRODUCT] product %s ' % n)
        d=c.send(n)
        print('[PRODUCT] consumer %s' % d)
        
def consumer():
    r=''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] consumer %s '% n)
        r = '200K'
    c.close()

c=consumer()
product(c)


def h():
    print('Wen Chuan')
    m = yield 5
    print(m)
    d = yield 12
    print('We are together!')

c = h()
m=c.send(None)#c.__next__() python3.x以前用 c.next()
m=c.send('Fighting')#yied 5 表达式被赋予了 'Fighting'
while True:
    try:
        d=c.send(12)
        print(d)
    except Exception as e:
        print(e.value)
        break
        print(m,d)

#斐波那契
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'

for n in fib(10):
    print(n)

#杨辉三角
def tringles():
    N = [1]
    while len(N)<10:
        yield N
        N.append(0)
        N=[N[i-1]+N[i] for i in range(len(N))]
#[1,0]
#N[-1]+N[0]=0+1=[1]
#N[1-1]+[1]=1+0=[1]
#[1,1]
#[1,1,0]
#N[-1]+N[0]=0+1=[1]
#N[1-1]+N[1]=1+1=[2]
#N[2-1]+N[2]=1+0=[1]
#N[1,2,1]
for i in tringles():
    print(i)