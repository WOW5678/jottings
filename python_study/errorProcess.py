# -*- coding:utf-8 -*-
#理解Python的错误处理机制

#用try来执行某段代码，如果执行出错，则后续代码不会被执行，而是直接跳至错误处理代码处，即except语句块
#执行完except后，如果有finally语句块，则执行finally,至此，执行完毕
try:
    print('try....')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('Except:',e)
finally:
    print('finally....')
print('End')

#错误可能有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理
print('############################################################')
try:
    print('try...')
    r=10/int('a')
    print('result:',r)
except ValueError as e:
    print('ValueError:',e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:',e)
#如果没有错误发生，可以在except语句后面加上一个else,当没有错误发生时，就会执行else语句
else:
    print('no error.')
finally:
    print('finally....')
print('END')

#在使用except时应该注意，它不但捕获该类型的错误，还把其子类也一网打尽
#UnicodeError永远也捕捉不到，因为它是ValueError的子类，已经被ErrorValue捕获
# try:
#     foo()
# except ValueError as e:
#     print('ValueError')
# except UnicodeDecodeError as e:
#     print('UnicodeError')

#记录错误
#如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也就结束了，既然我们能捕获错误，就可以把错误堆栈打印出来，
#然后分析错误原因，同时，让程序继续执行下去
print('##################################################################')
import logging
def foo(s):
    return 10/int(s)
def bar(s):
    return foo(s)**2
def main():
    try:
        bar(0)
    except Exception as e:
        logging.exception(e)
main()
print('End')

#抛出错误
print('############################################################')
print('###############################################################')
class FooError(ValueError):
    pass
def foo(s):
    n=int(s)
    if n==0:
        raise FooError('invalid value:%s'%s)
    return 10/n
foo('0')