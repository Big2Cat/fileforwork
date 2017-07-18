#!/usr/bin/env python
# encoding: utf-8
class TransValue(object):

    value = 0
    @classmethod
    def set_value(self,input_value):

        self.value = input_value
    @classmethod
    def get_value(self):

        valueRes = self.value

        return valueRes
