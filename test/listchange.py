#!/usr/bin/env python
# encoding: utf-8

'''
class changelist(object):


    def change(self,tolist):

#        print self.tolist
        tolist.append('a')
#        print self.tolist

c = changelist()
list1 = ['1','2']
c.change(list1)
print list1
'''

class changelist(object):

    list1 = ['1','2']

    def change(self):

        print self.list1

        self.list1.append('a')

        print self.list1
        self.list1 = []
    def showlist1(self):

        print self.list1

c = changelist()
c.change()
c.showlist1()
