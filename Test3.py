class Test3(object):
    """description of class"""

#try, except,finallly
#Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：
#https://docs.python.org/3/library/exceptions.html#exception-hierarchy

def dosome():
    try:
        print('try...')
        r = 10 / 0
        print('result:', r)
    except ZeroDivisionError as e:
        print('except:', e)
    except ValueError as e:
        print("except valueeROR")
    except Exception as e:
        logging.exception(e) #捕获所有，内置的logging模块打印日志
    finally:
        print('finally...')
    print('END')

#定义一个exception
class FooError(ValueError):
    pass

#抛出异常
#raise FooError("error info")


#使用断言
#assert n != 0, 'n is zero!'