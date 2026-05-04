# import threading
# from threading import *
#
#
# def hello():
#     for i in range(15):
#         print(" Hello ", i)
#
#
# def hii():
#     for i in range(15):
#         print(" hii ", i)
#
#
# t1 = threading.Thread(target=hello)
# t2 = threading.Thread(target=hii)
#
#
# t1.start()
# t2.start()

import threading
from threading import *


class Hi(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("hello")
        for i in range(1, 11):
            print(self.name, i)



t1 = Hi('abc')
t2 = Hi('xyz')

t1.start()
t2.start()