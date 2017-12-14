# -*-coding:utf-8 -*-
import copy
str="a"
Bytes=str.encode('utf-8');
print(Bytes)

dic={"ljm":95,"bob":50}
if(dic.get("ljm")!=-1):
    print("dic,ljm={}".format(dic.get("ljm"))); #字符串的format函数
dic.pop("bob")#删除指定元素

set1=set([0,1,1,2,3])
set1.add(5);
set1.remove(3)
print(set1) #无序无重合的

#函数
def nop():
    pass#定义一个空函数

#函数的参数校验
def max_v(a,b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)): 
        return TypeError("Type error")# 增加参数判定
    return a if a>b else b
#python的三元表达式，
print(max_v(5,9))

#默认参数，#返回多个参数组成的元组
def getPoint(x,y=100): 
    return x+1,y+2  
  

point=getPoint(5,6) #point为tuple元组
print(point)

#//推断出参数类型为集合型或可变参数，如果为*nums则为可变长参数
def calc(nums): 
    sum=0
    for n in nums:
        sum=sum+n
    return sum

print(calc([1,2,3])) #封装为list调用
#print(calc(1,2,3)) #依靠可变长参数调用
nu=[1,2,3]
#calc(*nu) #将list变为一个可变长参数，等效于calc(nu[0],nu[1],nu[2])

def person(name,age,**kv): #**kv标记kv是一个dict,
    if 'city' in kv:
        pass
    else:
        print("p in ciy")

#如果要限制参数的名字需要使用：命名关键字参数
#*号之后的参数名称固定住，
def persion2(name,age,*,city,job):
    print(name,age,city,job)
persion2("a",1,city="bj",job="per") #修改为jobs则错误
#参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

#递归，
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

#fact(1000) 会导致栈内存溢出， 如何优化呢? 尾递归优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
#然并卵，依然会溢出

#列表生成：
lista=[m + n for m in 'ABC' for n in 'XYZ']
print(lista)#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ'],选循环ABC，

import os
file_folders=[d for d in os.listdir(".") if d.index("p")>=0]
print(file_folders)#当前所有的 包含字母p的文件和文件夹

#for循环生成多个变量
dd={"a":1,"b":2}
for k,v in dd.items():
    print(k,"=",v)

#生成器 generator， 使用的时候才生成，节省开销
gen=(x*x for x in range(1,10)) #定义一个生成器此时是一个计算方法的保存，没有坐任何计算
#next(gen) 可以调用
for n in gen:
    print(n)#通过for来迭代，也就是说generator是一个可迭代的对象

#打印斐波那契数列
def fib(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1
    return 'done'
#a,b=b,a+b相当于，可以理解为右值都会创建一个对象
#t = (b, a + b) # t是一个tuple
#a = t[0]
#b = t[1]

#上面的函数可以修改为一个generator， 只需要一个关键字yield
def fib(max):
    n,a,b=0,0,1
    while n<max:
        yield b
        a,b=b,a+b
        n=n+1
    return 'done'




a=[1,2,3,4,['a','b']] #原始对象
b=a #引用赋值，a,b指向同一个对象
c=copy.copy(a) #对象拷贝，只拷贝第一层
a.pop(2);#删第1个数
a.insert(2,8);#插入
d=copy.deepcopy(a) #对象拷贝，深度拷贝,所有对象内对象都copy,完全解耦

a.append(5)
a[4].append('c')
print("a=",a);
print("b=",b);
print("c=",c);
print("d=",d);

for x in range(0,10):
    print(x,end="\r\n")#换行打印

a=[[1,2],[3,4],[5,6]]
print("a={}".format(a)) #字符串方法format 输出参数

#变量的说明
#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431658624177ea4f8fcb06bc4d0e8aab2fd7aa65dd95000



