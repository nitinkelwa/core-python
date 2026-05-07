# import threading
# import time
#
#
# def first_thread(name):
#     for i in range(1, 11):
#         time.sleep(3)
#         print(name, i)
#
#
# def second_thread(name):
#     for i in range(1, 10):
#         time.sleep(1)
#         print(name,i)
#
#
# t1 = threading.Thread(target=first_thread, args=('daemon',), daemon=True)
# t2 = threading.Thread(target=second_thread, args=('abc',))
#
# t1.start()
# time.sleep(2)
# t2.start()



import threading
import time


def firest_thread(name):
    for i in range(1,11):
        time.sleep(3)
        print("hello ",name,i)


def secon_thread(name):
    for i in range(1, 11):
        time.sleep(1)
        print("hello ", name, i)


t1=threading.Thread(target=firest_thread,args=('daemon',),daemon=True)
t2= threading.Thread(target=secon_thread,args=('rays',))


t1.start()
time.sleep(2)
t2.start()







