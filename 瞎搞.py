# !/usr/bin/env/python
# _*_coding:utf-8 _*_
# author:LiangJianfei

'''
def mul():
    return [lambda x:i*x for i in range(4)]

print([m(2) for m in mul()])


# 使用装饰器创建单利模式；

def Singleton(cls):

    instance = {}

    def wrapper(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return wrapper

@Singleton
class Foo(object):
    pass

foo1 = Foo()
foo2 = Foo()

print(id(foo1))
print(id(foo2))



# 使用基类
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Singleton, cls).__new__(cls,*args,**kwargs)

        return cls._instance

class Foo(Singleton):
    pass

foo1 = Foo()
foo2 = Foo()

print(id(foo1))

# 使用元类创建

class Sington(type):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
           cls._instance = super(Sington, cls).__call__(*args,**kwargs)
        return cls._instance


class Foo(object):
    __metaclass__ = Sington


foo1 = Foo()
fo2 = Foo()

print(id(foo1))

print("*"*30)

class DOG:
    pass

dog1 = DOG()
dog1.color = "red"
print(dog1.__class__)
dog2 = dog1.__class__()
print(dog2.__class__)

print(isinstance(dog1,DOG))

print(hasattr(dog1,'color'))

print("*"*30)

def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print ("list1 = %s" % list1)
print ("list2 = %s" % list2)
print ("list3 = %s" % list3)

print("*"*30)

list = [[]] * 5
print(list)


list[0].append(10)
print(list)

print("*"*30)
list = [ 1 , 3 , 5 , 8 , 10 , 13 , 18 , 36 , 78 ]
print(list[::2])

print([x for x in list[::2] if x % 2 == 0])

print("*"*30)

class DefaultDict(dict):
    def __missing__(self, key):
        return

d = DefaultDict()
d['florp'] = 127
print(d['florp'])


print("*"*30)


import pymysql
# 创建于数据库连接的对象：

db = pymysql.connect(host="localhost",user="root",password="123456",database="dict")

# 创建游标对象：
cursor = db.cursor()

# 利用游标对象的execute()方法执行SQL命令
# find = cursor.execute("show tables;")
# print(find)

# 提交到数据库执行



# db.commit()

try:
    sql_select  = "select * from word limit 10;"
    cursor.execute(sql_select)
    data1 = cursor.fetchone()
    print(data1)
    data2 = cursor.fetchmany(3)
    print(data2)
    for u in data2:
        print(u)
    data3 = cursor.fetchall()
    print(data3)
    for u in data3:
        print(u)

except:
    pass



cursor.close()
db.close()
'''

# import hashlib
# s1 =  hashlib.sha1()
# pwd = input("--》")
# s1.update(pwd.encode('utf8'))
# pwd2 = s1.hexdigest()
# print(pwd2)

# 连接数据库的模块
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column,Integer,String
#
# engine = create_engine("mysql+pymysql://root:123456@localhost/aa",encoding = "utf-8")
# # 生成一个ORM基类
# base = declarative_base()
# class User(base):
#     __tablename__ = "t123"
#     id = Column(Integer,primary_key=True)
#     name = Column(String(20))
#     adde = Column(String(20))
#
#
# base.metadata.create_all(engine)

# 发送端
from socket import *
import time
s = socket()
s.bind(("",8888))
s.listen(5)
c,addr = s.accept()
print("c-->",addr)
f = open('img.jpg','rb')
s.send('img.jpg'.encode())
time.sleep(0.1)


while True:
    data = f.read(1024)
    if not data:
        break
    c.send(data)

f.close()
c.close()
s.close()

# 接受端
from socket import *
s =socket()
s.connect(("127.60.40.181",8888))
filename = s.recv(1024).decode()
f = open(filename,'wb')


while True:
    data = s.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
s.close()

'''
接受http请求
查看http请求
返回一个网页给客户端

'''

from socket import *
import time
s =socket()
s.bind(('0.0.0.0',9999))
s.listen(5)
# 将IO事件设置为非阻塞
s.setblocking(False)


# 设置超时检测
s.settimeout(3)


while True:
    print("--?")
    try:
        c,addr  = s.accept()
    except:
        time.sleep(1)
        print(time.ctime())
        continue
    print("connect from ",addr)

    c.close()

s.close()
































