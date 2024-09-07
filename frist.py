print('Python,hello world')

print('Hi, %s, you have $%d.' % ('Michael', 1000000))

print('%.2f' % 3.1415926)

print('''line1
... line2
... line3''')

print(10/3)
print(10//3)
print(10%3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Bob!'''
print(s4)


# for 使用实例
sum = 0
for x in range(101): # sum from 0 to 100
    sum = sum + x
print(sum)

names = ['Michael', 'Bob', 'Tracy',]
for name in names:
    print(name)

x = 0
# for 使用实例
for x in range(len(names)):
    print('Hello',names[x])

x = 0
# while 使用实例
while x < len(names):
    print('Hi',names[x])
    x = x+ 1    # 需更新x值
# while break 使用实例
n = 1
while n <= 10:
    if n > 5: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
# while continue 使用实例
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
print('END')


#数据转换
print(int('123'))
print(int(12.34))
print(float('12.34'))
print(str(1.34))
print(1.34)
print('1.34')
print(str(100))
print(bool(1))
print(bool(0))
print(bool(10))