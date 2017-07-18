#!/usr/bin/env python
# encoding: utf-8

exampledict = {'a':'apple','b':'banana','c':'cat','d':'dog'}
try:
    word = exampledict['e']
    print word
else:
    print exampledict['c']

