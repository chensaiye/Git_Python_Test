#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 把第二个参数n的默认值设定为2
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name,'gender:', gender,'age:', age ,'city:', city)

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L