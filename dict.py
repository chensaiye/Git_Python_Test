#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list 使用实例
classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.append('Adam')     #追加元素到末尾
print('classmates =', classmates)  
classmates.insert(1, 'Jack')  #把元素插入到指定的位置
print('classmates =', classmates)
classmates.pop()              #删除list末尾的元素
print('classmates =', classmates)
classmates.pop(1)             #删除list指定位置的元素
print('classmates =', classmates)

list_test = ['Apple', 123, True]
print('list_test is', list_test)

# 2维list
s = ['python', 'java', ['asp', 'php'], 'scheme']
print('s is', s)

# 2维list
p = ['asp', 'php']
L = ['python', 'java', p, 'scheme']
print('L is', L)
p[1] = 'C++'
print('L is', L)

#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Bob']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

# dict 使用实例
# dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度
# 如果key不存在，dict就会报错,通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85,
    'Adam': 'older'
}
print( d['Bob'])
print( d.get('Michael'))
print( d.get('Adam'))
print( d.get('Thomas'))

print( d.get('Michael',-1))
print( d.get('Thomas',-1))

print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key
# 要创建一个set，用{x,y,z,...}列出每个元素
s1 = {1, 1, 2, 2, 3, 3}
print(s1)
s2 = {2, 3, 4}
print(s1 & s2)
print(s1 | s2)

s3 = {3,2,1}
print(s3)

s4 = {4,1,0}
print(s4)