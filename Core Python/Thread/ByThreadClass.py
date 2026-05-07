import threading
import time
from threading import *


class Hi(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        for i in range(1, 11):

            print(self.name, i)


t1 = Hi('abc')
time.sleep(12)
t2 = Hi('xyz')

t1.start()
t2.start()
