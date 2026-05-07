# # import threading
# # from threading import *
# #
# #
# # def hello(name):
# #     for i in range(1, 11):
# #         print('hello:', name, i)
# #
# #
# # def hi(name):
# #     for i in range(1, 11):
# #         print('hi:', name, i)
# #
# #
# # t1 = threading.Thread(target=hello, args=('abc',))
# # t2 = threading.Thread(target=hi, args=('xyz',))
# #
# # t1.start()
# # t2.start()
#
#
# import threading
# # from threading import *
#
#
# def hello(name):
#     for i in range(1, 10):
#         print("hello:", name, i)
#
#
# def hii(name):
#     for i in range(1, 15):
#         print("hii", name, i)
#
#
# t1 = threading.Thread(target=hello, args=('xyz',))
# t2 = threading.Thread(target=hii, args=('abc', ))
#
# t1.start()
# t2.start()
#
#

import threading
from threading import *


def hello(name):
    for i in range(1, 11):
        print("hello", name, i)


def hii(name):
    for i in range(1, 11):
        print("good morning", name, i)

t1=threading.Thread(target=hello,args=('Nitin',))
t2=threading.Thread(target=hii,args=('Nitin',))

t1.start()
t2.start()
