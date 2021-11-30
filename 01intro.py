print('hello world')
x = 10
print(x)
x = x + 1
print(x)

'''basic concept'''
# to check the value of x is pos or neg
# the short cut to comment is command+/
if x > 0:
    print('it is positive')
if x < 0:
    print('it is negative')

'''convert between str and int'''
print('===str and int===')
a = 1
print(type(a))
# k = 1 + "1"
# print(k) #this is not correct, different from java
b = str(a)  # convert a number into a string
print(type(b))
c = b + " banana"
print(c)

'''list'''
print('===list===')

class1 = [1, 2, 'a', 'b', [1, 2, '3']]  # the third element itself is a list
print(class1)
length = len(class1)
print(length)  # 5

class2 = ['Stanford', 'MIT', 'Princeton']
for i in class2:
    print(i)
print(class2[1])

# we can use the word "append" to add elements into a list
score = []
score.append(88)
score.append(90)
score.append(83)
a = score[0:3]  # CAREFUL!
print(a)

# how to convert a list into a string
# take the university list 'class2' as an example

str2 = ",".join(class2)  # use a comma to connect every element in the list
print(str2)

'''dictionary'''
print('===dictionary===')
# there are two parts for every element in a dictionary
# key and the value

class3 = {'Ana':90, 'Bob':87, 'Cobb':94}
for i in class3:  # i represent the key
    print(i)
for j in class3:
    print(j + ':' + str(class3[j]))
score = class3['Bob']
print(score)  # get the score of a certain key

'''爬虫实战案例'''
key = '阿里巴巴'
url = 'http://news.baidu.com/ns?word=' + key + '&tn=news&from=news&cl=2&rn=20&ct=1'
print(url)

score = 10
year = 2018
if (score <= -10) and (year > 2010) :
    print('录入数据库')
else:
    print('不录入数据库')

'''if'''

score = 85
if score >= 80:
    print('excellent')
elif (score >= 60) and (score < 80):
    print('well')
else:
    print('work on it!')

'''for'''
for i in range(5):
    print(i)  # 循环5次，0-4

# example
title = ['title1', 'title2', 'title3']
href = ['url1', 'url2', 'url3']
for i in range(len(title)):
    href[i] = 'www.baidu.com/' + href[i]
    print(str(i+1) + '.' + title[i])  # i+1是因为它是从0开始的
    print(href[i])

'''while'''
j = 1
while j < 5:
    print(j)
    j += 1

# while True:
#     print('u cannot stop me')

'''4-1 function & model'''
print('===function & model===')

def y(x):
    print(x+1)
    print(x+10)
y(1)
y(2)
y(10)

# example
def baidu(company):
    # some code
    print(company + 'completed!')

companys = ['阿里巴巴', '百度集团', '腾讯', '京东']
for i in companys:
    baidu(i)

'''4-2 return'''

def k(x):
    return(x+1)
print(k(2))


'''review of functions'''

# str

score = 85
print('A company\'s score is ' + str(score) + ' today.')

# replace

a = '<em>bilibili</em>lalala'
a = a.replace('<em>','')
a = a.replace('</em>','')
print(a)

# strip
# help delete the blank spaces and \n 换行符

a = '    华为2020上半年总结    '
a = a.strip()
print(a)

# split

a = '2018年12月12日 08:07'
a = a.split(' ')[0]  #[0]extracts the first element in the array
print(a)

# try except

try:
    print(1 + '1')
except:
    print('the code has ERROR!')

'''python 模块 & 库'''

# way of importing

# import 库名
# or
# from 库名 import 库里的一个项目

# time

import time
print(time.strftime('%Y/%m/%d'))  # export the time of today
                                  # 2020/06/16

from datetime import datetime
print(datetime.now())  # 2020-06-16 11:25:17.829444

# requests

import requests
url = 'https://www.baidu.com/'
res = requests.get(url)
print(res.text)