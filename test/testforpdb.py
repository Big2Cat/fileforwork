#!/usr/bin/env python
# encoding: utf-8
'''
import pdb
a = 'aaa'
pdb.set_trace()
b = 'bbb'
c = 'ccc'
final = a + b + c
print final
'''

import pdb

def combine(s1, s2):
    s3 = s1 + s2 + s1
    s3 = '"' + s3 + '"'
    return s3
a = 'aaa'
pdb.set_trace()
b = 'bbb'
c = 'ccc'
final = combine(a,b)
print final

