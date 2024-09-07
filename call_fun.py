#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

from MyMath import my_abs
print(my_abs(-99))

from MyMath import power
print(power(2))
print(power(2,10))

from MyMath import enroll
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

from MyMath import add_end
Str1 = add_end([1, 2, 3])
print(Str1)
Str1 = add_end()
print(Str1)


def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n 
    return sum
print(calc([1,2,3]))
print(calc((1,3,5,7)))
# print(calc())

# 可变参数 就是传入的参数个数是可变的，可以是0个、1个、2个到任意个
def calc_p(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(calc_p(1,3,5,7,9))
print(calc_p())
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
nums = [1, 2, 7]
print(calc_p(*nums))

# 关键字参数 允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        print('name:', name, 'age:', age, 'city:', kw.get('city'))
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
dict_table = {'city': 'Beijing', 'job': 'Engineer'}
person('Adam', 45, **dict_table)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person_filter(name, age, *, city, job):
    print(name, age, city, job)
#person_filter('Michael', 30)
person_filter('Jack', 24, city='Beijing', job='Engineer')
#person_filter('Jack', 24, area='Beijing', job='Engineer')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person_f1(name, age, *args, city, job):
    print(name, age, args, city, job)
person_f1('Mike', 24, city='Beijing', job='Engineer')
person_f1('Mike', 24,'man', city='Beijing', job='Engineer')
person_f1('Jack', 25, **dict_table)


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
f1(1, 2, 3)
f1(1, 2, 3, 'a')
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', 'c', x=99)

f2(1, 2, d=99, ext=None)
f2(1, 2, 3,d=100, ext=None)

arg = (3, 4, 5)
args = ('a', 'b', 'c', 'd',9)
kw = {'d': 99, 'x': '#'}
f1(*arg, **kw)
f1(*args, **kw)
kw = {'d': 88, 'x': '#'}
f2(*arg, **kw)

