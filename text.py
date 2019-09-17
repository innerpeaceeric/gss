"""
测试用例
"""

# 计算
import time
from multiprocessing import Process
import threading


def count(x,y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1



# test()


# io
def io():
    write()
    read()

def write():
    f = open('test','w')
    for i in range(1700000):
        f.write("Hello world\n")
    f.close()

def read():
    f = open('test')
    lines = f.readlines()
    f.close()

def test(fun):
    a = time.time()
    for i in range(10):
        fun(1,1)
    print(time.time()-a)

# test(count)
a = time.time()
jobs = []
for i in range(10):
    p = Process(target=io)
    jobs.append(p)
    p.start()
for i in jobs:
    i.join()
print(time.time()-a)  #2.0

# a = time.time()
# jobs = []
# for i in range(10):
#     t = threading.Thread(target=io)
#     jobs.append(t)
#     t.start()
# for i in jobs:
#     i.join()
# print(time.time()-a)  # 4.5s

# a = time.time()
# jobs = []
# for i in range(10):
#     t = threading.Thread(target=count, args=(1,1))
#     jobs.append(t)
#     t.start()
# for i in jobs:
#     i.join()
# print(time.time()-a)  # 5.8



