#!/usr/bin/env python
# encoding: utf-8

import datetime
import time


time_today = datetime.datetime.now()

def time_handler(n):

    time_delta = datetime.timedelta(days=-n)

    time_next = time_today+time_delta
    print time_next.strftime("%Y-%m-%d")


for i in range(100):

    time_handler((i+1)*31)
    time.sleep(2)

