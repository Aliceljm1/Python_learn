from functools import reduce

#高阶函数
#函数作为参数
def add(x,y,f):
    return f(x)+f(y)
print(add(1,-5,abs))

#破坏一个函数名
#import builtins; builtins.abs = 10
#这样之前的函数abs就指向了一个对象10，

#map/reduce 的支持
def f(x):
    return x*x
r=map(f,[1,2,3,4])
outinfo=list(r) #r是惰性Iterator，需要主动调用
print(r)
print(outinfo)

#讲一个数字数组的元素转换为字符串
a=list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def add(x,y):
    return x+y
b=reduce(add,[1,2,3]) #求和，

#讲一个序列转换为整数
iarray=[1,2,5,6]
def change(x,y):
    return x*10+y
c=reduce(change,iarray)#得到整数1256
print(c)

#将一个字符串转换为int类型的值
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn,map(char2num,s))
#先将char2num运用到s上，返回每一个字符转换的数字，然后合并数字

print(str2int('123123'))

#lambda 函数-匿名函数，最简单的输出输出

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))



#filter函数
def is_odd(n):
    return n % 2 == 1

list_ji= list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))


#sorted函数
array=[-5,1,2,6,7]
sort_list=sorted(array, key=abs, reverse=True) #key为排序函数,reverse是否倒序排列

print(sort_list)



#闭包和内部函数
#直接返回一个函数，
def lazy_sum(*args):
    def sum():
        ax=0
        for n in args:
            ax=ax+n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print(f())


#装饰器Decorator,在代码运行期间动态的增加函数的功能，

def dosome(n):
    print(n)

#定义log函数，函数执行之前执行某个代码
def log(func):
    def wrappers(*args,**kw):
        print('call %s:'%func.__name__)
        return func(*args,**kw)
    return wrappers

nfunc=log(dosome)
print(nfunc("ljm"));






#偏函数，将某个函数的参数固定住，直接调用
import functools

dosome2=functools.partial(dosome,kw="a")

from Student import *

t=Timer()
testRun(t)


