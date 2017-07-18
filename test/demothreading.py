#!/usr/bin/env python
# encoding: utf-8

import threading
import time
lista = range(0,100)

listb = []

lock = threading.Lock()

def get_number():
    lock.acquire()
    for i in lista:
        time.sleep(1)
        print i

        listb.append(i)
        time.sleep(1)
        print listb
    lock.release()
threads = []

for i in range(5):

    thread = threading.Thread(target=get_number)

    threads.append(thread)

    thread.start()

for thread in threads:

    thread.join()




