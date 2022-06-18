import timeit

from setuptools import setup


def fun1(n):
    return [str(num) for num in range(n)]


def fun2(n):
    return list(map(str, range(n)))


stmt1 = '''
fun1(1000)
'''


setup1 = '''

def fun1(n):
    return [str(num) for num in range(n)]

'''

print(timeit.timeit(stmt1, setup1, number=1000))


stmt2 = '''
fun2(1000)
'''


setup2 = '''

def fun2(n):
    return list(map(str, range(n)))

'''

print(timeit.timeit(stmt2, setup2, number=1000))
