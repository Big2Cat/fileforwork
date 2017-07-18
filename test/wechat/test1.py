#!/usr/bin/env python
# encoding: utf-8

from wxpy import *
robot = Robot(console_qr=2)

@robot.register(except_self=False)
def just_print(msg):
    print(msg)
    print(type(msg))
    #with open('msglog.txt','a+') as f:
    #    f.write(msg.text+'\n')
    if msg.type is TEXT:
        with open('msglog.txt','a+') as f:
            f.write(msg.text+'\n')
    else:
        with open('msglog.txt','a+') as f:
            f.write(msg.type+'\n')
robot.start()

