#!/usr/bin/env python
# encoding: utf-8
import threading
class FifoQueue(object):

    def __init__(self, max_size=100):
        self.max_size = max_size
        self.lock = threading.Lock()

    def enqueue(self, obj):
        with self.lock:
            if len(self.queue) >= self.max_size:
                raise Exception("queue full")
            self.queue.append(obj)

    def dequeue(self):
        with self.lock:
            if len(self.queue) == 0:
                raise Exception("queue empty")

            obj = queue[0]
            self.queue = self.queue[1:]

        return obj

if __name__ == "__main__":
    q = FifoQueue()
    q.enqueue(1)
    print q.dequeue()
